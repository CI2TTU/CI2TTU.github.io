---
layout: page
title: Research
permalink: /research/
nav: true
nav_order: 2
---

<div class="ci2-research-epi">
  <img class="ci2-research-epi__img" src="{{ '/assets/img/hero-coffee.jpg' | relative_url }}" alt="">
  <div class="ci2-research-epi__text">
    <p class="ci2-research-epi__q">&ldquo;A mathematician is a device for turning coffee into theorems.&rdquo;</p>
    <p class="ci2-research-epi__a">&mdash; Alfréd Rényi</p>
  </div>
</div>

<h1 class="post-title ci2-research-title">Research</h1>

<div class="ci2-research">

<p class="ci2-research-intro">
We build agents that learn to perceive, act, and acquire skills in complex physical systems —
uniting reinforcement learning, control and dynamical-systems theory, and information theory,
with <strong>intrinsic motivation</strong> as a recurring thread.
</p>

<section class="ci2-research-area">
  <h2>Intrinsic Motivation &amp; Empowerment</h2>
  <p>
  Information-theoretic objectives — empowerment, curiosity, information production — that drive
  agents to discover useful, generalizable behavior without human-engineered rewards. We explore
  these objectives using both classical control methods and modern learning-based algorithms.
  </p>
</section>

<section class="ci2-research-area">
  <h2>Information-Theoretic Perception &amp; Control</h2>
  <p>
  The fundamental limits of perceiving and controlling dynamical systems: how much information an
  agent must acquire and retain in order to act, studied through information-bottleneck and
  channel-capacity analyses of closed-loop feedback.
  </p>
</section>

<section class="ci2-research-area">
  <h2>Robot Learning &amp; Skill Acquisition</h2>
  <p>
  Learning controllable skills on real physical systems — manipulation, locomotion, and sparse
  robotic actuation — with an emphasis on sample efficiency, stability (Lyapunov-guided learning),
  and transfer from simulation to hardware.
  </p>
</section>

<section class="ci2-research-area">
  <h2>Learning in Contact-Rich Environments</h2>
  <p>
  Acting through frequent physical contact — dexterous manipulation, locomotion, and assembly —
  where intermittent contacts induce hybrid, non-smooth dynamics that challenge standard control
  and learning, and demand methods that reason about when and how to make contact.
  </p>
</section>

<section class="ci2-research-area">
  <h2>Behavior Synthesis for Dynamical Systems</h2>
  <p>
  Synthesizing complex, structured behavior for nonlinear and hybrid dynamical systems by learning
  predictive, control-aware representations of dynamics that support planning and design.
  </p>
</section>

<section class="ci2-research-area">
  <h2>Emergence &amp; Multi-Agent Intelligence</h2>
  <p>
  How coordinated, complex collective behavior emerges in groups of agents from intrinsic
  objectives, rather than from centralized control or explicit reward design.
  </p>
</section>

<section class="ci2-research-area">
  <h2>Foundations of Reinforcement Learning</h2>
  <p>
  The theory behind the applications above: entropy-regularized and average-reward RL, reward
  shaping and compositionality, and bounds on optimal value functions.
  </p>
</section>

</div>

<style>
  /* Our own centered title (hide al-folio's default left-aligned one) */
  .post > .post-header { display: none; }
  /* match the default page-title styling used on the other tabs (People, etc.) */
  .ci2-research-title { margin-bottom: 1.5rem; }

  /* Epigraph: round coffee inset to the LEFT of a single-line quote, above the title */
  .ci2-research-epi {
    display: flex; align-items: center; justify-content: flex-start; gap: 1.4rem;
    margin: 0.75rem 0 1.6rem;
  }
  .ci2-research-epi__img {
    width: 200px; height: 200px; border-radius: 50%; object-fit: cover; object-position: center 40%;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2); flex: none;
  }
  .ci2-research-epi__text { text-align: left; }
  .ci2-research-epi__q {
    font-family: "Roboto Slab", serif; font-style: italic; font-weight: 500;
    font-size: clamp(0.9rem, 1.75vw, 1.25rem); line-height: 1.4; margin: 0;
    white-space: nowrap; color: var(--global-text-color);
  }
  .ci2-research-epi__a {
    font-size: 0.83rem; opacity: 0.58; margin: 0.35rem 0 0; letter-spacing: 0.04em; text-transform: uppercase;
  }
  /* On phones the line is too long — stack the circle above and let the quote wrap */
  @media (max-width: 720px) {
    .ci2-research-epi { flex-direction: column; gap: 1rem; }
    .ci2-research-epi__text { text-align: center; }
    .ci2-research-epi__q { white-space: normal; }
  }

  .ci2-research { max-width: 48rem; margin: 0 auto; }
  .ci2-research-intro { font-size: 1.12rem; line-height: 1.7; opacity: 0.9; margin-bottom: 2.25rem; }
  .ci2-research-area { margin-bottom: 2.25rem; }
  .ci2-research-area h2 {
    font-family: "Roboto Slab", serif; font-weight: 700; font-size: 1.5rem; margin: 0 0 0.6rem;
    padding-left: 0.9rem; border-left: 3px solid var(--global-theme-color, #b1241f);
  }
  .ci2-research-area p { font-size: 1.02rem; line-height: 1.75; margin: 0; opacity: 0.92; }
</style>
