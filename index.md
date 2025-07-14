---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: home
---

<style>
  .section {
    margin-bottom: 2.5rem;
  }

  .section h2 {
    font-size: 1.6rem;
    margin-bottom: 1rem;
    border-bottom: 2px solid #eaecef;
    padding-bottom: 0.4rem;
    color: #2c3e50;
  }

  .item-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
  }

  .item-list li {
    margin-bottom: 1.2rem;
  }

  .item-list a {
    font-size: 1.1rem;
    font-weight: 600;
    color: #007acc;
    text-decoration: none;
  }

  .item-list a:hover {
    text-decoration: underline;
  }

  .excerpt {
    font-size: 0.95rem;
    color: #555;
    margin-top: 0.2rem;
  }

  .more-link {
    display: inline-block;
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: #333;
  }

  .more-link:hover {
    color: #007acc;
  }
</style>

<div class="section">
  <h2>🛠️ Featured Projects</h2>
  <ul class="item-list">
    {% assign featured_projects = site.projects | sort: 'date' | reverse | slice: 0, 3 %}
    {% for project in featured_projects %}
      <li>
        <a href="{{ project.url }}">{{ project.title }}</a>
        <div class="excerpt">{{ project.excerpt | default: project.content | strip_html | truncate: 120 }}</div>
      </li>
    {% endfor %}
  </ul>
  <a class="more-link" href="/projects/">🔗 See all projects</a>
</div>

<div class="section">
  <h2>📝 Recent Blog Posts</h2>
  <ul class="item-list">
    {% assign latest_posts = site.posts | slice: 0, 3 %}
    {% for post in latest_posts %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <div class="excerpt">{{ post.excerpt | default: post.content | strip_html | truncate: 120 }}</div>
      </li>
    {% endfor %}
  </ul>
  <a class="more-link" href="/blog/">🔗 Read all blog posts</a>
</div>

<div class="section">
  <h2>📫 Contact</h2>
  <p style="font-size: 0.95rem; color: #444;">
    Connect with me for RTL/ASIC projects, collaborations, or research ideas:
    <br>
    <a href="mailto:b.karthikmahendra@gmail.com">📧 b.karthikmahendra@gmail.com</a><br>
    <a href="https://github.com/ikarthikmb" target="_blank">💻 GitHub</a> |
    <a href="https://www.linkedin.com/in/karthikmahendra" target="_blank">LinkedIn</a>
  </p>
</div>

