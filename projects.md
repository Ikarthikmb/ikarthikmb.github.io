---
layout: page
title: Projects
permalink: /projects/
---

<div class="terminal-log">
  {% assign sorted_projects = site.projects | sort: 'date' | reverse %}
  {% for project in sorted_projects %}
    <a href="{{ project.url }}" class="log-line">
      <span class="log-date">[{{ project.date | date: "%y.%m.%d" }}]</span>
      
      <span class="log-title">{{ project.title | downcase | replace: " ", "_" }}.prj</span>
      
      <div class="log-tags">
        {% for tag in project.tags limit:2 %}
          <span class="tag-item">{{ tag | upcase }}</span>
        {% endfor %}
      </div>
    </a>
  {% endfor %}
</div>
