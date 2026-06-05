---
layout: page
title: Research
permalink: /research/
nav: true
nav_order: 2
description: Research in the Computational Intelligence, Control &amp; Information (CI²) Lab.
---

<div class="ci2-research">

<p class="ci2-research-intro">
The CI² Lab develops principled, learning-based methods for perceiving and controlling
complex dynamical systems. Our work draws on deep learning, reinforcement learning,
optimal control, and information theory, combining theory with large-scale experimentation.
</p>

<section class="ci2-research-area">
  <h2>Deep Learning for Control</h2>
  <p>
  A central theme of the lab is learning to control dynamical systems directly from data.
  We develop deep model-based and model-free reinforcement learning methods that learn
  predictive models of an environment and use them to plan and act — with an emphasis on
  sample efficiency, stability, and transfer to real physical systems.
  </p>
</section>

<section class="ci2-research-area">
  <h2>Information Theory of Perception &amp; Control</h2>
  <p>
  We study the information-theoretic principles that govern how an agent should perceive its
  environment and choose actions. This includes intrinsic motivation, empowerment, and the
  fundamental trade-offs between information acquisition and control performance.
  </p>
</section>

<section class="ci2-research-area">
  <h2>Representation Learning for Dynamical Systems</h2>
  <p>
  How should an agent represent a high-dimensional, partially observed world so that it can
  predict and act effectively? We develop representation-learning methods that capture the
  underlying structure of dynamical systems, supporting downstream prediction, planning, and control.
  </p>
</section>

<p class="ci2-research-footnote">
Interested in working on these problems? See the <a href="{{ '/people/' | relative_url }}">people</a>
page and our <a href="{{ '/publications/' | relative_url }}">publications</a>, or
<a href="mailto:stas.tiomkin@ttu.edu">get in touch</a>.
</p>

</div>

<style>
  .ci2-research { max-width: 48rem; margin: 0 auto; }
  .ci2-research-intro { font-size: 1.12rem; line-height: 1.7; opacity: 0.9; margin-bottom: 2.25rem; }

  .ci2-research-area { margin-bottom: 2.25rem; }
  .ci2-research-area h2 {
    font-family: "Roboto Slab", serif; font-weight: 700; font-size: 1.5rem; margin: 0 0 0.6rem;
    padding-left: 0.9rem; border-left: 3px solid var(--global-theme-color, #b1241f);
  }
  .ci2-research-area p { font-size: 1.02rem; line-height: 1.75; margin: 0; opacity: 0.92; }

  .ci2-research-footnote {
    margin-top: 2.5rem; padding-top: 1.25rem; font-size: 0.98rem; opacity: 0.85;
    border-top: 1px solid var(--global-divider-color, #e0e0e0);
  }
</style>
