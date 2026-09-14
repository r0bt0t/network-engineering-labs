/*
 * Rob Totton — Network Engineering Portfolio
 * Landing animation and light interaction layer.
 */

(() => {
  const root = document.documentElement;
  root.classList.add('js');

  const startLandingAnimation = () => {
    const landing = document.querySelector('.landing-page');
    if (!landing) return;

    // One frame ensures the initial CSS state is painted first.
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        landing.classList.add('is-ready');
      });
    });
  };

  const addSoftParallax = () => {
    const image = document.querySelector('.background-switch');
    const landing = document.querySelector('.landing-page');

    if (!image || !landing) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (window.matchMedia('(pointer: coarse)').matches) return;

    let frame = null;

    const update = (event) => {
      if (frame) cancelAnimationFrame(frame);

      frame = requestAnimationFrame(() => {
        const bounds = landing.getBoundingClientRect();
        const x = (event.clientX - bounds.left) / bounds.width - 0.5;
        const y = (event.clientY - bounds.top) / bounds.height - 0.5;

        image.style.setProperty('--parallax-x', `${x * -5}px`);
        image.style.setProperty('--parallax-y', `${y * -3}px`);
      });
    };

    landing.addEventListener('pointermove', update, { passive: true });

    landing.addEventListener('pointerleave', () => {
      image.style.removeProperty('--parallax-x');
      image.style.removeProperty('--parallax-y');
    });
  };

  const markActiveNavigation = () => {
    const current = window.location.pathname.replace(/\/$/, '');

    document.querySelectorAll('.site-nav a, .main-nav a').forEach((link) => {
      const href = new URL(link.href, window.location.href).pathname.replace(/\/$/, '');

      if (href === current) {
        link.setAttribute('aria-current', 'page');
      }
    });
  };

  const initialise = () => {
    startLandingAnimation();
    addSoftParallax();
    markActiveNavigation();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialise, { once: true });
  } else {
    initialise();
  }
})();
