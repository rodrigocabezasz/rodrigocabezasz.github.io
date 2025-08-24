---
layout: page
title: Blog
subtitle: "Aquí comparto reflexiones y aprendizajes sobre datos, tecnología y gestión."
permalink: /blog/
---

<div class="posts-list">
  {% for post in site.posts %}
    <article class="post-preview">
      <a href="{{ post.url | relative_url }}">
        <h2 class="post-title">{{ post.title }}</h2>
        {% if post.subtitle %}
          <h3 class="post-subtitle">{{ post.subtitle }}</h3>
        {% endif %}
      </a>
      <p class="post-meta">
        Publicado el
        <time datetime="{{ post.date | date_to_xmlschema }}">
          {{ post.date | date: "%d de %B de %Y" }}
        </time>
      </p>
      <div class="post-entry">
        {{ post.excerpt | strip_html | xml_escape | truncatewords: 50 }}
        <a href="{{ post.url | relative_url }}" class="post-read-more">[Leer más]</a>
      </div>
    </article>
    <hr class="my-4">
  {% endfor %}
</div>