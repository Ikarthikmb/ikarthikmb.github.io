---
layout: page
permalink: /blog/
---

<ul>
  {% assign sorted_posts = site.blog | where: "draft", false | sort: 'date' | reverse %}
  {% for post in sorted_posts %}
    <li style="margin-bottom: 1.5rem;">
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p>
        {% if post.excerpt %}
          {{ post.excerpt }}
        {% else %}
          {{ post.content | strip_html | truncatewords: 30 }}
        {% endif %}
      </p>
    </li>
  {% endfor %}
</ul>

