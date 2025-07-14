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

