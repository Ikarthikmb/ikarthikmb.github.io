---
layout: page
title: Projects
permalink: /projects/
---

<ul>
  {% assign sorted_projects = site.projects | sort: 'date' | reverse %}
  {% for project in sorted_projects %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endfor %}
</ul>

