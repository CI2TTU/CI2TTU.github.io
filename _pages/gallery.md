---
layout: page
title: Gallery
permalink: /gallery/
nav: true
nav_order: 6
description: Life in the CI² Lab — trips, talks, and time together.
---

{% assign gallery_imgs = site.static_files | where_exp: "f", "f.path contains '/assets/img/gallery/'" | sort: "name" %}

<div class="ci2-gallery">
{% for img in gallery_imgs %}
  {% assign ext = img.extname | downcase %}
  {% if ext == ".jpg" or ext == ".jpeg" or ext == ".png" %}
    {% include figure.liquid path=img.path class="ci2-gallery-img" sizes="(max-width: 575px) 95vw, (max-width: 991px) 45vw, 30vw" %}
  {% endif %}
{% endfor %}
</div>

<style>
  .ci2-gallery {
    column-count: 3;
    column-gap: 1rem;
    margin-top: 0.5rem;
  }
  @media (max-width: 991px) { .ci2-gallery { column-count: 2; } }
  @media (max-width: 575px) { .ci2-gallery { column-count: 1; } }

  .ci2-gallery figure {
    break-inside: avoid;
    margin: 0 0 1rem;
  }
  .ci2-gallery img {
    width: 100%;
    height: auto;
    border-radius: 0.6rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
    cursor: zoom-in;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  .ci2-gallery img:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.16);
  }
</style>
