---
layout: page
permalink: /publications/
title: Publications
description: Preprints and selected publications from the CI² Lab.
nav: true
nav_order: 4
---

<div class="publications">

<h2 class="ci2-pub-heading">Preprints</h2>
{% bibliography --group_by none --query @*[preprint=true]* %}

<h2 class="ci2-pub-heading">Selected Publications</h2>
{% bibliography --group_by none --query @*[selected=true]* %}

</div>

<style>
  .ci2-pub-heading {
    font-family: "Roboto Slab", serif; font-weight: 700;
    margin: 2rem 0 1rem; padding-bottom: 0.35rem;
    border-bottom: 2px solid var(--global-theme-color, #b1241f);
  }
  .ci2-pub-heading:first-child { margin-top: 0.5rem; }

  /* Clearly separate each publication entry */
  .publications ol.bibliography > li {
    padding-bottom: 1.1rem;
    margin-bottom: 1.1rem;
    border-bottom: 1px solid var(--global-divider-color, #e6e6e6);
  }
  .publications ol.bibliography > li:last-child { border-bottom: none; }

  /* Wider venue-badge column so long venue names fit (we have the horizontal room) */
  @media (min-width: 576px) {
    .publications ol.bibliography .abbr { flex: 0 0 24%; max-width: 24%; }
    .publications ol.bibliography .col-sm-8 { flex: 0 0 76%; max-width: 76%; }
  }

  /* Links relocated under the venue badge: space them out and let them wrap */
  .publications ol.bibliography .abbr .links { margin-top: 0.6rem; display: flex; flex-wrap: wrap; gap: 0.4rem; }
  .publications ol.bibliography .abbr .links a.btn { margin: 0; }

  /* Make the venue badge a clean, readable pill — a touch taller and roomier */
  .publications .abbr abbr {
    padding: 0.3rem 0.6rem;
    border-radius: 0.4rem;
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.01em;
    line-height: 1.25;
  }
</style>
