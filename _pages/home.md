---
layout: page
permalink: /
title: Home
nav: false
---

<div class="ci2-stage">
  <div class="ci2-stage-inner">
    <p class="ci2-eyebrow">Texas Tech University · Department of Computer Science</p>
    <h1 class="ci2-title">Computational Intelligence,<br>Control &amp; Information Lab</h1>
    <p class="ci2-lede">
      We study how intelligent agents learn to perceive, predict, and control complex
      dynamical systems — at the intersection of <strong>deep learning</strong>,
      <strong>reinforcement learning</strong>, <strong>optimal control</strong>, and
      <strong>information theory</strong>.
    </p>
  </div>
</div>

<style>
  /* Full-bleed hero. The image is TRANSPARENT (red nebula + CI² + robot), so the
     page background shows through: white in light mode, dark in dark mode. */
  .post > .post-header { display: none; }
  .post, .post > article { overflow: visible; }

  .ci2-stage {
    width: 100vw;
    margin-left: calc(50% - 50vw);
    margin-right: calc(50% - 50vw);
    margin-top: -2.5rem;
    background: transparent url("{{ '/assets/img/hero-home.webp' | relative_url }}") center center / cover no-repeat;
    min-height: 88vh;
    display: flex; flex-direction: column; align-items: center; justify-content: flex-start;
    padding: 3.5rem 1.25rem 4rem;
  }
  .ci2-stage-inner { max-width: 50rem; margin: 0 auto; text-align: center; }

  /* Theme-adaptive text colour (dark on white, light on dark) */
  .ci2-eyebrow {
    text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.92rem;
    font-weight: 600; opacity: 0.85; margin-bottom: 1rem;
    color: var(--global-text-color);
  }
  .ci2-title {
    font-family: "Roboto Slab", serif; font-weight: 700;
    font-size: clamp(1.8rem, 5vw, 3.3rem); line-height: 1.15; margin: 0 0 1.25rem;
    color: var(--global-text-color); text-wrap: balance;
  }
  .ci2-lede {
    font-size: 1.32rem; line-height: 1.7; max-width: 42rem; margin: 0 auto;
    color: var(--global-text-color);
  }

  @media (max-width: 575px) {
    .ci2-stage { padding: 2.5rem 1rem 3rem; min-height: 82vh; }
    .ci2-lede { font-size: 1.15rem; }
  }
</style>
