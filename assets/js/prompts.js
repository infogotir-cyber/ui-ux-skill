(function () {
  'use strict';
  var search = document.getElementById('prompt-search');
  var cards = document.querySelectorAll('.prompt-card');
  var emptyEl = document.getElementById('prompt-empty');
  var activeCat = '';

  var favKey = 'sn_prompt_favorites';
  var favs = {};
  try { favs = JSON.parse(localStorage.getItem(favKey) || '{}'); } catch (e) { favs = {}; }

  cards.forEach(function (card) {
    var id = card.querySelector('.fav-btn').dataset.favId;
    if (favs.hasOwnProperty(id)) {
      card.dataset.favorite = favs[id] ? 'true' : 'false';
      setFavIcon(card.querySelector('.fav-btn'), favs[id]);
    }
  });

  function setFavIcon(btn, active) {
    var icon = btn.querySelector('.fav-icon');
    icon.classList.toggle('icon-filled', active);
    icon.classList.toggle('text-yellow', active);
  }

  document.querySelectorAll('.fav-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var card = btn.closest('.prompt-card');
      var id = btn.dataset.favId;
      var newVal = card.dataset.favorite !== 'true';
      card.dataset.favorite = newVal ? 'true' : 'false';
      favs[id] = newVal;
      localStorage.setItem(favKey, JSON.stringify(favs));
      setFavIcon(btn, newVal);
      if (activeCat === '__favorites') applyFilters();
    });
  });

  function applyFilters() {
    var q = (search.value || '').toLowerCase().trim();
    var visible = 0;
    cards.forEach(function (card) {
      var matchesText = !q || card.dataset.title.indexOf(q) !== -1;
      var matchesCat = !activeCat || (activeCat === '__favorites' ? card.dataset.favorite === 'true' : card.dataset.category === activeCat);
      var show = matchesText && matchesCat;
      card.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    emptyEl.classList.toggle('d-none', visible !== 0);
  }

  search.addEventListener('input', applyFilters);
  document.querySelectorAll('[data-cat-filter]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('[data-cat-filter]').forEach(function (b) { b.className = 'btn btn-sm btn-outline-light'; });
      btn.className = 'btn btn-sm btn-indigo';
      activeCat = btn.dataset.catFilter;
      applyFilters();
    });
  });
})();
