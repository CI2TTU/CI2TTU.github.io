---
layout: page
permalink: /
title: Home
nav: false
---

<div class="ci2-home">
  <p class="ci2-eyebrow">Led by Dr. Stas Tiomkin</p>
  <h1 class="ci2-fullname">Computational Intelligence, Control &amp; Information Lab</h1>
  <p class="ci2-tagline">AI grounded in Engineering</p>
  <p class="ci2-lede">
    We build agents that learn to perceive, act, and acquire skills in complex physical
    systems — uniting <strong>reinforcement learning</strong>, <strong>control and
    dynamical-systems theory</strong>, and <strong>information theory</strong>, with
    <strong>intrinsic motivation</strong> as a recurring thread.
  </p>
</div>

<section class="ci2-featured" aria-label="Featured work">
  <h2 class="ci2-section-heading">Featured work</h2>
  <div class="ci2-featured-grid">
    <a class="ci2-featured-card" href="{{ '/publications/#tiomkin2026information' | relative_url }}">
      <span class="ci2-featured-media">
        <video class="ci2-featured-video" muted loop playsinline preload="none"
               poster="{{ '/assets/video/saltation_3x3_grid.jpg' | relative_url }}">
          <source src="{{ '/assets/video/saltation_3x3_grid.mp4' | relative_url }}" type="video/mp4">
        </video>
      </span>
      <span class="ci2-featured-title">Information-Theoretic Approach for Locomotion</span>
    </a>
    <a class="ci2-featured-card" href="{{ '/publications/#shah2026multiagent' | relative_url }}">
      <span class="ci2-featured-media">
        <video class="ci2-featured-video" muted loop playsinline preload="none"
               poster="{{ '/assets/video/flock_6.jpg' | relative_url }}">
          <source src="{{ '/assets/video/flock_6.mp4' | relative_url }}" type="video/mp4">
        </video>
      </span>
      <span class="ci2-featured-title">Multi-Agent Empowerment &amp; Emergence of Complex Behavior</span>
    </a>
    <a class="ci2-featured-card" href="{{ '/publications/#shah2026controllable' | relative_url }}">
      <span class="ci2-featured-media ci2-featured-media--stack">
        <video class="ci2-featured-video ci2-featured-video--wide" muted loop playsinline preload="none"
               poster="{{ '/assets/video/gibbon.jpg' | relative_url }}">
          <source src="{{ '/assets/video/gibbon.mp4' | relative_url }}" type="video/mp4">
        </video>
        <video class="ci2-featured-video ci2-featured-video--wide" muted loop playsinline preload="none"
               poster="{{ '/assets/video/triple_pendulum.jpg' | relative_url }}">
          <source src="{{ '/assets/video/triple_pendulum.mp4' | relative_url }}" type="video/mp4">
        </video>
      </span>
      <span class="ci2-featured-title">Emergence of Physical Intelligence via Controllable Information Production</span>
    </a>
  </div>
  <p class="ci2-featured-more">
    <a href="{{ '/publications/' | relative_url }}">See all publications &rarr;</a>
  </p>
</section>

<section class="ci2-support" aria-label="Support">
  <h2 class="ci2-section-heading">Support</h2>
  <p class="ci2-support-note">Our research is supported by</p>
  <div class="ci2-support-logos">
    <a class="ci2-support-item" href="https://www.nsf.gov/" target="_blank" rel="noopener"
       aria-label="National Science Foundation">
      <img class="ci2-logo-nsf" src="{{ '/assets/img/nsf-logo.png' | relative_url }}"
           alt="National Science Foundation" loading="lazy" />
    </a>
    <a class="ci2-support-item" href="https://www.pazyfoundation.org.il/" target="_blank" rel="noopener"
       aria-label="The Pazy Foundation">
      <img class="ci2-logo-pazy" src="{{ '/assets/img/pazy-logo.png' | relative_url }}"
           alt="The Pazy Foundation — Excelling in Science" loading="lazy" />
    </a>
    <a class="ci2-support-item" href="https://alliancernm.com" target="_blank" rel="noopener"
       aria-label="Alliance Innovation Lab — Silicon Valley">
      <img class="ci2-logo-ail" src="{{ '/assets/img/nissan-logo.png' | relative_url }}"
           alt="Alliance Innovation Lab — Silicon Valley (Renault–Nissan–Mitsubishi)" loading="lazy" />
    </a>
  </div>
</section>

<style>
  /* Home: a typographic "CI² Lab" wordmark (the old logo image is kept in the repo
     but no longer displayed), with the full lab name, tagline and intro beneath it. */
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
    font-size: clamp(1.2rem, 3vw, 2rem); line-height: 1.25; margin: 0 0 0.6rem;
    color: var(--global-text-color); text-wrap: balance; opacity: 0.92;
  }

  .ci2-tagline {
    font-family: "Roboto Slab", serif; font-weight: 600; font-style: italic;
    font-size: clamp(1.05rem, 2.4vw, 1.5rem); letter-spacing: 0.01em;
    margin: 0 0 1.5rem; color: #990000;
  }
  html[data-theme="dark"] .ci2-tagline { color: #e8473c; }

  .ci2-lede {
    font-size: 1.25rem; line-height: 1.65; max-width: 44rem; margin: 0 auto;
    color: var(--global-text-color);
  }

  /* Shared section heading for the Featured work and Support bands */
  .ci2-section-heading {
    font-family: "Roboto Slab", serif; font-weight: 700; text-align: center;
    font-size: 1.5rem; margin: 0 0 1.5rem; padding-bottom: 0.4rem;
  }

  /* Featured work — demo videos that link to their paper on /publications/ */
  .ci2-featured { max-width: 64rem; margin: 3.5rem auto 0; }
  .ci2-featured-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
    gap: 1.5rem; align-items: start;
  }
  .ci2-featured-card {
    display: flex; flex-direction: column; text-decoration: none;
    color: var(--global-text-color); transition: transform 0.15s ease;
  }
  .ci2-featured-card:hover { transform: translateY(-3px); text-decoration: none; }
  .ci2-featured-media {
    display: block; border-radius: 0.6rem; overflow: hidden; background: #000;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.18);
    border: 1px solid var(--global-divider-color, #e6e6e6);
  }
  .ci2-featured-video {
    display: block; width: 100%; aspect-ratio: 1 / 1; object-fit: cover;
    background: #000;
  }
  /* The "Controllable Information Production" paper has two landscape (≈3:2) clips.
     Stack them inside the same square footprint as the other cards and fit each by
     height (no cropping); the white side margins blend with the clips' white background. */
  .ci2-featured-media--stack {
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 2px; aspect-ratio: 1 / 1; background: #fff;
  }
  .ci2-featured-video--wide {
    aspect-ratio: auto; width: 100%; height: 100%; min-height: 0; flex: 1 1 0;
    object-fit: contain; background: #fff;
  }
  .ci2-featured-title {
    display: block; margin-top: 0.7rem; font-family: "Roboto Slab", serif;
    font-size: 0.98rem; font-weight: 600; line-height: 1.3; text-align: center;
  }
  .ci2-featured-card:hover .ci2-featured-title { color: var(--global-theme-color, #b1241f); }
  .ci2-featured-more { text-align: center; margin: 1.5rem 0 0; font-weight: 600; }

  /* Support — funding/sponsor logos */
  .ci2-support { max-width: 60rem; margin: 3.5rem auto 0; }
  .ci2-support-note {
    text-align: center; margin: -0.75rem 0 1.5rem; opacity: 0.75; font-size: 0.95rem;
  }
  .ci2-support-logos {
    display: flex; align-items: center; justify-content: center;
    gap: 3rem; flex-wrap: wrap;
  }
  .ci2-support-item {
    display: inline-flex; align-items: center; justify-content: center;
  }
  .ci2-support-logos img { width: auto; display: block; }
  .ci2-logo-nsf { height: 116px; }
  .ci2-logo-pazy { height: 108px; }
  .ci2-logo-ail { height: 80px; }
  /* In dark mode the full-color logos sit on a white chip so brand colors stay legible */
  html[data-theme="dark"] .ci2-support-logos img {
    background: #ffffff; padding: 0.4rem 0.6rem; border-radius: 0.5rem;
  }

  @media (max-width: 575px) {
    .ci2-eyebrow { font-size: 0.72rem; letter-spacing: 0.08em; }
    .ci2-fullname { font-size: 1.1rem; }
    .ci2-tagline { font-size: 1rem; }
    .ci2-lede { font-size: 1.05rem; }
    .ci2-support-logos { gap: 2rem; }
    .ci2-logo-nsf { height: 84px; }
    .ci2-logo-pazy { height: 78px; }
    .ci2-logo-ail { height: 58px; }
  }
</style>

<script>
  // Play the featured demo videos only while they're scrolled into view, so the
  // homepage doesn't eagerly download several MB of video on first paint.
  document.addEventListener("DOMContentLoaded", function () {
    var vids = document.querySelectorAll(".ci2-featured-video");
    if (!("IntersectionObserver" in window)) {
      vids.forEach(function (v) { v.play().catch(function () {}); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.play().catch(function () {}); }
        else { e.target.pause(); }
      });
    }, { threshold: 0.25 });
    vids.forEach(function (v) { io.observe(v); });
  });
</script>
