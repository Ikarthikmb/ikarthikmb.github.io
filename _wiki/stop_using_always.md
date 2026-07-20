---
title: "Stop Using always: A Guide to Modern SystemVerilog Blocks"
date: 2026-07-19
tags: [SystemVerilog, RTL]
excerpt: >
  Why always_comb, always_ff, and always_latch replaced the classic always block, and what that means for synthesis.
---

Procedural blocks in SystemVerilog are the primary constructs used to model the behavioral logic of a design. Unlike continuous assignments (which are always active), procedural blocks contain sequences of statements that execute when triggered by specific events or conditions.

### History and Evolution

* The predecessor to SystemVerilog’s specialized procedural blocks is the **Verilog HDL** (specifically Verilog-1995 and Verilog-2001). In these versions, designers relied on a single, general-purpose `always` block to model everything: combinational logic, sequential flip-flops, and latches. This often led to unintended synthesis issues, such as inferred latches when sensitivity lists were incomplete.
* As digital systems became more complex, the need for clearer design intent and more robust verification grew. In 2002, SystemVerilog was introduced as an extension to Verilog to address these deficiencies, bringing in advanced verification features and better hardware modeling constructs.
* SystemVerilog (IEEE 1800) is the modern standard that absorbed Verilog. It does not replace Verilog so much as it includes and extends it. The specialized procedural blocks (`always_comb`, `always_ff`, `always_latch`) are now the industry-standard way to write RTL, as they explicitly declare the designer's intent to synthesis tools.

---

### Procedural Blocks Overview

| Block | Purpose | Synthesis Intent |
| --- | --- | --- |
| **`initial`** | Executes once at $t=0$. | Non-synthesizable (Testbenches only). |
| **`always`** | The classic Verilog block. | Generic; prone to simulation/synthesis mismatches. |
| **`always_comb`** | Models combinational logic. | Infers logic with no memory; ensures correct triggers. |
| **`always_ff`** | Models sequential logic. | Infers flip-flops; enforces edge-triggered sensitivity. |
| **`always_latch`** | Models latched logic. | Specifically flags latch inference to avoid warnings. |
| **`final`** | Executes once at the end of simulation. | Non-synthesizable (Reporting/Statistics). |

---

### Key Concepts

* **Concurrency:** All procedural blocks in a module operate concurrently (in parallel).
* **Assignments:**
* **Blocking (`=`):** Executes sequentially. Best practice for `always_comb` and `initial` blocks.
* **Non-blocking (`<=`):** Schedules an update for the end of the time step. Essential for `always_ff` to accurately model register behavior and avoid race conditions.


* **Sensitivity Lists:** In classic `always` blocks, you must manually list every input signal. In SystemVerilog, `always_comb` automatically infers the sensitivity list, significantly reducing human error.

### Example: Intent-Driven Design

```systemverilog
// Sequential logic (Registers)
always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) q <= 1'b0;
    else        q <= d;
end

// Combinational logic (Logic gates/MUX)
always_comb begin
    // No need to list inputs; SystemVerilog handles it
    out = (sel) ? a : b; 
end

```
