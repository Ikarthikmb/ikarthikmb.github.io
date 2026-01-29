---
layout: page
title: Logs
permalink: /logs/
---

<div class="terminal-log">
  {% assign sorted_posts = site.logs | where: "draft", false | sort: 'date' | reverse %}
  {% for post in sorted_posts %}
    <a href="{{ post.url }}" class="log-line">
      <span class="log-date">[{{ post.date | date: "%y.%m.%d" }}]</span>
      <span class="log-title">{{ post.title | downcase | replace: " ", "_" }}.log</span>
      
      {% if post.tags %}
      <div class="log-tags">
        {% for tag in post.tags limit:1 %}
          <span class="tag-item">{{ tag | upcase }}</span>
        {% endfor %}
      </div>
      {% endif %}
    </a>
  {% endfor %}
</div>
