---
layout: page
title: Tutorials
permalink: /tutorials/
---

Notes and write-ups on RTL design and verification — the things I wish someone had explained to me plainly the first time.

<div class="terminal-log">
  {% assign sorted_wiki = site.wiki | sort: 'date' | reverse %}
  {% for entry in sorted_wiki %}
    <a href="{{ entry.url | relative_url }}" class="log-line">
      <span class="log-date">{{ entry.date | date: "%b %-d, %Y" }}</span>
      <span class="log-title">{{ entry.title }}</span>
      {% if entry.tags %}
      <div class="log-tags">
        {% for tag in entry.tags limit:2 %}<span class="tag-item">{{ tag }}</span>{% endfor %}
      </div>
      {% endif %}
    </a>
  {% endfor %}
</div>

### Reference Guides

External write-ups and references for getting started with Verilog and hardware design.

- [Data Types in Verilog HDL](/codeviewer.html?file=https://github.com/Ikarthikmb/VerilogFod/blob/main/data_types/data_types.v) — a primer on Verilog data types, essential for anyone working with hardware description languages.
- [Code Questions on Data Types](/codeviewer.html?file=https://github.com/Ikarthikmb/VerilogFod/blob/main/assignment2.md) — exercises to test your understanding of Verilog data types.
- [Icarus Verilog + GTKWave Guide](/pdfviewer.html?file=https://github.com/Ikarthikmb/VerilogFod/blob/main/References/Icarus_Verilog_GTKWave_guide.pdf) — how to simulate and visualize Verilog designs with Icarus Verilog and GTKWave.
- [OpenRAM Configuration for 4kB SRAM using sky130](https://github.com/Ikarthikmb/OpenRAM_Tech/blob/main/README.md) — configuring OpenRAM to generate an SRAM macro on the sky130 PDK.
- Memory maps for engineering concepts: [Antennas](/pdfviewer.html?file=https://github.com/Ikarthikmb/MindMaps_xmind/tree/master/Engineering-subject-memory-maps/Antennas.pdf), [Computer Networks](/pdfviewer.html?file=https://github.com/Ikarthikmb/MindMaps_xmind/tree/master/Engineering-subject-memory-maps/Computer-Networks.pdf), [Cryptography](/pdfviewer.html?file=https://github.com/Ikarthikmb/MindMaps_xmind/tree/master/Engineering-subject-memory-maps/Crypto.pdf), [Modern Communication](/pdfviewer.html?file=https://github.com/Ikarthikmb/MindMaps_xmind/tree/master/Engineering-subject-memory-maps/Digital-communication.pdf), [Evolution of Semiconductors](/pdfviewer.html?file=https://github.com/Ikarthikmb/MindMaps_xmind/tree/master/Engineering-subject-memory-maps/Evolution-of-semiconductors.pdf), [Microwave Devices](/pdfviewer.html?file=https://github.com/Ikarthikmb/MindMaps_xmind/tree/master/Engineering-subject-memory-maps/Microwave-Devices.pdf)
