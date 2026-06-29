/**
 * AVAGuard — Dashboard Index Logic
 * Template: dashboard/index.html
 * =========================================================
 */

document.addEventListener('DOMContentLoaded', function () {
    if (!window.AVA) return;
    
    // Data from Django template via bridge
    var trendLabels = AVAGuardCharts.parseJSON(window.AVA.trendLabels, ["Week 1", "Week 2", "Week 3", "Week 4"]);
    var trendData = AVAGuardCharts.parseJSON(window.AVA.trendData, [75, 78, 82, 85]);
    var statsPassed = Number(window.AVA.statsPassed || 70);
    var statsFailed = Number(window.AVA.statsFailed || 20);
    var statsWarning = Number(window.AVA.statsWarning || 10);

    // Initialize charts using library functions
    AVAGuardCharts.initTrendChart('trendChart', trendLabels, trendData);
    AVAGuardCharts.initStatusChart('statusChart', statsPassed, statsFailed, statsWarning);

    // Apply data-width to progress bars
    document.querySelectorAll('.score-bar-fill').forEach(function(bar) {
        var w = bar.getAttribute('data-width');
        if (w) bar.style.width = w + '%';
    });

    // ── Compliance score count-up animation ──────────────────────────────
    var scoreEl = document.getElementById('compliance-score');
    if (scoreEl) {
        var targetVal = parseFloat(scoreEl.getAttribute('data-target'));
        if (!isNaN(targetVal) && targetVal > 0) {
            var start = 0;
            var duration = 900; // ms
            var startTime = null;

            function animateCount(timestamp) {
                if (!startTime) startTime = timestamp;
                var elapsed = timestamp - startTime;
                var progress = Math.min(elapsed / duration, 1);
                // Ease-out cubic
                var eased = 1 - Math.pow(1 - progress, 3);
                var current = (eased * targetVal).toFixed(1);
                scoreEl.textContent = current + '%';
                if (progress < 1) {
                    requestAnimationFrame(animateCount);
                }
            }

            // Delay the count-up slightly so it fires after the card slides in
            setTimeout(function() {
                requestAnimationFrame(animateCount);
            }, 200);
        }
    }

    // ── Stat card hover glow micro-interaction ───────────────────────────
    document.querySelectorAll('.stat-card').forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.transition = 'transform 0.2s ease, box-shadow 0.2s ease';
            this.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.25)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });
});
