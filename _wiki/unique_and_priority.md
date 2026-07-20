---
title: "Controlling Logic Flow with unique and priority"
date: 2026-07-19
tags: [SystemVerilog, Verification]
excerpt: >
  How unique and priority communicate design intent around parallelism and completeness to synthesis tools.
---

Understanding `unique` and `priority` is arguably the most important bridge between writing "code that runs" and writing "hardware that is bug-free." These keywords allow you to communicate your design intent regarding **parallelism** and **completeness** to synthesis tools, effectively acting as an automated "assertion" for your logic.

### 1. `priority`: Modeling Logic Dependencies

The `priority` keyword ensures that at least one condition in an `if-else` chain is matched. If no condition is met during simulation, the tool flags a warning. This is crucial for verifying that you have handled all possible logical paths.

* **Behavior:** It enforces a specific order of evaluation.
* **Use Case:** When you have a chain of conditions where the first match is the most important, but you want to ensure the logic isn't "missing" a scenario.

### 2. `unique`: Enforcing Exclusivity

The `unique` keyword is more restrictive. It forces two things:

1. **Exclusivity:** No two conditions can be true at the same time (no overlaps).
2. **Completeness:** Every possible input value must be covered by a case or condition (no "holes").

* **Behavior:** If more than one condition is true, or if no condition is true, the simulator issues a warning.
* **Use Case:** Ideal for state machines or decoders where you know exactly one output state should be active.

---

### Comparison Summary

| Keyword | Ensures No Overlap? | Ensures All Covered? | Typical Use Case |
| --- | --- | --- | --- |
| **None** | No | No | Simple logic where "don't cares" are intended. |
| **`priority`** | No | Yes | Priority encoders, interrupt handling. |
| **`unique`** | Yes | Yes | One-hot state machines, decoder logic. |

---

### Code Example: `unique` in a `case` statement

When you use `unique case`, you are telling the synthesis tool: *"I guarantee only one of these cases will ever be true, and I have covered every single possibility."*

```systemverilog
// If sel is 2'b11, this code will trigger a run-time warning
// because 2'b11 is not explicitly covered.
unique case (sel)
    2'b00 : out = a;
    2'b01 : out = b;
    2'b10 : out = c;
endcase

```

---

### Why this matters for the "Hardware Mindset"

Without these keywords, synthesis tools often default to "safe" (but inefficient) logic:

* **Missing `unique`:** The synthesizer may infer a larger, slower decoder than necessary because it doesn't know you intended the inputs to be mutually exclusive.
* **Missing `priority`:** You might accidentally create a design that behaves unpredictably when an undefined input occurs, which is a leading cause of silicon "bugs" that only appear in real hardware.
