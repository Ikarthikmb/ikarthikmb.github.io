---
layout: page
title: Logs
permalink: /logs/
---

<div class="terminal-log">
  {% assign sorted_posts = site.logs | where: "draft", false | sort: 'date' | reverse %}
  {% for post in sorted_posts %}
    <a href="{{ post.url | relative_url }}" class="log-line">
      <span class="log-date">{{ post.date | date: "%b %-d, %Y" }}</span>
      <span class="log-title">{{ post.title }}</span>

      {% if post.tags %}
      <div class="log-tags">
        {% for tag in post.tags limit:2 %}
          <span class="tag-item">{{ tag }}</span>
        {% endfor %}
      </div>
      {% endif %}
    </a>
  {% endfor %}
</div>
