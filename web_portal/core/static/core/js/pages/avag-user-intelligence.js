/**
 * AVAGuard — User Intelligence Page Logic
 * Template: admin/user_sessions_detail.html
 */

(function () {
    'use strict';

    // ── Tab Switching ─────────────────────────────────────────────────────
    function switchTab(tabId) {
        document.querySelectorAll('.intel-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.intel-panel').forEach(p => p.classList.remove('active'));

        const btn = document.querySelector(`.intel-tab[data-tab="${tabId}"]`);
        const panel = document.getElementById(`panel-${tabId}`);
        if (btn) btn.classList.add('active');
        if (panel) panel.classList.add('active');

        // Persist in URL without reload
        try {
            const url = new URL(window.location.href);
            url.searchParams.set('tab', tabId);
            window.history.replaceState(null, '', url.toString());
        } catch (_) {}
    }

    // Restore tab from URL on load
    function restoreTab() {
        try {
            const params = new URLSearchParams(window.location.search);
            const tab = params.get('tab');
            if (tab && document.getElementById(`panel-${tab}`)) {
                switchTab(tab);
                return;
            }
        } catch (_) {}
        // Default to first tab
        const first = document.querySelector('.intel-tab');
        if (first) switchTab(first.dataset.tab);
    }

    // ── Action Badge Classifier ───────────────────────────────────────────
    function classifyAction(action) {
        if (!action) return 'info';
        const a = action.toUpperCase();
        if (a.includes('FAIL') || a.includes('LOCK') || a.includes('REVOKE')) return 'fail';
        if (a.includes('WARN') || a.includes('BYPASS') || a.includes('STALE')) return 'warn';
        if (a.includes('LOGIN') || a.includes('CREATED') || a.includes('AUTHORIZ') || a.includes('SETUP')) return 'success';
        return 'info';
    }

    // ── Audit event class classifier ─────────────────────────────────────
    function classifyEvent(action) {
        if (!action) return '';
        const a = action.toUpperCase();
        if (a.includes('FAIL') || a.includes('LOCK') || a.includes('REVOKE')) return 'failed';
        if (a.includes('WARN') || a.includes('BYPASS')) return 'warning';
        return '';
    }

    // ── Confirmation Modal Handlers ───────────────────────────────────────
    function confirmRevokeSingle(buttonEl, userName, userEmail, deviceName, ipAddress) {
        if (window.Modal && typeof window.Modal.confirmRevoke === 'function') {
            window.Modal.confirmRevoke({
                userName: userName,
                userEmail: userEmail,
                deviceName: deviceName,
                ipAddress: ipAddress,
                onConfirm: function() {
                    buttonEl.closest('form').submit();
                }
            });
        } else {
            if (confirm(`Revoke session for ${userEmail}?`)) {
                buttonEl.closest('form').submit();
            }
        }
    }

    function confirmRevokeAll(buttonEl, userName, totalActive) {
        if (window.Modal && typeof window.Modal.confirm === 'function') {
            window.Modal.confirm({
                title: 'Revoke All Sessions',
                icon: 'danger',
                message: `
                    <p>Are you sure you want to revoke <strong>ALL ${totalActive} active sessions</strong> for <strong>${userName}</strong>?</p>
                    <p class="ava-modal-warning">This user will be immediately logged out of all connected desktop apps.</p>
                `,
                confirmText: 'Revoke All',
                confirmClass: 'btn-danger',
                onConfirm: function() {
                    document.getElementById('revokeAllForm').submit();
                }
            });
        } else {
            if (confirm(`Revoke ALL ${totalActive} active session(s) for this user?`)) {
                document.getElementById('revokeAllForm').submit();
            }
        }
    }

    // ── Expose globally for inline onclick handlers ───────────────────────
    window.IntelPage = {
        switchTab,
        classifyAction,
        classifyEvent,
        confirmRevokeSingle,
        confirmRevokeAll,
    };

    // ── Init ──────────────────────────────────────────────────────────────
    document.addEventListener('DOMContentLoaded', function () {
        restoreTab();

        // Decorate action badges in the audit table
        document.querySelectorAll('[data-action-badge]').forEach(el => {
            const cls = classifyAction(el.dataset.actionBadge);
            el.classList.add('action-badge', cls);
        });

        // Decorate audit timeline events
        document.querySelectorAll('[data-audit-event]').forEach(el => {
            const cls = classifyEvent(el.dataset.auditEvent);
            if (cls) el.classList.add(cls);
        });
    });
}());
