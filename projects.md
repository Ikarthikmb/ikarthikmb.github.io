---
layout: page
title: Projects
permalink: /projects/
---

<ul>
  {% assign sorted_projects = site.projects | sort: 'date' | reverse %}
  {% for project in sorted_projects %}
    <li style="margin-bottom: 1.5rem;">
      <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
      <p>
        {% if project.excerpt %}
          {{ project.excerpt }}
        {% else %}
          {{ project.content | strip_html | truncatewords: 30 }}
        {% endif %}
      </p>
    </li>
  {% endfor %}
</ul>

<h2>📦 GitHub Projects</h2>
<ul class="item-list">
<li>
	<a href="https://github.com/Ikarthikmb/ACORN128b2025/tree/state_in_top" target="_blank">
	🔐 ACORN128b2025 (state_in_top branch)
	</a>
	<div class="excerpt">
	RTL hardware implementation of the ACORN authenticated encryption cipher. This branch structures the state machine at the top level for better modularity and clarity.
	</div>
</li>
<!-- Add more projects here -->
</ul>
<a class="more-link" href="https://github.com/Ikarthikmb" target="_blank">🔗 View all repositories on GitHub</a>
