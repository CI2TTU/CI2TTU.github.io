---
layout: page
permalink: /publications/
title: Publications
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

  /* Every publication entry is a card: a bordered, lightly-tinted block with a red
     left accent, so the page reads as a consistent list of cards. */
  .publications ol.bibliography > li {
    padding: 1.15rem 1.35rem; margin-bottom: 1.1rem;
    border: 1px solid var(--global-divider-color, #e6e6e6);
    border-left: 4px solid var(--global-theme-color, #cc0000);
    border-radius: 0.6rem;
    background: rgba(204, 0, 0, 0.025);
  }
  .publications ol.bibliography > li > .row { margin: 0; }

  /* Two fixed-role columns on every entry: a 9.5rem badge/links column and the
     bibliographic info beside it. flex-basis 0 (not width:100%) so the info column
     never wraps under the badge, with or without a video on the right. */
  @media (min-width: 576px) {
    .publications ol.bibliography > li > .row { flex-wrap: nowrap; align-items: flex-start; }
    .publications ol.bibliography .abbr { flex: 0 0 9.5rem; max-width: 9.5rem; }
    .publications ol.bibliography .col-sm-8 {
      flex: 1 1 0; width: auto; max-width: none; min-width: 0; padding-left: 1.35rem;
    }
  }

  /* Bibliographic typography: clear hierarchy — title, then authors, then venue+year */
  .publications ol.bibliography .title {
    font-family: "Roboto Slab", serif; font-weight: 600; font-size: 1.08rem;
    line-height: 1.4; margin-bottom: 0.25rem;
  }
  .publications ol.bibliography .author { font-size: 0.97rem; line-height: 1.55; }
  .publications ol.bibliography .periodical {
    font-size: 0.93rem; line-height: 1.5; opacity: 0.85; margin-top: 0.15rem;
  }

  /* Links relocated under the venue badge: space them out and let them wrap */
  .publications ol.bibliography .abbr .links { margin-top: 0.6rem; display: flex; flex-wrap: wrap; gap: 0.4rem; }
  .publications ol.bibliography .abbr .links a.btn { margin: 0; }

  /* Accolade/highlight note (e.g. spotlight selections) — quiet red emphasis */
  .publications ol.bibliography .ci2-pub-note {
    font-size: 0.88rem; line-height: 1.45; margin-top: 0.3rem;
    color: var(--global-theme-color, #b1241f);
  }

  /* Make the venue badge a clean, readable pill — a touch taller and roomier.
     (No Bootstrap w-100 on the element: width is set here per breakpoint so the
     Tailwind layer's !important can't fight us.) */
  .publications .abbr abbr {
    padding: 0.3rem 0.45rem;
    border-radius: 0.4rem;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0;
    line-height: 1.25;
    text-align: center;
  }
  @media (min-width: 576px) {
    /* Fill the fixed 9.5rem column so every badge is exactly the same width */
    .publications .abbr abbr { width: 100%; }
  }

  /* Phones: columns stack — keep the badge an inline pill beside its links,
     not a full-width red bar */
  @media (max-width: 575px) {
    .publications ol.bibliography .abbr {
      display: flex; align-items: center; flex-wrap: wrap; gap: 0.45rem;
      margin-bottom: 0.55rem;
    }
    .publications .abbr abbr { width: auto; padding: 0.3rem 0.7rem; }
    .publications ol.bibliography .abbr .links { margin-top: 0; }
  }

  /* Papers with demo videos keep the same card, and lay the video(s) out on the
     right of the bibliographic info. Video on the right; solo larger, pair side-by-side.
     Top-aligned so the text sits consistently with video-less cards. */
  .publications ol.bibliography > li:has(.ci2-pub-media) {
    display: flex; align-items: flex-start; gap: 1.25rem;
  }
  .publications ol.bibliography > li:has(.ci2-pub-media) > .row { flex: 1 1 auto; min-width: 0; }
  .publications ol.bibliography > li:has(.ci2-pub-media) > .ci2-pub-media { flex: 0 0 auto; margin: 0; }

  .ci2-pub-media { display: flex; flex-wrap: nowrap; gap: 0.5rem; }
  .ci2-pub-media--pair { flex-direction: column; }  /* multiple videos stack vertically */
  .ci2-pub-media .ci2-pub-video {
    width: 18rem; height: auto; display: block; background: #000;
    border-radius: 0.5rem; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
  }

  /* Phones: drop the video(s) below the bib info, still inside the card, full width */
  @media (max-width: 767px) {
    .publications ol.bibliography > li:has(.ci2-pub-media) {
      flex-direction: column; align-items: stretch; gap: 0.85rem;
    }
    .ci2-pub-media .ci2-pub-video { width: 100%; max-width: 32rem; }
  }
</style>
