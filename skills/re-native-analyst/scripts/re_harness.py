import os
import sys
import json
import math
import struct
import argparse
from typing import Dict, Any, List

def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    entropy = 0.0
    length = len(data)
    occurrences = [0] * 256
    for byte in data:
        occurrences[byte] += 1
    for count in occurrences:
        if count > 0:
            p_x = count / length
            entropy -= p_x * math.log2(p_x)
    return round(entropy, 4)

def parse_pe_minimal(file_path: str) -> Dict[str, Any]:
    result = {
        "format": "Unknown",
        "file_size": 0,
        "is_pe": False,
        "machine": "Unknown",
        "number_of_sections": 0,
        "entry_point_rva": "0x0",
        "image_base": "0x0",
        "sections": [],
        "high_entropy_detected": False
    }

    if not os.path.isfile(file_path):
        result["error"] = f"File not found: {file_path}"
        return result

    result["file_size"] = os.path.getsize(file_path)

    with open(file_path, "rb") as f:
        data = f.read(4096)

    if len(data) < 64 or data[:2] != b"MZ":
        if data[:4] == b"\x7fELF":
            result["format"] = "ELF Linux/Unix"
            return result
        result["format"] = "Raw / Non-PE"
        return result

    result["is_pe"] = True
    pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
    with open(file_path, "rb") as f:
        f.seek(pe_offset)
        pe_header_data = f.read(1024)

    if len(pe_header_data) < 24 or pe_header_data[:4] != b"PE\x00\x00":
        result["format"] = "MS-DOS Stub / Corrupted PE"
        return result

    machine, num_sections, _, _, _, opt_hdr_size, _ = struct.unpack_from("<HHIIIHH", pe_header_data, 4)
    result["number_of_sections"] = num_sections

    machines = {
        0x014c: "x86 (32-bit)",
        0x8664: "x64 (64-bit AMD64)",
        0xaa64: "ARM64"
    }
    result["machine"] = machines.get(machine, f"0x{machine:04x}")

    opt_header_offset = 24
    if opt_hdr_size > 0 and len(pe_header_data) >= opt_header_offset + 2:
        opt_magic = struct.unpack_from("<H", pe_header_data, opt_header_offset)[0]
        if opt_magic == 0x010b:
            entry_point, _, image_base = struct.unpack_from("<III", pe_header_data, opt_header_offset + 16)
            result["format"] = "PE32 (32-bit)"
            result["entry_point_rva"] = hex(entry_point)
            result["image_base"] = hex(image_base)
        elif opt_magic == 0x020b:
            entry_point = struct.unpack_from("<I", pe_header_data, opt_header_offset + 16)[0]
            image_base = struct.unpack_from("<Q", pe_header_data, opt_header_offset + 24)[0]
            result["format"] = "PE32+ (64-bit)"
            result["entry_point_rva"] = hex(entry_point)
            result["image_base"] = hex(image_base)

    sections_start = pe_offset + 24 + opt_hdr_size
    with open(file_path, "rb") as f:
        f.seek(sections_start)
        sec_table_data = f.read(num_sections * 40)

    with open(file_path, "rb") as f:
        for i in range(num_sections):
            sec_bytes = sec_table_data[i * 40 : (i + 1) * 40]
            if len(sec_bytes) < 40:
                break
            sec_name = sec_bytes[:8].decode("latin-1", errors="replace").rstrip("\x00")
            virt_size, virt_addr, raw_size, raw_ptr = struct.unpack_from("<IIII", sec_bytes, 8)

            f.seek(raw_ptr)
            sec_raw = f.read(min(raw_size, 512 * 1024))
            sec_ent = calculate_entropy(sec_raw) if sec_raw else 0.0

            if sec_ent >= 7.2:
                result["high_entropy_detected"] = True

            result["sections"].append({
                "name": sec_name,
                "virtual_address": hex(virt_addr),
                "virtual_size": hex(virt_size),
                "raw_size": raw_size,
                "entropy": sec_ent,
                "packed": sec_ent >= 7.2
            })

    return result

def extract_safe_strings(file_path: str, min_len: int = 5, limit: int = 50) -> List[str]:
    if not os.path.isfile(file_path):
        return []

    strings_found = []
    with open(file_path, "rb") as f:
        content = f.read(1024 * 1024)

    current_ascii = []
    for byte in content:
        if 0x20 <= byte <= 0x7E:
            current_ascii.append(chr(byte))
        else:
            if len(current_ascii) >= min_len:
                s = "".join(current_ascii)
                clean = s.replace("\r", " ").replace("\n", " ").strip()
                if clean:
                    strings_found.append(clean)
                if len(strings_found) >= limit:
                    break
            current_ascii = []

    return strings_found

def main():
    parser = argparse.ArgumentParser(description="CLI-Anything Deterministic RE Harness")
    parser.add_argument("target", help="Path to target binary")
    parser.add_argument("--json", action="store_true", help="Emit strict JSON dictionary output")
    parser.add_argument("--strings", action="store_true", help="Extract sanitized strings")
    parser.add_argument("--limit", type=int, default=40, help="Max strings limit")

    args = parser.parse_args()
    triage = parse_pe_minimal(args.target)

    if args.strings:
        triage["extracted_strings_evidence"] = extract_safe_strings(args.target, min_len=4, limit=args.limit)

    if args.json:
        print(json.dumps(triage, indent=2, ensure_ascii=False))
    else:
        print(f"Format: {triage.get('format')} | Machine: {triage.get('machine')} | EP: {triage.get('entry_point_rva')}")

if __name__ == "__main__":
    main()
