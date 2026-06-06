---
layout: page
title: People
permalink: /people/
nav: true
nav_order: 3
description: Members of the Computational Intelligence, Control &amp; Information (CI²) Lab.
---

{% assign people_groups = "faculty,phd,undergrad" | split: "," %}
{% assign group_titles = "Faculty,PhD Students,Undergraduate Students" | split: "," %}

<div class="ci2-people">
{% for group in people_groups %}
  {% assign members = site.data.members[group] %}
  {% if members and members.size > 0 %}
    <h2 class="ci2-people-heading">{{ group_titles[forloop.index0] }}</h2>
    <div class="ci2-people-grid{% if group == 'faculty' %} ci2-people-grid--faculty{% endif %}">
      {% for m in members %}
        <div class="ci2-person">
          <div class="ci2-person-photo">
            <img src="{{ m.image | prepend: '/assets/img/' | relative_url }}" alt="{{ m.name }}" loading="lazy" />
          </div>
          <h3 class="ci2-person-name">{{ m.name }}</h3>
          {% if m.title %}<p class="ci2-person-title">{{ m.title }}</p>{% endif %}
          {% if m.role %}<p class="ci2-person-role">{{ m.role }}</p>{% endif %}
          <div class="ci2-person-links">
            {% if m.email %}<a href="mailto:{{ m.email }}" title="Email {{ m.name }}" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>{% endif %}
            {% if m.website %}<a href="{{ m.website }}" target="_blank" rel="noopener" title="Website" aria-label="Website"><i class="fa-solid fa-globe"></i></a>{% endif %}
            {% if m.scholar %}<a href="{{ m.scholar }}" target="_blank" rel="noopener" title="Google Scholar" aria-label="Google Scholar"><i class="ai ai-google-scholar"></i></a>{% endif %}
            {% if m.linkedin %}<a href="{{ m.linkedin }}" target="_blank" rel="noopener" title="LinkedIn" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>{% endif %}
            {% if m.github %}<a href="{{ m.github }}" target="_blank" rel="noopener" title="GitHub" aria-label="GitHub"><i class="fa-brands fa-github"></i></a>{% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
  {% endif %}
{% endfor %}
</div>

<style>
  .ci2-people { max-width: 60rem; margin: 0 auto; }

  .ci2-people-heading {
    font-family: "Roboto Slab", serif; text-align: center;
    margin: 2rem 0 1.5rem; padding-bottom: 0.4rem;
  }

  .ci2-people-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr));
    gap: 1.75rem; margin-bottom: 1rem;
  }
  /* Faculty: center the card(s) at a comfortable width rather than stretching */
  .ci2-people-grid--faculty {
    grid-template-columns: repeat(auto-fit, minmax(13rem, 16rem));
    justify-content: center;
  }

  .ci2-person { text-align: center; }
  .ci2-person-photo {
    width: 100%; aspect-ratio: 1 / 1; max-width: 12rem; margin: 0 auto 1rem;
    border-radius: 50%; overflow: hidden;
    background: var(--global-bg-color-secondary, rgba(0,0,0,0.04));
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  }
  .ci2-person-photo img { width: 100%; height: 100%; object-fit: cover; display: block; }

  .ci2-person-name {
    font-family: "Roboto Slab", serif; font-size: 1.1rem; margin: 0 0 0.25rem;
  }
  .ci2-person-title {
    margin: 0; font-size: 0.92rem; font-weight: 600;
    color: var(--global-theme-color, #b1241f);
  }
  .ci2-person-role { margin: 0.1rem 0 0; font-size: 0.88rem; opacity: 0.75; }

  .ci2-person-links { margin-top: 0.6rem; display: flex; gap: 0.85rem; justify-content: center; }
  .ci2-person-links a {
    font-size: 1.05rem; color: var(--global-text-color-light, #828282);
    transition: color 0.15s ease;
  }
  .ci2-person-links a:hover { color: var(--global-theme-color, #b1241f); }
</style>
