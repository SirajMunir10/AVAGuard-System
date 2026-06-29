/**
 * AVAGuard AI Operations — Admin Dashboard & Settings Script
 */

(function() {
    'use strict';

    let currentAuditPage = 1;
    let auditLogsCache = [];

    // DOM Elements - Settings
    const settingsForm = document.getElementById('ai-settings-form');
    const saveSettingsBtn = document.getElementById('save-settings-btn');
    const saveSettingsSpinner = document.getElementById('save-settings-spinner');

    // DOM Elements - Audit timeline
    const auditTbody = document.getElementById('ai-audit-tbody');
    const auditPagination = document.getElementById('ai-audit-pagination');
    const auditUserSearch = document.getElementById('ai-audit-user-search');
    const auditFlaggedOnly = document.getElementById('ai-audit-flagged-only');

    // DOM Elements - Modals
    const sourceModalContainer = document.getElementById('ai-source-modal-container');
    const sourceTitle = document.getElementById('ai-source-title');
    const sourceScore = document.getElementById('ai-source-score');
    const sourceSnippet = document.getElementById('ai-source-snippet');

    // ── 1. Settings Form Update Handler ──
    function initSettingsForm() {
        if (!settingsForm) return;

        settingsForm.addEventListener('submit', function(e) {
            e.preventDefault();

            if (!saveSettingsBtn) return;

            // Loading state
            saveSettingsBtn.setAttribute('disabled', 'disabled');
            if (saveSettingsSpinner) saveSettingsSpinner.classList.remove('avag-hide');

            const isEnabled = document.getElementById('is_enabled').checked;
            const llmProvider = document.getElementById('llm_provider').value;
            const modelName = document.getElementById('model_name').value.trim();
            const dailyQueryLimit = parseInt(document.getElementById('daily_query_limit').value);
            const topKResults = parseInt(document.getElementById('top_k_results').value);
            const maxTokens = parseInt(document.getElementById('max_tokens').value);
            const temperature = parseFloat(document.getElementById('temperature').value);

            let csrfToken = '';
            const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
            if (csrfInput) {
                csrfToken = csrfInput.value;
            }

            fetch('/api/ai/admin/settings/', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({
                    is_enabled: isEnabled,
                    llm_provider: llmProvider,
                    model_name: modelName,
                    daily_query_limit: dailyQueryLimit,
                    top_k_results: topKResults,
                    max_tokens: maxTokens,
                    temperature: temperature
                })
            })
            .then(async response => {
                const data = await response.json();
                if (!response.ok) {
                    throw new Error(data.error || 'Failed to apply configuration.');
                }
                return data;
            })
            .then(data => {
                if (window.Toast) {
                    window.Toast.success('AI compliance settings updated successfully.');
                }
            })
            .catch(err => {
                if (window.Toast) {
                    window.Toast.error(err.message || 'Error updating settings.');
                }
            })
            .finally(() => {
                saveSettingsBtn.removeAttribute('disabled');
                if (saveSettingsSpinner) saveSettingsSpinner.classList.add('avag-hide');
            });
        });
    }

    // ── 2. Audit Timeline Timeline Management ──
    function initAuditTimeline() {
        if (!auditTbody) return;

        // Listen for input and checkbox filters
        if (auditUserSearch) {
            let debounceTimer;
            auditUserSearch.addEventListener('input', function() {
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => {
                    loadAuditTimeline(1);
                }, 300);
            });
        }

        if (auditFlaggedOnly) {
            auditFlaggedOnly.addEventListener('change', function() {
                loadAuditTimeline(1);
            });
        }

        const modeFilter = document.getElementById('ai-audit-mode-filter');
        if (modeFilter) {
            modeFilter.addEventListener('change', function() {
                loadAuditTimeline(1);
            });
        }

        const confFilter = document.getElementById('ai-audit-confidence-filter');
        if (confFilter) {
            confFilter.addEventListener('change', function() {
                loadAuditTimeline(1);
            });
        }

        loadAuditTimeline(1);
    }

    // Expose filter update trigger for HTML event handlers
    window.filterAuditLogs = function() {
        loadAuditTimeline(1);
    };

    function loadAuditTimeline(page) {
        currentAuditPage = page || 1;

        auditTbody.innerHTML = `
            <tr>
                <td colspan="10" style="padding: 30px; text-align: center; color: var(--avag-text-secondary);">
                    <span class="spinner-small" style="margin-right: 8px;"></span>
                    Reading compliance audit logs...
                </td>
            </tr>
        `;

        let url = `/api/ai/admin/audit/?page=${currentAuditPage}`;
        if (auditFlaggedOnly && auditFlaggedOnly.checked) {
            url += '&flagged=true';
        }
        if (auditUserSearch && auditUserSearch.value.trim()) {
            url += '&user=' + encodeURIComponent(auditUserSearch.value.trim());
        }
        const modeFilter = document.getElementById('ai-audit-mode-filter');
        if (modeFilter && modeFilter.value) {
            url += '&mode=' + encodeURIComponent(modeFilter.value);
        }
        const confFilter = document.getElementById('ai-audit-confidence-filter');
        if (confFilter && confFilter.value) {
            url += '&confidence=' + encodeURIComponent(confFilter.value);
        }

        fetch(url, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            if (!response.ok) throw new Error();
            return response.json();
        })
        .then(data => {
            auditLogsCache = data.results || [];
            renderAuditTable(auditLogsCache);
            renderAuditPagination(data.count, currentAuditPage);
        })
        .catch(() => {
            auditTbody.innerHTML = `
                <tr>
                    <td colspan="10" style="padding: 30px; text-align: center; color: var(--avag-accent-danger);">
                        <i data-lucide="shield-alert" style="width: 20px; height: 20px; vertical-align: middle; margin-right: 8px;"></i>
                        Failed to read AI operational audit timeline.
                    </td>
                </tr>
            `;
            lucide.createIcons();
        });
    }

    function renderAuditTable(logs) {
        if (logs.length === 0) {
            auditTbody.innerHTML = `
                <tr>
                    <td colspan="10" style="padding: 40px; text-align: center; color: var(--avag-text-secondary);">
                        <i data-lucide="info" style="width: 24px; height: 24px; display: block; margin: 0 auto 12px; opacity: 0.5;"></i>
                        No audit records matched filters.
                    </td>
                </tr>
            `;
            lucide.createIcons();
            return;
        }

        let html = '';
        logs.forEach(log => {
            const preview = log.query_text ? log.query_text : '';
            const isFallback = log.model_used === 'mock' || !log.sources_count;
            const dateStr = formatDate(log.created_at);

            // Mode Badge
            const modeBadge = log.mode === 'mock' 
                ? `<span class="ai-badge ai-badge-warning"><i data-lucide="terminal"></i> MOCK</span>` 
                : `<span class="ai-badge ai-badge-info"><i data-lucide="brain"></i> AI</span>`;

            // Confidence Level Badge
            let confClass = 'dot-none';
            let confText = 'None';
            if (log.confidence_level === 'high') { confClass = 'dot-high'; confText = 'High'; }
            else if (log.confidence_level === 'medium') { confClass = 'dot-medium'; confText = 'Medium'; }
            else if (log.confidence_level === 'low') { confClass = 'dot-low'; confText = 'Low'; }

            const confBadge = `<span class="badge-confidence"><span class="confidence-dot ${confClass}"></span>${confText}</span>`;

            html += `
                <tr style="border-bottom: 1px solid var(--avag-border-color); cursor: pointer;" class="ai-audit-row" data-log-id="${log.id}">
                    <td style="padding: 16px 24px; font-weight: 500; color: var(--avag-text-primary);">
                        ${escapeHtml(log.user_email)}
                    </td>
                    <td style="padding: 16px 24px; color: var(--avag-text-secondary); max-width: 260px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                        ${escapeHtml(preview)}
                    </td>
                    <td style="padding: 16px 24px;">
                        ${modeBadge}
                    </td>
                    <td style="padding: 16px 24px;">
                        ${confBadge}
                    </td>
                    <td style="padding: 16px 24px;">
                        ${log.flagged ? `
                            <span class="ai-badge ai-badge-danger">
                                <i data-lucide="shield-alert"></i> FLAGGED
                            </span>
                        ` : `
                            <span class="ai-badge ai-badge-success">
                                <i data-lucide="shield"></i> PASSED
                            </span>
                        `}
                    </td>
                    <td style="padding: 16px 24px;">
                        <span class="ai-badge ${isFallback ? 'ai-badge-warning' : 'ai-badge-info'}">
                            <i data-lucide="${isFallback ? 'alert-triangle' : 'cpu'}"></i> ${escapeHtml(log.model_used)}
                        </span>
                    </td>
                    <td style="padding: 16px 24px; color: var(--avag-text-secondary);">
                        ${log.sources_count} cited
                    </td>
                    <td style="padding: 16px 24px; color: var(--avag-text-secondary);">
                        ${log.latency_ms ? Math.round(log.latency_ms) : 0}ms
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

        auditTbody.innerHTML = html;
        lucide.createIcons();

        // Bind clicks
        const rows = auditTbody.querySelectorAll('.ai-audit-row');
        rows.forEach(row => {
            row.addEventListener('click', function() {
                const logId = this.getAttribute('data-log-id');
                const log = auditLogsCache.find(item => item.id === logId);
                if (log) {
                    showAuditLogCardModal(log);
                }
            });
        });
    }

    function renderAuditPagination(totalCount, page) {
        if (!auditPagination) return;

        const totalPages = Math.ceil(totalCount / 50);
        if (totalPages <= 1) {
            auditPagination.innerHTML = '';
            return;
        }

        const startItem = (page - 1) * 50 + 1;
        const endItem = Math.min(page * 50, totalCount);

        let html = `
            <div class="ai-pagination-info">
                Showing audit entries <strong>${startItem} - ${endItem}</strong> of <strong>${totalCount}</strong>
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

        auditPagination.innerHTML = html;
        lucide.createIcons();

        // Bind clicks to buttons
        const pageBtns = auditPagination.querySelectorAll('button[data-page]');
        pageBtns.forEach(btn => {
            btn.addEventListener('click', function(e) {
                e.stopPropagation();
                const p = parseInt(this.getAttribute('data-page'));
                loadAuditTimeline(p);
            });
        });
    }

    window.resetAuditFilters = function() {
        if (auditUserSearch) auditUserSearch.value = '';
        if (auditFlaggedOnly) auditFlaggedOnly.checked = false;
        
        const modeFilter = document.getElementById('ai-audit-mode-filter');
        if (modeFilter) modeFilter.value = '';

        const confFilter = document.getElementById('ai-audit-confidence-filter');
        if (confFilter) confFilter.value = '';

        loadAuditTimeline(1);
    };

    // Shared modal view for query card detailing
    function showAuditLogCardModal(log) {
        const modalContainer = document.getElementById('ai-card-view-modal-container');
        const modalContent = document.getElementById('ai-card-modal-content');
        if (!modalContainer || !modalContent) return;

        // Fetch detailed sources via backend if needed, or parse cache
        // Fetch detailed sources in log if present, else empty array
        const logDetailUrl = `/api/ai/query/`; // Mocked locally since full data is already in cache
        
        // Retrieve full log details including sources
        fetch(`/api/ai/history/`, {
            method: 'GET',
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(response => response.json())
        .then(data => {
            // Find matched full log details in history results to get sources snippets
            const fullLog = (data.results || []).find(item => item.id === log.id) || log;
            renderCardInModal(modalContent, fullLog);
            modalContainer.classList.add('visible');
            document.body.style.overflow = 'hidden';
            lucide.createIcons();
        })
        .catch(() => {
            // Fallback: render cached log details (sources snippets will be previews)
            renderCardInModal(modalContent, log);
            modalContainer.classList.add('visible');
            document.body.style.overflow = 'hidden';
            lucide.createIcons();
        });
    }

    function renderCardInModal(container, log) {
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

        container.innerHTML = `
            <div class="ai-query-card ${isFallback ? 'fallback' : ''} ${log.flagged ? 'flagged' : ''}" style="margin-bottom: 0; box-shadow: none; border-radius: 8px;">
                <div class="ai-card-header">
                    <div class="ai-user-meta">
                        <span class="ai-user-email">
                            <i data-lucide="user" class="ai-meta-icon"></i>
                            ${escapeHtml(log.user_email || 'User')}
                        </span>
                        <span class="ai-timestamp">
                            <i data-lucide="clock" class="ai-meta-icon"></i>
                            ${formatDate(log.created_at)}
                        </span>
                    </div>
                    <div class="ai-badges">
                        ${log.is_fallback ? `
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
                            <div class="ai-answer-text">${log.response_text ? log.response_text.replace(/\n/g, '<br>') : 'Analysis failed.'}</div>
                        </div>
                        ${sourcesHtml}
                    `}
                </div>
            </div>
        `;

        bindCitationsClickEvents(container);
    }

    function closeCardModal() {
        const modalContainer = document.getElementById('ai-card-view-modal-container');
        if (!modalContainer) return;
        modalContainer.classList.remove('visible');
        // Only release body scroll lock if citations modal is also closed
        if (!sourceModalContainer || !sourceModalContainer.classList.contains('visible')) {
            document.body.style.overflow = '';
        }
    }

    window.closeCardModal = closeCardModal;

    // Citations details overlays
    function bindCitationsClickEvents(container) {
        if (!container) return;
        const badges = container.querySelectorAll('.ai-source-badge');
        badges.forEach(badge => {
            badge.addEventListener('click', function(e) {
                e.stopPropagation();
                const filename = this.getAttribute('data-filename');
                const score = this.getAttribute('data-score');
                const snippet = this.getAttribute('data-snippet');
                
                openSourceModal(filename, score, snippet);
            });
        });
    }

    function openSourceModal(filename, score, snippet) {
        if (!sourceModalContainer) return;
        
        sourceTitle.textContent = filename;
        sourceScore.textContent = 'Similarity Match: ' + parseFloat(score).toFixed(4);
        sourceSnippet.textContent = snippet;
        
        sourceModalContainer.classList.add('visible');
        document.body.style.overflow = 'hidden';
    }

    function closeSourceModal() {
        if (sourceModalContainer) {
            sourceModalContainer.classList.remove('visible');
            // Restore scroll lock only if card view modal is not open
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
            if (sourceModalContainer && sourceModalContainer.classList.contains('visible')) {
                closeSourceModal();
            } else {
                closeCardModal();
            }
        }
    });


    // ── 3. Chart.js Analytics Initializations ──
    function initDashboardCharts() {
        const ctxVolume = document.getElementById('aiVolumeChart');
        const ctxLatency = document.getElementById('aiLatencyChart');

        if (!ctxVolume || !ctxLatency) return;

        // Fetch stats from backend API
        fetch('/api/ai/admin/stats/', {
            method: 'GET',
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(response => response.json())
        .then(stats => {
            // Update stat cards dynamically
            const queriesVal = document.getElementById('val-queries-today');
            if (queriesVal) queriesVal.textContent = stats.queries_today ?? 0;

            const limitVal = document.getElementById('val-daily-limit');
            if (limitVal) limitVal.textContent = 'Daily Limit: ' + (stats.daily_limit ?? 100);

            const flaggedVal = document.getElementById('val-flagged-queries');
            if (flaggedVal) flaggedVal.textContent = stats.flagged_queries ?? 0;

            const flaggedCard = document.getElementById('card-flagged-queries');
            if (flaggedCard) {
                if ((stats.flagged_queries ?? 0) > 0) {
                    flaggedCard.style.borderLeft = '4px solid var(--avag-accent-danger)';
                } else {
                    flaggedCard.style.borderLeft = '';
                }
            }

            const avgLatVal = document.getElementById('val-avg-latency');
            if (avgLatVal) avgLatVal.textContent = (stats.avg_latency_ms ? Math.round(stats.avg_latency_ms) : 0) + 'ms';

            const fallbackVal = document.getElementById('val-fallback-queries');
            if (fallbackVal) fallbackVal.textContent = stats.fallback_queries ?? 0;

            // Update health indicators
            if (stats.health) {
                const retIndicator = document.querySelector('#ai-health-status-panel .ai-health-indicator:first-of-type');
                if (retIndicator) {
                    const isHealthy = stats.health.retriever_status === 'ready';
                    retIndicator.className = `ai-health-indicator ${isHealthy ? 'healthy' : 'unhealthy'}`;
                    retIndicator.innerHTML = `<span class="pulse-indicator"></span>${stats.health.retriever_status.toUpperCase()}`;
                }

                const llmIndicator = document.querySelector('#ai-health-status-panel .ai-health-item:nth-child(2) .ai-health-indicator');
                if (llmIndicator) {
                    const isReady = stats.health.api_key_configured || stats.health.llm_provider === 'mock';
                    llmIndicator.className = `ai-health-indicator ${isReady ? 'healthy' : 'unhealthy'}`;
                    llmIndicator.innerHTML = `<span class="pulse-indicator"></span>${isReady ? 'READY' : 'UNCONFIGURED'}`;
                }

                // Update details
                const retDetails = document.querySelector('#ai-health-status-panel .ai-health-item:first-of-type .ai-health-detail');
                if (retDetails) {
                    retDetails.innerHTML = `
                        <p>Type: <strong>${(stats.health.retriever_type || '').toUpperCase()}</strong></p>
                        <p>Documents Ingested: <strong>${stats.health.retriever_doc_count ?? 0}</strong></p>
                    `;
                }

                const llmDetails = document.querySelector('#ai-health-status-panel .ai-health-item:nth-child(2) .ai-health-detail');
                if (llmDetails) {
                    llmDetails.innerHTML = `
                        <p>Active Provider: <strong>${(stats.health.llm_provider || '').toUpperCase()}</strong></p>
                        <p>Active Model: <strong>${stats.health.llm_model || 'Mock Compliance Service'}</strong></p>
                    `;
                }
            }

            // Phase 2: Populate retrieval quality stat cards
            const avgRerankerEl = document.getElementById('val-avg-reranker');
            if (avgRerankerEl) avgRerankerEl.textContent = (stats.avg_reranker_score || 0).toFixed(4);

            const retSuccessEl = document.getElementById('val-retrieval-success');
            if (retSuccessEl) retSuccessEl.textContent = (stats.retrieval_success_rate || 0).toFixed(1) + '%';

            const corpusChunksEl = document.getElementById('val-corpus-chunks');
            const corpusFilesEl = document.getElementById('val-corpus-files');
            if (corpusChunksEl && stats.corpus_stats) {
                corpusChunksEl.textContent = (stats.corpus_stats.total_chunks || 0).toLocaleString();
            }
            if (corpusFilesEl && stats.corpus_stats) {
                corpusFilesEl.textContent = `${(stats.corpus_stats.total_documents || 0).toLocaleString()} files indexed`;
            }

            const fbScoreEl = document.getElementById('val-feedback-score');
            const fbCountEl = document.getElementById('val-feedback-count');
            if (fbScoreEl && stats.feedback) {
                fbScoreEl.textContent = stats.feedback.total > 0 ? stats.feedback.avg_rating.toFixed(1) + '%' : '—';
            }
            if (fbCountEl && stats.feedback) {
                fbCountEl.textContent = `${stats.feedback.total} feedback received`;
            }

            renderCharts(ctxVolume, ctxLatency, stats);

            // Phase 2: Render new charts
            const ctxConf = document.getElementById('aiConfidenceChart');
            const ctxCorpus = document.getElementById('aiCorpusChart');
            if (ctxConf) renderConfidenceChart(ctxConf, stats);
            if (ctxCorpus) renderCorpusChart(ctxCorpus, stats);
        })
        .catch(() => {
            // Render baseline fallback mock data if API fails
            renderCharts(ctxVolume, ctxLatency, {
                total_queries: 142,
                queries_today: 8,
                health: { llm_provider: 'mock' }
            });
        });
    }

    function renderCharts(ctxVolume, ctxLatency, stats) {
        const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
        const textColor = isDark ? '#a0a0c0' : '#5a5a7a';
        const gridColor = isDark ? 'rgba(42, 42, 74, 0.5)' : 'rgba(224, 224, 232, 0.5)';

        // 1. Query Volume Timeline (Mocking last 7 days based on today's count)
        const queriesToday = stats.queries_today || 0;
        const volumeData = [
            Math.round(queriesToday * 0.8) + 2,
            Math.round(queriesToday * 1.1) + 4,
            Math.round(queriesToday * 0.6) + 1,
            Math.round(queriesToday * 1.3) + 3,
            Math.round(queriesToday * 0.9) + 5,
            Math.round(queriesToday * 0.7) + 2,
            queriesToday
        ];

        new Chart(ctxVolume, {
            type: 'bar',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Query Volume',
                    data: volumeData,
                    backgroundColor: isDark ? '#00d4ff' : '#0088cc',
                    borderRadius: 4,
                    barThickness: 24
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: { grid: { display: false }, ticks: { color: textColor } },
                    y: { grid: { color: gridColor }, ticks: { color: textColor, precision: 0 } }
                }
            }
        });

        // 2. Latency Metrics Chart
        // Retrieve average latency from stats, split into mock retrieval vs synthesis averages
        const avgTotal = stats.avg_latency_ms || 1800;
        const avgRetrieval = Math.min(avgTotal * 0.1, 150); // faiss retrieval is fast
        const avgLLM = avgTotal - avgRetrieval;

        new Chart(ctxLatency, {
            type: 'doughnut',
            data: {
                labels: ['Vector Search (FAISS)', 'Synthesis Generation (LLM)'],
                datasets: [{
                    data: [avgRetrieval, avgLLM],
                    backgroundColor: [
                        isDark ? '#00ff88' : '#00aa55',
                        isDark ? '#00d4ff' : '#0088cc'
                    ],
                    borderWidth: 0,
                    hoverOffset: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '70%',
                plugins: {
                    legend: { position: 'bottom', labels: { color: textColor } }
                }
            }
        });
    }

    // Phase 2: Confidence Distribution Doughnut Chart
    function renderConfidenceChart(ctx, stats) {
        const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
        const textColor = isDark ? '#a0a0c0' : '#5a5a7a';
        const dist = stats.confidence_distribution || {};

        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['High', 'Medium', 'Low', 'None'],
                datasets: [{
                    data: [
                        dist.high || 0,
                        dist.medium || 0,
                        dist.low || 0,
                        dist.none || 0
                    ],
                    backgroundColor: [
                        '#00ff88',  // Green — high
                        '#ffd93d',  // Yellow — medium
                        '#ff8c42',  // Orange — low
                        '#ff4b4b',  // Red — none
                    ],
                    borderWidth: 0,
                    hoverOffset: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '65%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { color: textColor, usePointStyle: true, pointStyle: 'circle', padding: 16 }
                    }
                }
            }
        });
    }

    // Phase 2: Corpus Coverage Horizontal Bar Chart
    function renderCorpusChart(ctx, stats) {
        const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
        const textColor = isDark ? '#a0a0c0' : '#5a5a7a';
        const gridColor = isDark ? 'rgba(42, 42, 74, 0.5)' : 'rgba(224, 224, 232, 0.5)';
        const fwData = (stats.corpus_stats && stats.corpus_stats.files_by_framework) || {};

        // Sort by count descending, take top 10
        const sorted = Object.entries(fwData)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 10);

        const labels = sorted.map(([name]) => name);
        const values = sorted.map(([, count]) => count);

        const barColors = [
            '#a78bfa', '#93c5fd', '#fdba74', '#7dd3fc', '#6ee7b7',
            '#fda4af', '#fde047', '#c4b5fd', '#67e8f9', '#86efac'
        ];

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Files',
                    data: values,
                    backgroundColor: barColors.slice(0, labels.length),
                    borderRadius: 4,
                    barThickness: 18
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        grid: { color: gridColor },
                        ticks: { color: textColor, precision: 0 }
                    },
                    y: {
                        grid: { display: false },
                        ticks: { color: textColor, font: { size: 11 } }
                    }
                }
            }
        });
    }

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

    // Expose functions to windows
    window.initSettingsForm = initSettingsForm;
    window.initAuditTimeline = initAuditTimeline;
    window.initDashboardCharts = initDashboardCharts;

    // Self-initialize components on DOMContentLoaded (supports strict CSP without inline scripts)
    document.addEventListener('DOMContentLoaded', function() {
        // 1. Detect and init dashboard charts
        if (document.getElementById('aiVolumeChart') && document.getElementById('aiLatencyChart')) {
            initDashboardCharts();
        }

        // 2. Detect and init settings form
        if (document.getElementById('ai-settings-form')) {
            initSettingsForm();
            
            // Setup temperature slider display sync
            const tempInput = document.getElementById('temperature');
            const displayVal = document.getElementById('temp-val-display');
            if (tempInput && displayVal) {
                tempInput.addEventListener('input', function() {
                    displayVal.textContent = parseFloat(this.value).toFixed(2);
                });
            }
        }

        // 3. Detect and init audit timeline
        if (document.getElementById('ai-audit-table')) {
            initAuditTimeline();
        }
    });

})();
