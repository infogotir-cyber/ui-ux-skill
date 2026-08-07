(function () {
  'use strict';

  var fmt = function (n) { return '$' + Math.round(n).toLocaleString('en-US'); };

  // ---------------- Kanban drag & drop ----------------
  var dragged = null;
  document.addEventListener('dragstart', function (e) {
    var card = e.target.closest('.kanban-card');
    if (!card) return;
    dragged = card;
    card.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
    try { e.dataTransfer.setData('text/plain', card.dataset.leadId || ''); } catch (err) {}
  });
  document.addEventListener('dragend', function (e) {
    var card = e.target.closest('.kanban-card');
    if (card) card.classList.remove('dragging');
    document.querySelectorAll('.kanban-col-body.drop-hover').forEach(function (el) { el.classList.remove('drop-hover'); });
  });
  document.querySelectorAll('.kanban-col-body').forEach(function (col) {
    col.addEventListener('dragover', function (e) {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
      col.classList.add('drop-hover');
    });
    col.addEventListener('dragleave', function () { col.classList.remove('drop-hover'); });
    col.addEventListener('drop', function (e) {
      e.preventDefault();
      col.classList.remove('drop-hover');
      if (!dragged) return;
      var fromCol = dragged.closest('.kanban-col-body');
      col.appendChild(dragged);
      updateColumnStats(fromCol);
      updateColumnStats(col);
      var stageLabel = col.closest('.kanban-col').querySelector('.fw-medium.small').textContent;
      if (window.snToast) window.snToast('Moved <strong>' + dragged.querySelector('.fw-medium.small, .fw-medium').textContent + '</strong> to <strong>' + stageLabel + '</strong>', { color: 'indigo', title: 'Pipeline updated' });
      dragged = null;
    });
  });
  function updateColumnStats(colBody) {
    if (!colBody) return;
    var cards = colBody.querySelectorAll('.kanban-card');
    var total = 0;
    cards.forEach(function (c) { total += parseFloat(c.dataset.value || '0'); });
    var wrap = colBody.closest('.kanban-col');
    var countEl = wrap.querySelector('[data-col-count]');
    var totalEl = wrap.querySelector('[data-col-total]');
    if (countEl) countEl.textContent = cards.length;
    if (totalEl) totalEl.textContent = fmt(total);
  }

  // ---------------- Contacts table search/filter ----------------
  var searchInput = document.getElementById('contacts-search');
  var stageFilter = document.getElementById('contacts-filter-stage');
  var table = document.getElementById('contacts-table');
  var countEl = document.getElementById('contacts-count');
  function applyFilters() {
    if (!table) return;
    var q = (searchInput && searchInput.value || '').toLowerCase().trim();
    var stage = stageFilter && stageFilter.value;
    var rows = table.querySelectorAll('tbody tr');
    var visible = 0;
    rows.forEach(function (row) {
      var matchesText = !q || row.dataset.name.indexOf(q) !== -1;
      var matchesStage = !stage || row.dataset.stage === stage;
      var show = matchesText && matchesStage;
      row.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    if (countEl) countEl.innerHTML = 'Showing <strong>' + visible + '</strong> of <strong>' + rows.length + '</strong> contacts';
  }
  if (searchInput) searchInput.addEventListener('input', applyFilters);
  if (stageFilter) stageFilter.addEventListener('change', applyFilters);

  // ---------------- Tasks ----------------
  document.querySelectorAll('[data-task-toggle]').forEach(function (cb) {
    cb.addEventListener('change', function () {
      var label = cb.closest('.list-group-item').querySelector('[data-task-label]');
      label.classList.toggle('text-decoration-line-through', cb.checked);
      label.classList.toggle('text-secondary', cb.checked);
      if (cb.checked && window.snToast) window.snToast('Task marked complete', { color: 'green', title: 'Tasks' });
    });
  });

  // ---------------- Quote status ----------------
  document.querySelectorAll('[data-quote-status]').forEach(function (item) {
    item.addEventListener('click', function (e) {
      e.preventDefault();
      var status = item.dataset.quoteStatus;
      var toggle = item.closest('.dropdown').querySelector('.dropdown-toggle');
      var colors = { Draft: 'secondary', Sent: 'azure', Approved: 'green', Invoiced: 'indigo' };
      toggle.className = 'badge bg-' + colors[status] + '-lt text-' + colors[status] + ' dropdown-toggle';
      toggle.textContent = status;
      if (window.snToast) window.snToast('Quote status set to <strong>' + status + '</strong>', { color: colors[status], title: 'Quotes' });
    });
  });

  // ---------------- Charts ----------------
  if (window.ApexCharts) {
    var months = ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb'];
    var revenue = [186000, 212000, 179000, 248000, 231000, 268000];
    var pipeline = [420000, 398000, 455000, 512000, 486000, (window.SN_LEADS || []).filter(function (l) { return l.stage !== 'won' && l.stage !== 'lost'; }).reduce(function (s, l) { return s + l.value; }, 0)];

    var revChart = new ApexCharts(document.querySelector('#chart-revenue'), {
      chart: { type: 'area', height: 260, toolbar: { show: false }, fontFamily: 'inherit', background: 'transparent' },
      series: [{ name: 'Closed revenue', data: revenue }, { name: 'Active pipeline', data: pipeline }],
      colors: ['#6366f1', '#22d3ee'],
      theme: { mode: 'dark' },
      stroke: { curve: 'smooth', width: 2 },
      fill: { type: 'gradient', gradient: { opacityFrom: 0.35, opacityTo: 0 } },
      dataLabels: { enabled: false },
      grid: { borderColor: 'rgba(255,255,255,.08)' },
      xaxis: { categories: months, axisBorder: { show: false }, axisTicks: { show: false } },
      yaxis: { labels: { formatter: function (v) { return '$' + Math.round(v / 1000) + 'k'; } } },
      legend: { position: 'top', horizontalAlign: 'left' },
      tooltip: { y: { formatter: function (v) { return fmt(v); } } },
    });
    revChart.render();

    if (window.SN_STAGES && window.SN_LEADS) {
      var stageTotals = window.SN_STAGES.map(function (s) {
        return window.SN_LEADS.filter(function (l) { return l.stage === s.key; }).reduce(function (sum, l) { return sum + l.value; }, 0);
      });
      var stageChart = new ApexCharts(document.querySelector('#chart-stages'), {
        chart: { type: 'donut', height: 260, fontFamily: 'inherit', background: 'transparent' },
        series: stageTotals,
        labels: window.SN_STAGES.map(function (s) { return s.label; }),
        theme: { mode: 'dark' },
        colors: ['#4299e1', '#22d3ee', '#6366f1', '#a78bfa', '#f0b429', '#2fb344', '#e63757'],
        legend: { position: 'bottom' },
        dataLabels: { enabled: false },
        tooltip: { y: { formatter: function (v) { return fmt(v); } } },
        plotOptions: { pie: { donut: { labels: { show: true, total: { show: true, formatter: function (w) { return fmt(w.globals.seriesTotals.reduce(function (a, b) { return a + b; }, 0)); } } } } } },
      });
      stageChart.render();
    }
  }

  // ---------------- FullCalendar ----------------
  var calEl = document.getElementById('followups-calendar');
  if (calEl && window.FullCalendar && window.SN_FOLLOWUPS) {
    var typeColor = { inspection: '#6366f1', call: '#22d3ee', job: '#2fb344', meeting: '#a78bfa', automation: '#f0b429' };
    var events = window.SN_FOLLOWUPS.map(function (f) {
      return { title: f.title, start: f.date + 'T' + f.time, color: typeColor[f.type] || '#6366f1' };
    });
    var calendar = new FullCalendar.Calendar(calEl, {
      initialView: 'listMonth',
      initialDate: '2026-02-24',
      height: 'auto',
      headerToolbar: { left: 'prev,next today', center: 'title', right: 'listWeek,listMonth' },
      buttonText: { listWeek: 'Week', listMonth: 'Month', today: 'Today' },
      noEventsText: 'No follow-ups scheduled',
      eventTimeFormat: { hour: 'numeric', minute: '2-digit', meridiem: 'short' },
      events: events,
    });
    calendar.render();
  }
})();
