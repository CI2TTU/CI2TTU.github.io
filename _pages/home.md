---
layout: page
permalink: /
title: Home
nav: false
---

<div class="ci2-home">
  <p class="ci2-eyebrow">Texas Tech University · Department of Computer Science</p>
  <h1 class="ci2-title">Computational Intelligence,<br>Control &amp; Information Lab</h1>
  <p class="ci2-lede">
    We study how intelligent agents learn to perceive, predict, and control complex
    dynamical systems — at the intersection of <strong>deep learning</strong>,
    <strong>reinforcement learning</strong>, <strong>optimal control</strong>, and
    <strong>information theory</strong>.
  </p>
  <figure class="ci2-hero-fig">
    <img class="ci2-hero-img" src="{{ '/assets/img/hero-home.webp' | relative_url }}"
         alt="CI² — Computational Intelligence, Control &amp; Information Lab">
  </figure>
</div>

<style>
  /* Home: centered text with the logo below it. The logo is a real <img>, so it
     scales with the viewport and the surrounding whitespace shrinks with it. */
  .post > .post-header { display: none; }

  .ci2-home { text-align: center; max-width: 72rem; margin: 1rem auto 0; }

  .ci2-eyebrow {
    text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.9rem;
    font-weight: 600; opacity: 0.8; margin-bottom: 1rem; color: var(--global-text-color);
  }
  .ci2-title {
    font-family: "Roboto Slab", serif; font-weight: 700;
    font-size: clamp(1.6rem, 4.5vw, 3rem); line-height: 1.15; margin: 0 0 1.1rem;
    color: var(--global-text-color); text-wrap: balance;
  }
  .ci2-lede {
    font-size: 1.25rem; line-height: 1.65; max-width: 42rem; margin: 0 auto;
    color: var(--global-text-color);
  }

  .ci2-hero-fig { margin: 1.75rem 0 0; }
  .ci2-hero-img {
    display: block; margin: 0 auto;
    max-width: 100%; max-height: 60vh; width: auto; height: auto;
  }

  @media (max-width: 575px) {
    .ci2-eyebrow { font-size: 0.72rem; letter-spacing: 0.08em; }
    .ci2-title { font-size: 1.5rem; }
    .ci2-lede { font-size: 1.05rem; }
    .ci2-hero-fig { margin-top: 1.25rem; }
  }
</style>
