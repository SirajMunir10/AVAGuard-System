/**
 * AVAGuard AI Compliance Assistant — User Query History Script
 */

(function() {
    'use strict';

    let currentPage = 1;
    let allHistoryData = []; // Local cache for instant client-side search across current pages

    // DOM Elements
    const searchInput = document.getElementById('ai-history-search');
    const tbody = document.getElementById('ai-history-tbody');
    const paginationContainer = document.getElementById('ai-history-pagination');
    const countLabel = document.getElementById('history-count-label');

    if (!tbody) return;

    // Fetch and load history logs
    function loadHistory(page) {
        currentPage = page || 1;
        
        // Show loading state
        tbody.innerHTML = `
            <tr>
                <td colspan="7" style="padding: 30px; text-align: center; color: var(--avag-text-secondary);">
                    <span class="spinner-small" style="margin-right: 8px;"></span>
                    Fetching compliance logs...
                </td>
            </tr>
        `;

        fetch(`/api/ai/history/?page=${currentPage}`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            if (!response.ok) throw new Error('Unauthenticated or server error.');
            return response.json();
        })
        .then(data => {
            allHistoryData = data.results || [];
            renderTable(allHistoryData);
            renderPagination(data.count, currentPage);
            
            if (countLabel) {
                countLabel.textContent = `Total audit queries conducted: ${data.count}`;
            }
        })
        .catch(err => {
            tbody.innerHTML = `
                <tr>
                    <td colspan="7" style="padding: 30px; text-align: center; color: var(--avag-accent-danger);">
                        <i data-lucide="shield-alert" style="width: 20px; height: 20px; vertical-align: middle; margin-right: 8px;"></i>
                        Failed to load compliance query records. Please check your credentials and try again.
                    </td>
                </tr>
            `;
            lucide.createIcons();
        });
    }

    // Render table rows
    function renderTable(logs) {
        if (logs.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="7" style="padding: 40px; text-align: center; color: var(--avag-text-secondary);">
                        <i data-lucide="info" style="width: 24px; height: 24px; display: block; margin: 0 auto 12px; opacity: 0.5;"></i>
                        No compliance queries matching filters.
                    </td>
                </tr>
            `;
            lucide.createIcons();
            return;
        }

        let html = '';
        logs.forEach(log => {
            const preview = log.response_text ? (log.response_text.substring(0, 75) + '...') : '(safety blocked)';
            const isFallback = log.is_fallback || log.model_used === 'mock';
            const sourcesCount = log.retrieved_sources ? log.retrieved_sources.length : 0;
            const dateStr = formatDate(log.created_at);

            html += `
                <tr style="border-bottom: 1px solid var(--avag-border-color); cursor: pointer;" class="ai-history-row" data-log-id="${log.id}">
                    <td style="padding: 16px 24px; font-weight: 500; color: var(--avag-text-primary); max-width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                        ${escapeHtml(log.query_text)}
                    </td>
                    <td style="padding: 16px 24px; color: var(--avag-text-secondary); max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                        ${escapeHtml(preview)}
                    </td>
                    <td style="padding: 16px 24px;">
                        <span class="ai-badge ${isFallback ? 'ai-badge-warning' : 'ai-badge-info'}">
                            <i data-lucide="${isFallback ? 'alert-triangle' : 'cpu'}"></i> ${escapeHtml(log.model_used)}
                        </span>
                    </td>
                    <td style="padding: 16px 24px; color: var(--avag-text-secondary);">
                        ${log.latency_ms ? Math.round(log.latency_ms) : 0}ms
                    </td>
                    <td style="padding: 16px 24px;">
                        <span class="badge ${sourcesCount > 0 ? 'badge-success' : 'badge-warning'}">
                            ${sourcesCount} cited
                        </span>
                    </td>
                    <td style="padding: 16px 24px; color: var(--avag-text-secondary);">
                        ${dateStr}
                    </td>
                    <td style="padding: 16px 24px; text-align: right;">
                        <button class="btn btn-secondary btn-small view-audit-btn">Open Audit</button>
                    </td>
                </tr>
            `;
        });

        tbody.innerHTML = html;
        lucide.createIcons();

        // Bind clicks to rows
        const rows = tbody.querySelectorAll('.ai-history-row');
        rows.forEach(row => {
            row.addEventListener('click', function(e) {
                // If clicked button, let standard handler trigger
                const logId = this.getAttribute('data-log-id');
                const log = allHistoryData.find(item => item.id === logId);
                if (log) {
                    showAuditLogCardModal(log);
                }
            });
        });
    }

    // Render pagination controls
    function renderPagination(totalCount, page) {
        if (!paginationContainer) return;

        const totalPages = Math.ceil(totalCount / 20);
        if (totalPages <= 1) {
            paginationContainer.innerHTML = '';
            return;
        }

        const startItem = (page - 1) * 20 + 1;
        const endItem = Math.min(page * 20, totalCount);

        let html = `
            <div class="ai-pagination-info">
                Showing entries <strong>${startItem} - ${endItem}</strong> of <strong>${totalCount}</strong>
            </div>
            <div class="ai-pagination-controls">
                <button class="btn btn-secondary btn-small" ${page === 1 ? 'disabled' : ''} data-page="${page - 1}">
                    <i data-lucide="chevron-left" style="width: 14px; height: 14px; vertical-align: middle;"></i> Previous
                </button>
        `;

        for (let i = 1; i <= totalPages; i++) {
            if (i === 1 || i === totalPages || (i >= page - 2 && i <= page + 2)) {
                html += `
                    <button class="btn ${i === page ? 'btn-primary' : 'btn-secondary'} btn-small" data-page="${i}">
                        ${i}
                    </button>
                `;
            } else if (i === 2 || i === totalPages - 1) {
                html += `<span style="align-self: center; padding: 0 4px; color: var(--avag-text-secondary);">...</span>`;
            }
        }

        html += `
                <button class="btn btn-secondary btn-small" ${page === totalPages ? 'disabled' : ''} data-page="${page + 1}">
                    Next <i data-lucide="chevron-right" style="width: 14px; height: 14px; vertical-align: middle;"></i>
                </button>
            </div>
        `;

        paginationContainer.innerHTML = html;
        lucide.createIcons();

        // Bind clicks to page buttons
        const pageBtns = paginationContainer.querySelectorAll('button[data-page]');
        pageBtns.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                const p = parseInt(this.getAttribute('data-page'));
                loadHistory(p);
            });
        });
    }

    // Client-side instant filter keyup handler
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const queryText = this.value.toLowerCase().trim();
            if (!queryText) {
                renderTable(allHistoryData);
                return;
            }

            const filtered = allHistoryData.filter(log => {
                const questionMatches = log.query_text && log.query_text.toLowerCase().includes(queryText);
                const answerMatches = log.response_text && log.response_text.toLowerCase().includes(queryText);
                const modelMatches = log.model_used && log.model_used.toLowerCase().includes(queryText);
                return questionMatches || answerMatches || modelMatches;
            });

            renderTable(filtered);
        });
    }

    // Reset filters
    window.clearFilters = function() {
        if (searchInput) searchInput.value = '';
        renderTable(allHistoryData);
    };

    // Shared modal view for query card detailing
    function showAuditLogCardModal(log) {
        const modalContainer = document.getElementById('ai-card-view-modal-container');
        const modalContent = document.getElementById('ai-card-modal-content');
        if (!modalContainer || !modalContent) return;

        const isFallback = log.is_fallback || log.model_used === 'mock';
        let sourcesHtml = '';
        if (log.retrieved_sources && log.retrieved_sources.length > 0) {
            sourcesHtml = `
                <div class="ai-query-sources">
                    <span class="ai-sources-label">
                        <i data-lucide="bookmark-check"></i> Grounded Citations:
                    </span>
                    <div class="ai-sources-list">
            `;
            log.retrieved_sources.forEach(src => {
                sourcesHtml += `
                    <button class="ai-source-badge" 
                            data-filename="${escapeHtml(src.filename)}" 
                            data-score="${src.score}" 
                            data-snippet="${escapeHtml(src.snippet)}">
                        <i data-lucide="file-text"></i>
                        <span class="ai-src-name">${escapeHtml(src.filename)}</span>
                        <span class="ai-src-score">${parseFloat(src.score).toFixed(3)}</span>
                    </button>
                `;
            });
            sourcesHtml += `
                    </div>
                </div>
            `;
        }

        modalContent.innerHTML = `
            <div class="ai-query-card ${isFallback ? 'fallback' : ''} ${log.flagged ? 'flagged' : ''}" style="margin-bottom: 0; box-shadow: none; border-radius: 8px;">
                <div class="ai-card-header">
                    <div class="ai-user-meta">
                        <span class="ai-user-email">
                            <i data-lucide="user" class="ai-meta-icon"></i>
                            You
                        </span>
                        <span class="ai-timestamp">
                            <i data-lucide="clock" class="ai-meta-icon"></i>
                            ${formatDate(log.created_at)}
                        </span>
                    </div>
                    <div class="ai-badges">
                        ${isFallback ? `
                            <span class="ai-badge ai-badge-warning animate-pulse">
                                <i data-lucide="alert-triangle"></i> Fallback Mode
                            </span>
                        ` : ''}
                        ${log.flagged ? `
                            <span class="ai-badge ai-badge-danger">
                                <i data-lucide="shield-alert"></i> Flagged
                            </span>
                        ` : `
                            <span class="ai-badge ai-badge-info">
                                <i data-lucide="cpu"></i> ${escapeHtml(log.model_used)}
                            </span>
                            <span class="ai-badge ai-badge-success">
                                <i data-lucide="gauge"></i> ${Math.round(log.latency_ms)}ms
                            </span>
                        `}
                    </div>
                </div>
                <div class="ai-card-body">
                    <div class="ai-query-question">
                        <span class="ai-q-indicator">Q</span>
                        <p class="ai-question-text">${escapeHtml(log.query_text)}</p>
                    </div>
                    
                    ${log.flagged ? `
                        <div class="ai-flagged-message">
                            <div class="ai-flagged-icon">
                                <i data-lucide="shield-x"></i>
                            </div>
                            <div class="ai-flagged-text">
                                <strong>Query Blocked by Safety Filters</strong>
                                <p>Reason: ${escapeHtml(log.flag_reason || 'Safety filter violation.')}</p>
                            </div>
                        </div>
                    ` : `
                        <div class="ai-query-answer">
                            <span class="ai-a-indicator">A</span>
                            <div class="ai-answer-text">${log.response_text.replace(/\n/g, '<br>')}</div>
                        </div>
                        ${sourcesHtml}
                    `}
                </div>
            </div>
        `;

        // Bind citation events in the modal
        bindCitationsClickEvents(modalContent);

        modalContainer.classList.add('visible');
        document.body.style.overflow = 'hidden';
        lucide.createIcons();
    }

    function closeCardModal() {
        const modalContainer = document.getElementById('ai-card-view-modal-container');
        if (!modalContainer) return;
        modalContainer.classList.remove('visible');
        const sourceModalContainer = document.getElementById('ai-source-modal-container');
        if (!sourceModalContainer || !sourceModalContainer.classList.contains('visible')) {
            document.body.style.overflow = '';
        }
    }

    window.closeCardModal = closeCardModal;

    // Citations details overlay
    function bindCitationsClickEvents(container) {
        if (!container) return;
        const badges = container.querySelectorAll('.ai-source-badge');
        badges.forEach(badge => {
            badge.addEventListener('click', function(e) {
                e.stopPropagation(); // Avoid row click triggers
                const filename = this.getAttribute('data-filename');
                const score = this.getAttribute('data-score');
                const snippet = this.getAttribute('data-snippet');
                
                openSourceModal(filename, score, snippet);
            });
        });
    }

    function openSourceModal(filename, score, snippet) {
        const sourceModalContainer = document.getElementById('ai-source-modal-container');
        const sourceTitle = document.getElementById('ai-source-title');
        const sourceScore = document.getElementById('ai-source-score');
        const sourceSnippet = document.getElementById('ai-source-snippet');

        if (!sourceModalContainer) return;
        
        sourceTitle.textContent = filename;
        sourceScore.textContent = 'Similarity Match: ' + parseFloat(score).toFixed(4);
        sourceSnippet.textContent = snippet;
        
        sourceModalContainer.classList.add('visible');
        document.body.style.overflow = 'hidden';
    }

    function closeSourceModal() {
        const sourceModalContainer = document.getElementById('ai-source-modal-container');
        if (sourceModalContainer) {
            sourceModalContainer.classList.remove('visible');
            const cardModal = document.getElementById('ai-card-view-modal-container');
            if (!cardModal || !cardModal.classList.contains('visible')) {
                document.body.style.overflow = '';
            }
        }
    }

    window.closeSourceModal = closeSourceModal;
    window.openSourceModal = openSourceModal;

    // Register Escape key listener globally
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            const sourceModalContainer = document.getElementById('ai-source-modal-container');
            if (sourceModalContainer && sourceModalContainer.classList.contains('visible')) {
                closeSourceModal();
            } else {
                closeCardModal();
            }
        }
    });


    // Helper functions
    function escapeHtml(str) {
        if (!str) return '';
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    function formatDate(isoStr) {
        if (!isoStr) return '';
        try {
            const date = new Date(isoStr);
            return date.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' }) + ' ' +
                   date.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit', hour12: false });
        } catch (e) {
            return isoStr;
        }
    }

    // Initial load
    loadHistory(1);

})();
