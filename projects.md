---
layout: page
title: Projects
permalink: /projects/
---

Hardware, software, and everything in between — RTL designs verified and taped out to silicon, PCBs,
embedded builds, and a few software detours.

<span class="section-heading">Tapeouts &amp; Fabricated Silicon</span>
{% include tapeout.html %}

<span class="section-heading">All Projects</span>

<div class="filter-bar" id="project-filters"></div>

<div class="project-grid" id="project-grid">
  {% for project in site.projects %}
  <a class="card project-card" href="{{ project.url | relative_url }}"
     data-tags="Featured Build{% if project.tags %},{% for t in project.tags %}{{ t }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endif %}">
    <div class="project-card-body">
      <span class="tag-pill project-card-badge">Featured Build</span>
      <h3 class="project-card-title">{{ project.title }}</h3>
      <p class="project-card-desc">{{ project.excerpt | strip_html | truncatewords: 22 }}</p>
    </div>
  </a>
  {% endfor %}

  {% for project in site.data.projects %}
  <a class="card project-card" href="{{ project.link }}" target="_blank" rel="noopener noreferrer"
     data-tags="{{ project.tags | join: ',' }}">
    <div class="project-card-body">
      {% if project.featured %}<span class="tag-pill project-card-badge">Featured</span>{% endif %}
      <h3 class="project-card-title">{{ project.title }}</h3>
      <p class="project-card-desc">{{ project.description }}</p>
      <ul class="tag-list project-card-tags">
        {% for tag in project.tags %}<li class="tag-pill">{{ tag }}</li>{% endfor %}
      </ul>
    </div>
  </a>
  {% endfor %}
</div>

<script>
  (function () {
    const grid = document.getElementById('project-grid');
    const bar = document.getElementById('project-filters');
    const cards = Array.from(grid.querySelectorAll('.project-card'));

    const tags = new Set(['All']);
    cards.forEach(c => c.dataset.tags.split(',').forEach(t => t.trim() && tags.add(t.trim())));

    tags.forEach(tag => {
      const btn = document.createElement('button');
      btn.className = 'filter-btn' + (tag === 'All' ? ' active' : '');
      btn.textContent = tag;
      btn.onclick = () => {
        bar.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        cards.forEach(c => {
          const show = tag === 'All' || c.dataset.tags.split(',').map(t => t.trim()).includes(tag);
          c.style.display = show ? '' : 'none';
        });
      };
      bar.appendChild(btn);
    });
  })();
</script>

<style>
  .filter-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 1.75rem;
  }

  .filter-btn {
    font-family: 'Inter', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    padding: 6px 14px;
    border-radius: 999px;
    border: 1px solid #d8dee4;
    background: #fff;
    color: #57606a;
    cursor: pointer;
  }
  .filter-btn:hover { border-color: #1a7f37; color: #1a7f37; }
  .filter-btn.active { background: #1a7f37; border-color: #1a7f37; color: #fff; }

  .project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
  }

  .project-card { text-decoration: none; display: block; }
  .project-card-body { padding: 20px; }

  .project-card-badge { margin-bottom: 10px; }

  .project-card-title {
    font-size: 1.02rem;
    color: #1f2328;
    margin: 0 0 8px;
  }
  .project-card:hover .project-card-title { color: #1a7f37; }

  .project-card-desc {
    font-size: 0.88rem;
    color: #57606a;
    line-height: 1.55;
    margin: 0 0 12px;
  }

  .project-card-tags { margin-top: 4px; }
</style>
