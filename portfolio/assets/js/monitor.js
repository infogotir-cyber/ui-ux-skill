(function () {
  'use strict';

  if (window.ApexCharts) {
    var execChart = new ApexCharts(document.querySelector('#chart-executions'), {
      chart: { type: 'bar', height: 230, toolbar: { show: false }, fontFamily: 'inherit', background: 'transparent' },
      series: [{ name: 'Executions', data: window.SN_MON_COUNTS || [] }],
      colors: ['#6366f1'],
      theme: { mode: 'dark' },
      plotOptions: { bar: { borderRadius: 3, columnWidth: '55%' } },
      dataLabels: { enabled: false },
      grid: { borderColor: 'rgba(255,255,255,.08)' },
      xaxis: { categories: window.SN_MON_HOURS || [], labels: { rotate: 0, style: { fontSize: '9px' } }, tickAmount: 8 },
    });
    execChart.render();

    var successChart = new ApexCharts(document.querySelector('#chart-success'), {
      chart: { type: 'donut', height: 230, fontFamily: 'inherit', background: 'transparent' },
      series: window.SN_MON_SUCCESS || [0, 0, 0],
      labels: ['Success', 'Error', 'Running'],
      colors: ['#2fb344', '#e63757', '#4299e1'],
      theme: { mode: 'dark' },
      legend: { position: 'bottom' },
      dataLabels: { enabled: true, formatter: function (v) { return Math.round(v) + '%'; } },
    });
    successChart.render();
  }

  var filter = document.getElementById('log-filter');
  var rows = document.querySelectorAll('#log-table tbody tr');
  if (filter) {
    filter.addEventListener('change', function () {
      var val = filter.value;
      rows.forEach(function (r) {
        r.style.display = !val || r.dataset.status === val ? '' : 'none';
      });
    });
  }

  // Simulate a live tick: occasionally flip a random "running" row to success
  var runningRows = Array.prototype.slice.call(document.querySelectorAll('tr[data-status="running"]'));
  if (runningRows.length) {
    setTimeout(function () {
      var row = runningRows[0];
      row.dataset.status = 'success';
      row.querySelector('.status-dot').className = 'status-dot bg-green';
      var statusCell = row.children[4];
      statusCell.innerHTML = '<span class="badge bg-green-lt text-green">Success</span>';
      row.children[5].textContent = (1.4 + Math.random() * 2).toFixed(2) + 's';
      if (window.snToast) window.snToast('Workflow execution completed successfully', { color: 'green', title: 'Automation Monitor' });
    }, 4000);
  }
})();
