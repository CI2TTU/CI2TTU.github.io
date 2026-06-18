---
layout: page
title: Research
permalink: /research/
nav: true
nav_order: 2
---

<section class="ci2-rhero" aria-label="">
  <div class="ci2-rhero__inner">
    <p class="ci2-rhero__quote">&ldquo;A mathematician is a device for turning coffee into theorems.&rdquo;</p>
    <p class="ci2-rhero__cap">&mdash; Alfréd Rényi</p>
  </div>
</section>

<div class="ci2-research">

<p class="ci2-research-intro">
We build agents that learn to perceive, act, and acquire skills in complex physical systems —
uniting reinforcement learning, control and dynamical-systems theory, and information theory,
with <strong>intrinsic motivation</strong> as a recurring thread.
</p>

<section class="ci2-research-area">
  <h2>Intrinsic Motivation &amp; Empowerment</h2>
  <p>
  Information-theoretic objectives — empowerment, channel capacity, and the value of information —
  that drive agents to discover useful, generalizable behavior without hand-engineered rewards,
  including intrinsic motivation realized through deep reinforcement learning.
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
  /* Coffee hero with the "coffee → theorems" epigraph */
  .ci2-rhero {
    width: 100vw; position: relative; left: 50%; margin-left: -50vw; margin-top: 0.5rem;
    min-height: clamp(280px, 37vh, 410px);
    display: flex; align-items: flex-end; justify-content: flex-end;
    background-image: url('{{ '/assets/img/hero-coffee.jpg' | relative_url }}');
    background-size: cover; background-position: center 42%;
  }
  .ci2-rhero::before {
    content: ""; position: absolute; inset: 0;
    background: linear-gradient(180deg, rgba(0,0,0,0.40) 0%, rgba(0,0,0,0.52) 100%);
  }
  .ci2-rhero__inner { position: relative; z-index: 1; text-align: right; padding: 1.4rem 2.25rem 1.5rem; max-width: 52rem; }
  .ci2-rhero__quote {
    font-family: "Roboto Slab", serif; font-style: italic; font-weight: 600; color: #fff; margin: 0;
    font-size: clamp(1rem, 1.7vw, 1.5rem); line-height: 1.45; text-wrap: balance;
    text-shadow: 0 2px 16px rgba(0,0,0,0.55);
  }
  .ci2-rhero__cap { color: #fff; opacity: 0.9; margin: 0.8rem 0 0; font-size: 1rem; letter-spacing: 0.02em; }

  .ci2-research { max-width: 48rem; margin: 2.5rem auto 0; }
  .ci2-research-intro { font-size: 1.12rem; line-height: 1.7; opacity: 0.9; margin-bottom: 2.25rem; }

  .ci2-research-area { margin-bottom: 2.25rem; }
  .ci2-research-area h2 {
    font-family: "Roboto Slab", serif; font-weight: 700; font-size: 1.5rem; margin: 0 0 0.6rem;
    padding-left: 0.9rem; border-left: 3px solid var(--global-theme-color, #b1241f);
  }
  .ci2-research-area p { font-size: 1.02rem; line-height: 1.75; margin: 0; opacity: 0.92; }
</style>
