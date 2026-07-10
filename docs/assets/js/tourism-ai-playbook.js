(() => {
  'use strict';

  const menuButton = document.querySelector('.ai-menu');
  const navigation = document.querySelector('#ai-nav');

  const closeMenu = () => {
    if (!menuButton || !navigation) return;
    navigation.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
  };

  if (menuButton && navigation) {
    menuButton.addEventListener('click', () => {
      const isOpen = navigation.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(isOpen));
    });

    navigation.addEventListener('click', (event) => {
      if (event.target.closest('a')) closeMenu();
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && navigation.classList.contains('open')) {
        closeMenu();
        menuButton.focus();
      }
    });
  }

  const fallbackCopy = (text) => {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.setAttribute('readonly', '');
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    const copied = document.execCommand('copy');
    textarea.remove();
    return copied;
  };

  document.querySelectorAll('[data-copy-target]').forEach((button) => {
    button.addEventListener('click', async () => {
      const prompt = document.getElementById(button.dataset.copyTarget);
      const status = document.getElementById(button.getAttribute('aria-describedby'));
      if (!prompt) return;

      let copied = false;
      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(prompt.textContent);
          copied = true;
        } else {
          copied = fallbackCopy(prompt.textContent);
        }
      } catch (error) {
        copied = fallbackCopy(prompt.textContent);
      }

      const originalLabel = button.textContent;
      button.textContent = copied ? 'Copied' : 'Select prompt';
      if (status) {
        status.textContent = copied
          ? 'Prompt copied. Replace the placeholders and verify every operational fact.'
          : 'Automatic copy was unavailable. Select the prompt text and copy it manually.';
      }

      window.setTimeout(() => {
        button.textContent = originalLabel;
      }, 2200);
    });
  });

  const progressBar = document.querySelector('.reading-progress');
  const updateReadingProgress = () => {
    if (!progressBar) return;
    const page = document.documentElement;
    const scrollableHeight = page.scrollHeight - page.clientHeight;
    const progress = scrollableHeight
      ? Math.min(100, (page.scrollTop / scrollableHeight) * 100)
      : 0;
    progressBar.style.width = `${progress}%`;
  };

  window.addEventListener('scroll', updateReadingProgress, { passive: true });
  updateReadingProgress();

  const tableOfContentsLinks = [
    ...document.querySelectorAll('.article-toc a[href^="#"]'),
  ];
  const tableOfContentsMap = new Map(
    tableOfContentsLinks.map((link) => [link.getAttribute('href').slice(1), link]),
  );
  const observedSections = [...tableOfContentsMap.keys()]
    .map((id) => document.getElementById(id))
    .filter(Boolean);

  if ('IntersectionObserver' in window && observedSections.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          tableOfContentsLinks.forEach((link) => link.classList.remove('current'));
          const currentLink = tableOfContentsMap.get(entry.target.id);
          if (currentLink) currentLink.classList.add('current');
        });
      },
      { rootMargin: '-18% 0px -72% 0px' },
    );

    observedSections.forEach((section) => observer.observe(section));
  }
})();
