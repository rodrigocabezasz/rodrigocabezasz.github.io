---
layout: page
title: "Blog"
---


## Blog

Bienvenido a mi blog. Aquí comparto reflexiones y aprendizajes sobre datos, tecnología y gestión.

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url | relative_url }})
<small>{{ post.date | date: "%d de %B de %Y" }}</small>

{{ post.excerpt }}
---
{% endfor %}