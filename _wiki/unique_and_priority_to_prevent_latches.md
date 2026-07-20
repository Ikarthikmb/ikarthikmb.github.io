---
title: "Using unique and priority to Prevent Latches"
date: 2026-07-19
tags: [SystemVerilog, RTL]
excerpt: >
  unique and priority as a contract with the synthesis tool — and the gold standard for latch-free combinational logic.
---

Using `unique` and `priority` inside an `always_comb` block is the gold standard for writing robust, synthesis-friendly combinational logic. These keywords act as a "contract" between you and the synthesis tool, ensuring that your hardware implementation exactly matches your logical intent and preventing the accidental inference of **latches**.

### Why Unintended Latches Happen

An unintended latch occurs when a signal is not assigned a value in every possible logical path. The synthesis tool assumes the signal must "remember" its previous value, thus inserting a latch.

`always_comb` inherently helps by automatically triggering on all inputs, but it cannot "see" your logical gaps—unless you use `unique` or `priority`.

---

### Eliminating Latches with `unique` and `priority`

When you apply these to a `case` or `if-else` statement, you are telling the synthesizer: *"I have accounted for all scenarios, and there are no missing paths."*

#### 1. The `unique` Approach (Best for MUX/Decoders)

`unique` enforces both **completeness** (every possible value of the selector is covered) and **exclusivity** (no overlapping conditions). Because it forces completeness, the synthesis tool knows you don't need a latch for any "missing" cases.

```systemverilog
always_comb begin
    // If sel is 2'b11, the simulator will throw a warning
    // because it wasn't explicitly covered.
    unique case (sel)
        2'b00: out = a;
        2'b01: out = b;
        2'b10: out = c;
        2'b11: out = d; // Completeness ensures no latch is inferred
    endcase
end

```

#### 2. The `priority` Approach (Best for Priority Encoders)

`priority` ensures that the first true condition is evaluated, but it also warns you if no condition is met. By using it in an `if-else` chain, you can ensure that the "else" branch is logically handled, preventing latches.

```systemverilog
always_comb begin
    priority if (req0)      out = data0;
    else if (req1)          out = data1;
    else if (req2)          out = data2;
    else                    out = '0; // The 'else' forces completeness
end

```

---

### Visualization: How Synthesis Interprets Your Intent

* **Standard (No keyword):** The tool sees a potential "hole" in your logic. To play it safe, it inserts a latch to hold the state. This creates hardware that is larger and slower than you intended.
* **With `unique`/`priority`:** The tool treats your code as a complete, fully specified boolean function. It optimizes away any need for memory, producing clean, "pure" combinational logic gates.

### Summary Checklist to Avoid Latches

* **Default Assignments:** Always initialize variables at the very top of your `always_comb` block (e.g., `out = 0;`). If a path is missed, the default holds, preventing a latch.
* **Use `unique case`:** It forces you to cover every input value, making "missing" branches impossible.
* **Complete your `if-else`:** If you use `priority`, ensure an `else` clause exists to capture the final state.
