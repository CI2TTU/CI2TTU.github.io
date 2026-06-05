---
layout: page
permalink: /
title: Home
nav: false
---

<div class="ci2-home">
  <section class="ci2-hero">
    <p class="ci2-eyebrow">Texas Tech University · Department of Computer Science</p>
    <h1 class="ci2-title">Computational Intelligence,<br>Control &amp; Information Lab</h1>
    <p class="ci2-lede">
      We study how intelligent agents learn to perceive, predict, and control complex
      dynamical systems — at the intersection of <strong>deep learning</strong>,
      <strong>reinforcement learning</strong>, <strong>optimal control</strong>, and
      <strong>information theory</strong>.
    </p>
  </section>

  <figure class="ci2-home-photo">
    {% include figure.liquid path="assets/img/gallery/group.jpg" class="ci2-home-img" sizes="(max-width: 575px) 95vw, 54rem" %}
  </figure>
</div>

<style>
  /* Home is a custom hero — hide the default page title/description header */
  .post > .post-header { display: none; }

  .ci2-home { max-width: 54rem; margin: 0 auto; }

  .ci2-hero { text-align: center; padding: 4rem 0 3rem; }
  .ci2-eyebrow {
    text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.9rem;
    font-weight: 600; opacity: 0.7; margin-bottom: 1rem;
  }
  .ci2-title {
    font-family: "Roboto Slab", serif; font-weight: 700;
    font-size: clamp(1.7rem, 5vw, 3.4rem); line-height: 1.15; margin: 0 0 1.5rem;
    text-wrap: balance;
  }
  .ci2-lede {
    font-size: 1.4rem; line-height: 1.7; max-width: 46rem;
    margin: 0 auto; opacity: 0.9;
  }
  @media (max-width: 575px) {
    .ci2-hero { padding: 2.5rem 0 2rem; }
    .ci2-lede { font-size: 1.2rem; }
  }

  .ci2-home-photo { margin: 0 auto; max-width: 54rem; }
  .ci2-home-photo .ci2-home-img,
  .ci2-home-photo img {
    width: 100%; height: auto; display: block;
    border-radius: 0.8rem;
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.14);
  }
</style>
