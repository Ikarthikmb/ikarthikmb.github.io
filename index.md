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
      {% assign combined = site.projects | concat: site.blog %}
      {% assign sorted_combined = combined | sort: 'date' | reverse %}
      {% for item in sorted_combined limit:8 %}
        <li>
          <span class="tag">
            {% if item.collection == 'projects' %}[Project]{% elsif item.collection == 'blog' %}[Blog]{% endif %}
          </span>
          <a href="{{ item.url }}">{{ item.title }}</a>
          <div class="excerpt">
            {% if item.excerpt %}
              {{ item.excerpt | truncatewords: 25 }}
            {% else %}
              {{ item.content | strip_html | truncatewords: 30 }}
            {% endif %}
          </div>
        </li>
      {% endfor %}
    </ul>
  </div>

---

### A Little About Me

Hey, I’m Karthik - a Digital Design Engineer with extensive professional experience in RTL design, formal verification, and hardware development. Graduated from Purdue with M.S in ECE, focused on implementing hardware for [ACORN Encryption Decryption algorithm in verilog](https://github.com/Ikarthikmb/ACORN128b2025/tree/state_in_top).

My engineering journey began with hands-on experience in protocols like PCIe, I2C, UART, and AMBA, and evolved through developing IPs, writing synthesizable RTL, and performing lint, CDC, RDC, and power analysis. Whether I'm implementing CDC FIFOs or debugging formal runs, I approach each task with precision and a passion for clean, efficient design.

### Highlights

- **1st Place**, 600+ submissions in the *["Circuit Design and Simulation Marathon using eSim"](https://www.linkedin.com/posts/activity-6833789615363657728-py75?utm_source=share&utm_medium=member_desktop&rcm=ACoAACyJs6IBHF0R8VMjlhgjaOi-3OXpyN-R9vs)* [June 2021]
- **5th Place** out of 12 teams in the *["IEEE HKN Founders Day Hackathon"](https://hkn.ieee.org/news-and-announcements/2024/11/first-hkn-international-hackathon#:~:text=Coders%2C%20Jumbos%2C%20and-,Leo,-.)* [October 2024]
- **Top 52** out of 400 finalists in the *["Capture the Bug - A Design Verification Hackathon"](https://www.linkedin.com/posts/activity-6975543672410886144-VcwP?utm_source=share&utm_medium=member_desktop&rcm=ACoAACyJs6IBHF0R8VMjlhgjaOi-3OXpyN-R9vs)* [September 2022]

### Workshops & Speaking

- **Speaker & Workshop Instructor**, *["Sand to Silicon: Build Your Custom ASICs"](https://www.linkedin.com/posts/activity-7322883938060828672-fHcn/?utm_source=share&utm_medium=member_desktop&rcm=ACoAACyJs6IBHF0R8VMjlhgjaOi-3OXpyN-R9vs)*, Purdue University [March, April 2025]  
  Led a live session to design a **stopwatch in Verilog** and guided participants in deploying their programs on the **Terasic DE10 Lite FPGA board**.

- **ECE Department Internship Instructor**, Purdue University [January - May 2025]  
  Under the guidance of **Dr. Lizhe Tan**, led an internship for a small group of high school students, teaching them the basics of **electronics**, **PCB design**, and **digital logic concepts**. They successfully designed a **traffic signal controller** and a **vending machine**, standing out for their strong grasp of the material.

- **PCB Design Workshop Instructor**, Design Studio at Purdue University [March 29th, October 25th, 2024]  
  Conducted a hands-on workshop covering **PCB fundamentals**, including a live session on drawing schematics and trace routing using **KiCad**. Participants then soldered components onto their own PCB boards.


  Feel free to explore my portfolio, projects, and blog. Let’s connect and build the future of silicon
