(function () {
  'use strict';
  var nodes = window.SN_WF_NODES || [];
  var edges = window.SN_WF_EDGES || [];
  var canvas = document.getElementById('wf-canvas');
  var svg = document.getElementById('wf-svg');
  if (!canvas || !svg) return;

  var nodeById = {};
  nodes.forEach(function (n) { nodeById[n.id] = n; });

  function nodeEl(id) { return document.getElementById(id); }
  function centerPoint(el, side) {
    var x = parseFloat(el.style.left);
    var y = parseFloat(el.style.top);
    var w = el.offsetWidth || 220;
    var h = el.offsetHeight || 70;
    if (side === 'in') return { x: x, y: y + h / 2 };
    return { x: x + w, y: y + h / 2 };
  }

  function drawEdges() {
    var lines = svg.querySelectorAll('path.wf-edge');
    lines.forEach(function (l) { l.remove(); });
    edges.forEach(function (edge) {
      var from = nodeEl(edge[0]);
      var to = nodeEl(edge[1]);
      if (!from || !to) return;
      var p1 = centerPoint(from, 'out');
      var p2 = centerPoint(to, 'in');
      var dx = Math.max(60, (p2.x - p1.x) / 2);
      var d = 'M ' + p1.x + ' ' + p1.y + ' C ' + (p1.x + dx) + ' ' + p1.y + ', ' + (p2.x - dx) + ' ' + p2.y + ', ' + p2.x + ' ' + p2.y;
      var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('d', d);
      path.setAttribute('class', 'wf-edge');
      path.setAttribute('id', 'edge-' + edge[0] + '-' + edge[1]);
      path.setAttribute('fill', 'none');
      path.setAttribute('stroke', '#6366f1');
      path.setAttribute('stroke-opacity', '0.55');
      path.setAttribute('stroke-width', '2');
      path.setAttribute('marker-end', 'url(#arrow)');
      svg.insertBefore(path, svg.firstChild.nextSibling);
    });
  }

  // ---------------- dragging ----------------
  var dragState = null;
  document.querySelectorAll('.wf-node').forEach(function (el) {
    el.addEventListener('pointerdown', function (e) {
      if (e.target.closest('.wf-port')) return;
      var rect = el.getBoundingClientRect();
      dragState = { el: el, offX: e.clientX - rect.left, offY: e.clientY - rect.top };
      el.classList.add('dragging');
      el.setPointerCapture(e.pointerId);
    });
    el.addEventListener('pointermove', function (e) {
      if (!dragState || dragState.el !== el) return;
      var canvasRect = canvas.getBoundingClientRect();
      var newX = e.clientX - canvasRect.left + canvas.scrollLeft - dragState.offX;
      var newY = e.clientY - canvasRect.top + canvas.scrollTop - dragState.offY;
      el.style.left = Math.max(0, newX) + 'px';
      el.style.top = Math.max(0, newY) + 'px';
      drawEdges();
    });
    ['pointerup', 'pointercancel'].forEach(function (evt) {
      el.addEventListener(evt, function () {
        if (dragState && dragState.el === el) { el.classList.remove('dragging'); dragState = null; }
      });
    });
    el.addEventListener('click', function () { selectNode(el.id); });
  });

  function selectNode(id) {
    document.querySelectorAll('.wf-node').forEach(function (el) { el.classList.remove('selected'); });
    var el = nodeEl(id);
    if (el) el.classList.add('selected');
    var n = nodeById[id];
    var detail = document.getElementById('wf-detail');
    if (n && detail) {
      detail.innerHTML =
        '<div class="d-flex align-items-center gap-2 mb-2"><span class="badge bg-' + n.color + '-lt text-' + n.color + '">' + n.type + '</span></div>' +
        '<h4 class="mb-1">' + n.label + '</h4>' +
        '<div class="text-secondary small mb-2">' + n.subtitle + '</div>' +
        '<p class="text-secondary small mb-0">' + n.detail + '</p>';
    }
  }

  document.getElementById('wf-reset').addEventListener('click', function () {
    nodes.forEach(function (n) {
      var el = nodeEl(n.id);
      if (el) { el.style.left = n.x + 'px'; el.style.top = n.y + 'px'; }
    });
    drawEdges();
    if (window.snToast) window.snToast('Layout reset to default', { title: 'Workflow Gallery' });
  });

  // ---------------- run simulation ----------------
  var LOG_STEPS = [
    { id: 'n1', msg: 'Lead form submitted by homeowner (Frisco, TX) — payload captured.' },
    { id: 'n2', msg: 'Webhook received POST /lead-intake — payload validated ✓' },
    { id: 'n3', msg: 'OpenAI analysis complete — priority_score: 88, recommended_action: "call_immediately"' },
    { id: 'n4', msg: 'Condition evaluated — score ≥ 70 → high-priority branch selected' },
    { id: 'n5', msg: 'Row appended to Google Sheets "Leads Tracker" (row 1,248)' },
    { id: 'n6', msg: 'Contact upserted in GoHighLevel — assigned to Mike Torres' },
    { id: 'n7', msg: 'Confirmation email queued and sent to homeowner' },
    { id: 'n8', msg: 'Slack message posted to #new-leads ✓' },
  ];

  var running = false;
  document.getElementById('wf-run').addEventListener('click', function () {
    if (running) return;
    running = true;
    var btn = this;
    btn.disabled = true;
    var logEl = document.getElementById('wf-log');
    logEl.innerHTML = '';
    document.querySelectorAll('.wf-node').forEach(function (el) { el.classList.remove('exec-active'); });

    var start = performance.now();
    LOG_STEPS.forEach(function (step, i) {
      setTimeout(function () {
        document.querySelectorAll('.wf-node').forEach(function (el) { el.classList.remove('exec-active'); });
        var el = nodeEl(step.id);
        if (el) { el.classList.add('exec-active'); el.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' }); }
        var line = document.createElement('div');
        var t = ((performance.now() - start) / 1000).toFixed(2);
        line.innerHTML = '<span style="color:#6ee7b7;">[' + t + 's]</span> ' + step.msg;
        line.style.marginBottom = '4px';
        logEl.appendChild(line);
        logEl.scrollTop = logEl.scrollHeight;
        if (i === LOG_STEPS.length - 1) {
          setTimeout(function () {
            document.querySelectorAll('.wf-node').forEach(function (el2) { el2.classList.remove('exec-active'); });
            var total = ((performance.now() - start) / 1000).toFixed(2);
            var doneLine = document.createElement('div');
            doneLine.innerHTML = '<span style="color:#22d3ee;">✓ Execution completed successfully in ' + total + 's</span>';
            doneLine.style.marginTop = '6px';
            logEl.appendChild(doneLine);
            logEl.scrollTop = logEl.scrollHeight;
            if (window.snToast) window.snToast('Workflow executed successfully in ' + total + 's', { color: 'green', title: 'Lead Qualification Automation' });
            running = false;
            btn.disabled = false;
          }, 500);
        }
      }, i * 550);
    });
  });

  drawEdges();
  window.addEventListener('resize', drawEdges);
})();
