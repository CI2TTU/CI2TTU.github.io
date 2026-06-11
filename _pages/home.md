---
layout: page
permalink: /
title: Home
nav: false
---

<div class="ci2-home">
  <p class="ci2-eyebrow">Texas Tech University · Department of Computer Science</p>
  <div class="ci2-wordmark" aria-hidden="true">CI<sup>2</sup> Lab</div>
  <h1 class="ci2-fullname">Computational Intelligence, Control &amp; Information Lab</h1>
  <p class="ci2-lede">
    We study how intelligent agents learn to perceive, predict, and control complex
    dynamical systems — at the intersection of <strong>deep learning</strong>,
    <strong>reinforcement learning</strong>, <strong>optimal control</strong>, and
    <strong>information theory</strong>.
  </p>
</div>

<style>
  /* Home: a typographic "CI² Lab" wordmark (the old logo image is kept in the repo
     but no longer displayed), with the full lab name and intro beneath it. */
  .post > .post-header { display: none; }

  .ci2-home { text-align: center; max-width: 60rem; margin: 2.5rem auto 0; }

  .ci2-eyebrow {
    text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.9rem;
    font-weight: 600; opacity: 0.8; margin-bottom: 1.25rem; color: var(--global-text-color);
  }

  .ci2-wordmark {
    font-family: "Roboto Slab", serif; font-weight: 800;
    font-size: clamp(4rem, 15vw, 10.5rem); line-height: 1; letter-spacing: 0.005em;
    margin: 0 0 0.7rem; color: #990000;
  }
  html[data-theme="dark"] .ci2-wordmark { color: #e8473c; }
  .ci2-wordmark sup {
    font-size: 0.5em; top: -0.9em; margin-left: 0.02em;
  }

  .ci2-fullname {
    font-family: "Roboto Slab", serif; font-weight: 600;
    font-size: clamp(1.2rem, 3vw, 2rem); line-height: 1.25; margin: 0 0 1.5rem;
    color: var(--global-text-color); text-wrap: balance; opacity: 0.92;
  }

  .ci2-lede {
    font-size: 1.25rem; line-height: 1.65; max-width: 42rem; margin: 0 auto;
    color: var(--global-text-color);
  }

  @media (max-width: 575px) {
    .ci2-eyebrow { font-size: 0.72rem; letter-spacing: 0.08em; }
    .ci2-fullname { font-size: 1.1rem; }
    .ci2-lede { font-size: 1.05rem; }
  }
</style>
