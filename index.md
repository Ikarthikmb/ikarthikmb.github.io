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

<h1>Hi, welcome to Qarbyte</h1>

<h2>🛠️ Featured Projects</h2>
<ul>
  {% assign top_projects = site.projects | sort: 'date' | reverse | slice: 0, 3 %}
  {% for project in top_projects %}
    <li>
      <h3><a href="{{ project.url }}">{{ project.title }}</a></h3>
      <p>{{ project.excerpt }}</p>
    </li>
  {% endfor %}
</ul>
<a href="/projects/">See All Projects →</a>

<h2>📝 Latest Blog Posts</h2>
<ul>
  {% for post in site.posts limit:3 %}
    <li>
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>
<a href="/blog/">Read All Posts →</a>

