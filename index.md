---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: home
title: Home
---

Welcome home!

## Top Projects

<ul>
  {% assign top_projects = site.projects | sort: 'date' | reverse | slice: 0,3 %}
  {% for project in top_projects %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endfor %}
</ul>

## Latest Blog Posts

<ul>
  {% assign top_posts = site.posts | slice: 0,3 %}
  {% for post in top_posts %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

