---
name: x64dbg-debugger
description: Low-level native debugging, crash diagnosis, assembly inspection, memory analysis, and execution flow control using x64dbg/x32dbg via the x64dbg-bridge MCP server.
---

# x64dbg Low-Level Debugger Skill

This skill teaches the Antigravity agent how to leverage native Windows debugging capabilities using **x64dbg** / **x32dbg** through the `x64dbg-bridge` MCP server.

---

## When to Activate This Skill
Activate this skill when:
* Diagnosing process crashes, unhandled exceptions (`STATUS_ACCESS_VIOLATION`, `0xC0000005`, `STATUS_STACK_BUFFER_OVERRUN`).
* Inspecting compiled binaries (C, C++, Rust, Go, Zig, Assembly) at the machine-code level.
* Verifying memory contents, pointer validity, and structures in heap/stack memory.
* Analyzing compiler code generation and optimization effects.
* Setting breakpoints and stepping through execution (`step_into`, `step_over`, `resume`).

---

## Tool Reference (`x64dbg-bridge`)

| Tool | Purpose | Key Parameters |
| :--- | :--- | :--- |
| `x64dbg_status` | Check bridge connection, attached process PID, architecture and execution state (`PAUSED`, `RUNNING`, `STOPPED`). | None |
| `x64dbg_get_registers` | Retrieve all 64-bit and 32-bit registers (RAX, RBX, RCX, RDX, RSI, RDI, RSP, RBP, RIP, R8-R15, EFLAGS). | None |
| `x64dbg_disasm` | Disassemble instructions at a memory address or from current `RIP`. | `address` (string), `count` (number, default: 5) |
| `x64dbg_read_memory` | Read memory block and display canonical Hex + ASCII dump. | `address` (string), `size` (number, default: 32) |
| `x64dbg_set_breakpoint` | Place a breakpoint on an address or exported API symbol. | `address` (string), `type` (software/hardware/memory) |
| `x64dbg_control_execution`| Step or continue execution. | `action`: `step_into`, `step_over`, `pause`, `resume` |
| `x64dbg_get_callstack` | Extract active thread frames and return addresses. | None |
| `x64dbg_eval` | Evaluate an expression using the x64dbg engine (e.g., `[rsp+8]`, `rax & 0xFF`). | `expression` (string) |
| `x64dbg_exec_command` | Execute a raw command in x64dbg's console. | `command` (string) |

---

## Diagnostic Workflows

### 1. Investigating an Access Violation Crash
1. Call `x64dbg_status` to ensure the debugger is paused on the exception.
2. Call `x64dbg_get_registers` to inspect `RIP` (failing instruction) and pointers in `RAX`, `RCX`, `RDX`, `RSI`, `RDI`.
3. Call `x64dbg_disasm` at `address: "rip"` with `count: 5` to view the failing instruction.
   * *Example:* If instruction is `mov [rax], rcx` and `rax == 0x0000000000000000`, this is a confirmed Null Pointer Dereference.
4. Call `x64dbg_get_callstack` to identify the chain of function callers.
5. Correlate the crash location with source code line numbers and generate an actionable RCA (Root Cause Analysis).

### 2. Windows x64 Calling Convention Guide (Microsoft ABI)
When analyzing disassembled functions in Windows x64 binaries:
* **Arguments:**
  * 1st argument: `RCX` (or `XMM0` for float/double)
  * 2nd argument: `RDX` (or `XMM1`)
  * 3rd argument: `R8` (or `XMM2`)
  * 4th argument: `R9` (or `XMM3`)
  * 5th+ arguments: Pushed onto stack at `[RSP + 0x20]`, `[RSP + 0x28]`, etc.
* **Shadow Space:** The caller *must* allocate 32 bytes of shadow store before the `CALL` instruction (`sub rsp, 28h` or `sub rsp, 20h`).
* **Return Value:** Stored in `RAX` (integer/pointer) or `XMM0` (float/double).
* **Non-Volatile Registers (must be preserved across calls):** `RBX`, `RBP`, `RDI`, `RSI`, `R12`, `R13`, `R14`, `R15`.
* **Volatile Registers (can be destroyed by callee):** `RAX`, `RCX`, `RDX`, `R8`, `R9`, `R10`, `R11`.
