---
layout: page
title: "Categorías"
subtitle: "Explora los artículos por tema."
permalink: /categories/
---

<div id="archives">
{% for category in site.categories %}
  <div class="archive-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <h3 id="#{{ category_name | slugify }}">{{ category_name }}</h3>
    <a name="{{ category_name | slugify }}"></a>
    {% for post in site.categories[category_name] %}
    <article class="archive-item">
      <h4><a href="{{ root_url }}{{ post.url }}">{{post.title}}</a></h4>
      <p class="post-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%d de %B de %Y" }}</time>
      </p>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>