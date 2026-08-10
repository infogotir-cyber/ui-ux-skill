(function () {
  'use strict';

  // Reveal-on-scroll
  var revealables = document.querySelectorAll('.reveal, .stagger');
  if ('IntersectionObserver' in window && revealables.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add('in-view'); });
  }

  // Animated counters: <span data-counter="1234" data-suffix="+">
  var counters = document.querySelectorAll('[data-counter]');
  if (counters.length) {
    var countIo = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          countIo.unobserve(el);
          var target = parseFloat(el.getAttribute('data-counter'));
          var suffix = el.getAttribute('data-suffix') || '';
          var decimals = el.getAttribute('data-decimals') ? parseInt(el.getAttribute('data-decimals'), 10) : 0;
          var duration = 1200;
          var start = null;
          function step(ts) {
            if (!start) start = ts;
            var progress = Math.min((ts - start) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3);
            var value = target * eased;
            el.textContent = value.toFixed(decimals).replace(/\B(?=(\d{3})+(?!\d))/g, ',') + suffix;
            if (progress < 1) requestAnimationFrame(step);
          }
          requestAnimationFrame(step);
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach(function (el) { countIo.observe(el); });
  }

  // Copy-to-clipboard: <button data-copy="text to copy">
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-copy]');
    if (!btn) return;
    var text = btn.getAttribute('data-copy');
    var doCopy = function () {
      var original = btn.getAttribute('data-copy-label') || btn.innerHTML;
      btn.classList.add('copied');
      var label = btn.querySelector('.copy-label');
      if (label) {
        var prev = label.textContent;
        label.textContent = 'Copied!';
        setTimeout(function () { label.textContent = prev; btn.classList.remove('copied'); }, 1400);
      } else {
        setTimeout(function () { btn.classList.remove('copied'); }, 1400);
      }
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(doCopy).catch(doCopy);
    } else {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); } catch (err) {}
      document.body.removeChild(ta);
      doCopy();
    }
  });

  // Toast helper
  window.snToast = function (message, opts) {
    opts = opts || {};
    var root = document.getElementById('toast-root');
    if (!root) {
      root = document.createElement('div');
      root.id = 'toast-root';
      root.style.cssText = 'position:fixed;bottom:20px;right:20px;z-index:1080;display:flex;flex-direction:column;gap:8px;';
      document.body.appendChild(root);
    }
    var el = document.createElement('div');
    el.className = 'toast show';
    el.style.cssText = 'min-width:280px;animation:sn-toast-in .3s cubic-bezier(.16,1,.3,1) both;';
    el.innerHTML =
      '<div class="toast-header">' +
      '<span class="status-dot ' + (opts.color ? 'bg-' + opts.color : 'bg-azure') + ' status-dot-animated me-2"></span>' +
      '<strong class="me-auto">' + (opts.title || 'Automation OS') + '</strong>' +
      '<button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>' +
      '</div>' +
      '<div class="toast-body">' + message + '</div>';
    root.appendChild(el);
    var closeBtn = el.querySelector('.btn-close');
    var remove = function () {
      el.style.transition = 'opacity .25s, transform .25s';
      el.style.opacity = '0';
      el.style.transform = 'translateY(6px)';
      setTimeout(function () { el.remove(); }, 250);
    };
    closeBtn.addEventListener('click', remove);
    setTimeout(remove, opts.duration || 3200);
  };

  var styleTag = document.createElement('style');
  styleTag.textContent = '@keyframes sn-toast-in{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}';
  document.head.appendChild(styleTag);
})();
