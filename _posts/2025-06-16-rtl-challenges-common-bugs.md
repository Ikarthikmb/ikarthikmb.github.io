---
title: Most common RTL Bugs and How they are Fixed
date: 2025-05-16T07:40:13-05:30
author: Karthik Mahendra
avatar: /me.png
authorlink: https://ikarthikmb.github.io
cover: 
categories:
  - projects
tags:
  - articles
nolastmod: true
draft: false

---

## Incomplete Sensitivity:

**Potential Issue**: In combinational always blocks, missing signals in the sensitivity list can result in synthesis-simulation mismatches and unintended latches.

**Example code**: 

![example](/static/posts/common_rtl_bugs/image5.png)
![waveform](/static/posts/common_rtl_bugs/image8.png)

Notice how the output ‘latch_out’ is still 0 after c is turned HIGH at 10ns. This is because the synthesis infers a latch as simulation is incorrect because ‘c’ isn’t in the sensitivity list. 

**Try it out**: https://edaplayground.com/x/KdCM


## Unused Signals, Ports:

**Potential Issue**: Defining signals or ports that are never used leads to extra logic or inferred latches that confuse formal tools and verification. 

**Example code**:

![example](/static/posts/common_rtl_bugs/image11.png)

**Try it out**: https://edaplayground.com/x/Yatc


## Poor Clock Gating:

**Potential Issue**: Using combinational logic to gate clocks directly leads to glitches. This is dangerous because even tiny glitches can toggle flip-flops unexpectedly, breaking state machines or corrupting data paths.

**Example code**:

![Example](/static/posts/common_rtl_bugs/image1.png)
![waveform](/static/posts/common_rtl_bugs/image4.png)


**Try it out**: (https://edaplayground.com/x/iYSV)[https://edaplayground.com/x/iYSV]


## Non-Full case statement:

**Potential Issue**: Case missing a default statement and not covering all input values leads to implied latches

**Example code**:

![example](/static/posts/common_rtl_bugs/image7.png)
![waveform](/static/posts/common_rtl_bugs/image6.png)


**Try it out**: (https://edaplayground.com/x/YM3E)[https://edaplayground.com/x/YM3E]



## Missing Else

**Potential Issue**: Missing final else in multi-branch if-else-if leads to incomplete assignments and latches.

**Example code**:

![example code](/static/posts/common_rtl_bugs/image9.png)
![waveform](/static/posts/common_rtl_bugs/image10.png)


**Try it out**: (https://edaplayground.com/x/KzCh)[https://edaplayground.com/x/KzCh]



## Blocking vs Non‑Blocking in Sequential Blocks

**Potential Issue**: Using blocking assignments (=) in sequential always @(posedge clk) blocks can lead to order-sensitive bugs that are difficult to spot.

**Example code**:

![example code](/static/posts/common_rtl_bugs/image3.png)


## Width Mismatch in Assignments

**Potential Issue**: Assigning a wider signal to a narrower one leads to silent truncation. No error or warning by default. In control or address buses, this could be catastrophic.


**Example code**: 

![example code](/static/posts/common_rtl_bugs/image2.png)

