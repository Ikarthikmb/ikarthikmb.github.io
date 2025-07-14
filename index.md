---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: home
---

<div class="home">
  <!-- Featured Section -->
  <div class="section">
    <h2>Featured</h2>
    <ul class="item-list">
      {% assign combined = site.projects | concat: site.blog | sort: 'date' | reverse %}
      {% for item in combined limit:8 %}
        <li>
          <span class="tag">
            {% if item.collection == 'projects' %}[Project]{% elsif item.collection == 'blog' %}[Blog]{% endif %}
          </span>
          <a href="{{ item.url }}">{{ item.title }}</a>
          <div class="excerpt">
            {{ item.excerpt | default: item.content | strip_html | truncatewords: 25 }}
          </div>
        </li>
      {% endfor %}
    </ul>
  </div>
</div>

### A Little About Me

Hey, I’m Karthik - a Digital Design Engineer with extensive professional experience in RTL design, formal verification, and hardware development. I graduated from Purdue with an M.S. in ECE, focusing on implementing hardware for the [ACORN Encryption Decryption algorithm in Verilog](https://github.com/Ikarthikmb/ACORN128b2025/tree/state_in_top).

My journey started with hands-on work in protocols like PCIe, I2C, UART, and AMBA, later evolving to IP development, synthesizable RTL, and analysis for lint, CDC, RDC, and power.

### Highlights
- **1st Place**, 600+ submissions in *["Circuit Design and Simulation Marathon using eSim"](https://www.linkedin.com/posts/activity-6833789615363657728-py75?utm_source=share&utm_medium=member_desktop&rcm=ACoAACyJs6IBHF0R8VMjlhgjaOi-3OXpyN-R9vs)* [June 2021]
- **5th Place** in the *["IEEE HKN Founders Day Hackathon"](https://hkn.ieee.org/news-and-announcements/2024/11/first-hkn-international-hackathon#:~:text=Coders%2C%20Jumbos%2C%20and-,Leo,-.)* [October 2024]
- **Top 52** in *["Capture the Bug - A Design Verification Hackathon"](https://www.linkedin.com/posts/activity-6975543672410886144-VcwP?utm_source=share&utm_medium=member_desktop&rcm=ACoAACyJs6IBHF0R8VMjlhgjaOi-3OXpyN-R9vs)* [September 2022]

### Workshops & Speaking
- **Speaker & Workshop Instructor**, *["Sand to Silicon: Build Your Custom ASICs"](https://www.linkedin.com/posts/activity-7322883938060828672-fHcn/?utm_source=share&utm_medium=member_desktop&rcm=ACoAACyJs6IBHF0R8VMjlhgjaOi-3OXpyN-R9vs)*, Purdue University [March, April 2025]
- **ECE Department Internship Instructor**, Purdue University [January - May 2025]
- **PCB Design Workshop Instructor**, Design Studio at Purdue University [March 29th, October 25th, 2024]

Feel free to explore my portfolio, projects, and blog. Let’s connect and build the future of silicon!

