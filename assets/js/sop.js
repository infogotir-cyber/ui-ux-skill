(function () {
  'use strict';
  var search = document.getElementById('sop-search');
  var items = document.querySelectorAll('.sop-item');
  var countEl = document.getElementById('sop-count');
  var emptyEl = document.getElementById('sop-empty');
  var activeCategory = '';

  function applyFilters() {
    var q = (search.value || '').toLowerCase().trim();
    var visible = 0;
    items.forEach(function (el) {
      var matchesText = !q || el.dataset.title.indexOf(q) !== -1;
      var matchesCat = !activeCategory || el.dataset.category === activeCategory;
      var show = matchesText && matchesCat;
      el.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    countEl.textContent = visible + ' standard operating procedure' + (visible === 1 ? '' : 's');
    emptyEl.classList.toggle('d-none', visible !== 0);
  }

  search.addEventListener('input', applyFilters);

  document.querySelectorAll('[data-category-filter]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelectorAll('[data-category-filter]').forEach(function (l) { l.classList.remove('active'); });
      link.classList.add('active');
      activeCategory = link.dataset.categoryFilter;
      applyFilters();
    });
  });
})();
