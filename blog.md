---
layout: page
title: Blog
subtitle: Reflexiones y aprendizajes sobre datos, tecnología y gestión.
---

<div class="posts-list">
  {% for post in paginator.posts %}
    <article class="post-preview">
      <a href="{{ post.url | prepend: site.baseurl }}">
        <h2 class="post-title">{{ post.title }}</h2>
        {% if post.subtitle %}
          <h3 class="post-subtitle">{{ post.subtitle }}</h3>
        {% endif %}
      </a>
      <p class="post-meta">
        Publicado el {{ post.date | date: "%d de %B de %Y" }}
      </p>
    </article>
    <hr>
  {% endfor %}
</div>

<!-- Paginación -->
{% if paginator.total_pages > 1 %}
<ul class="pager main-pager">
  {% if paginator.previous_page %}
  <li class="previous">
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl | replace: '//', '/' }}">&larr; Posts Recientes</a>
  </li>
  {% endif %}
  {% if paginator.next_page %}
  <li class="next">
    <a href="{{ paginator.next_page_path | prepend: site.baseurl | replace: '//', '/' }}">Posts Antiguos &rarr;</a>
  </li>
  {% endif %}
</ul>
{% endif %}