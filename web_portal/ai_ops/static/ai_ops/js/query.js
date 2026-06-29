/**
 * AVAGuard AI Compliance Assistant — User Query Script
 */

(function() {
    'use strict';

    // DOM Elements
    const queryForm = document.getElementById('ai-query-form');
    const queryInput = document.getElementById('ai-query-input');
    const charCount = document.getElementById('char-count');
    const submitBtn = document.getElementById('ai-submit-btn');
    const btnSpinner = document.getElementById('ai-btn-spinner');
    const responseBoard = document.getElementById('ai-response-board');
    const sidebarHistoryList = document.getElementById('ai-sidebar-history-list');

    // Modals DOM
    const sourceModalContainer = document.getElementById('ai-source-modal-container');
    const sourceTitle = document.getElementById('ai-source-title');
    const sourceScore = document.getElementById('ai-source-score');
    const sourceSnippet = document.getElementById('ai-source-snippet');

    if (!queryForm || !queryInput) return;

    // ── 1. Textarea Character Counter ──
    queryInput.addEventListener('input', function() {
        const len = this.value.length;
        charCount.textContent = len;
        
        if (len >= 2000) {
            charCount.style.color = 'var(--avag-accent-danger)';
        } else {
            charCount.style.color = '';
        }
    });

    // ── 2. Query Form Submission Handler ──
    queryForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const queryText = queryInput.value.trim();
        if (!queryText) return;

        // Loading state
        setLoadingState(true);

        // Fetch CSRF Token
        let csrfToken = '';
        const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
        if (csrfInput) {
            csrfToken = csrfInput.value;
        }

        // AJAX POST request
        fetch('/api/ai/query/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({
                query: queryText,
                top_k: 5,
                framework: document.getElementById('ai-framework-filter') ? document.getElementById('ai-framework-filter').value : ''
            })
        })
        .then(async response => {
            let data = {};
            try {
                const contentType = response.headers.get('content-type');
                if (contentType && contentType.includes('application/json')) {
                    data = await response.json();
                } else {
                    data = { error: 'Non-JSON server response returned.' };
                }
            } catch (e) {
                data = { error: 'Malformed response returned.' };
            }

            if (!response.ok) {
                throw { status: response.status, message: data.error || 'Request failed.' };
            }
            return data;
        })
        .then(data => {
            // Success response
            handleQuerySuccess(queryText, data);
        })
        .catch(err => {
            // Handle error UX
            handleQueryError(err);
        })
        .finally(() => {
            setLoadingState(false);
        });
    });

    // Loading UX toggle
    function setLoadingState(isLoading) {
        if (isLoading) {
            submitBtn.setAttribute('disabled', 'disabled');
            queryInput.setAttribute('disabled', 'disabled');
            btnSpinner.classList.remove('avag-hide');
        } else {
            submitBtn.removeAttribute('disabled');
            queryInput.removeAttribute('disabled');
            btnSpinner.classList.add('avag-hide');
        }
    }

    // Success response handler
    function handleQuerySuccess(queryText, data) {
        // Enforce structural data validation
        if (!data || typeof data.answer !== 'string' || typeof data.model_used !== 'string') {
            handleQueryError({ status: 500, message: 'Grounded generation returned a malformed response envelope.' });
            return;
        }

        // Clear textarea
        queryInput.value = '';
        charCount.textContent = '0';

        // Hide welcome placeholder
        const placeholder = document.getElementById('ai-response-placeholder');
        if (placeholder) {
            placeholder.style.display = 'none';
        }

        // Construct dynamic Q&A Card
        const cardId = 'query-card-' + data.query_id;
        const isFallback = data.model_used === 'mock' || !data.sources || data.sources.length === 0;

        // Confidence level badge (🟢🟡🟠🔴)
        let confBadgeHtml = '';
        const confidence = (data.confidence || 'none').toLowerCase();
        if (confidence === 'high') {
            confBadgeHtml = `<span class="ai-badge" style="background: rgba(0, 255, 136, 0.12); color: var(--avag-accent-success, #00ff88); border: 1px solid rgba(0, 255, 136, 0.2);"><span class="confidence-dot dot-high" style="width:6px; height:6px; border-radius:50%; display:inline-block; margin-right:4px; background:var(--avag-accent-success, #00ff88);"></span>High Match</span>`;
        } else if (confidence === 'medium') {
            confBadgeHtml = `<span class="ai-badge" style="background: rgba(255, 217, 61, 0.12); color: var(--avag-accent-warning, #ffd93d); border: 1px solid rgba(255, 217, 61, 0.2);"><span class="confidence-dot dot-medium" style="width:6px; height:6px; border-radius:50%; display:inline-block; margin-right:4px; background:var(--avag-accent-warning, #ffd93d);"></span>Medium Match</span>`;
        } else if (confidence === 'low') {
            confBadgeHtml = `<span class="ai-badge" style="background: rgba(255, 75, 75, 0.12); color: #ff4b4b; border: 1px solid rgba(255, 75, 75, 0.2);"><span class="confidence-dot dot-low" style="width:6px; height:6px; border-radius:50%; display:inline-block; margin-right:4px; background:#ff4b4b;"></span>Low Match</span>`;
        } else {
            confBadgeHtml = `<span class="ai-badge" style="background: rgba(255, 255, 255, 0.05); color: var(--avag-text-secondary, #808080); border: 1px solid rgba(255, 255, 255, 0.1);"><span class="confidence-dot dot-none" style="width:6px; height:6px; border-radius:50%; display:inline-block; margin-right:4px; background:var(--avag-text-secondary, #808080);"></span>No Match</span>`;
        }

        let sourcesHtml = '';
        if (data.sources && data.sources.length > 0) {
            sourcesHtml = `
                <div class="ai-query-sources">
                    <span class="ai-sources-label">
                        <i data-lucide="bookmark-check"></i> Grounded Citations:
                    </span>
                    <div class="ai-sources-list">
            `;
            
            data.sources.forEach(src => {
                const fwName = (src.metadata && src.metadata.framework) ? src.metadata.framework : '';
                const fwBadge = fwName ? `<span class="ai-fw-badge ai-fw-${fwName.toLowerCase().replace(/[^a-z0-9]/g, '')}" title="Framework: ${escapeHtml(fwName)}">${escapeHtml(fwName)}</span>` : '';
                sourcesHtml += `
                    <button class="ai-source-badge" 
                            data-filename="${escapeHtml(src.filename)}" 
                            data-score="${src.score}" 
                            data-snippet="${escapeHtml(src.snippet)}"
                            title="Reranker Score: ${parseFloat(src.score).toFixed(4)}">
                        ${fwBadge}
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

        const cardHtml = `
            <div class="ai-query-card ${isFallback ? 'fallback' : ''}" id="${cardId}">
                <div class="ai-card-header">
                    <div class="ai-user-meta">
                        <span class="ai-user-email">
                            <i data-lucide="user" class="ai-meta-icon"></i>
                            You
                        </span>
                        <span class="ai-timestamp">
                            <i data-lucide="clock" class="ai-meta-icon"></i>
                            Just now
                        </span>
                    </div>
                    <div class="ai-badges">
                        ${data.mode === 'mock' ? `
                            <span class="ai-badge" style="background:#d97706; color:white;">
                                <i data-lucide="shield-alert"></i> MOCK
                            </span>
                        ` : `
                            <span class="ai-badge" style="background:#16a34a; color:white;">
                                <i data-lucide="cpu"></i> AI
                            </span>
                        `}
                        ${confBadgeHtml}
                        <span class="ai-badge ai-badge-info">
                            <i data-lucide="server"></i> ${escapeHtml(data.model_used)}
                        </span>
                        <span class="ai-badge ai-badge-success">
                            <i data-lucide="gauge"></i> ${Math.round(data.latency_ms)}ms
                        </span>
                    </div>
                </div>
                <div class="ai-card-body">
                    <div class="ai-query-question">
                        <span class="ai-q-indicator">Q</span>
                        <p class="ai-question-text">${escapeHtml(queryText)}</p>
                    </div>
                    
                    <div class="ai-query-answer">
                        <span class="ai-a-indicator">A</span>
                        <div class="ai-answer-text">${data.answer.replace(/\n/g, '<br>')}</div>
                    </div>
                    
                    <div class="ai-card-actions">
                        <div class="ai-feedback-group" data-query-id="${data.query_id}">
                            <button class="ai-feedback-btn ai-fb-up" data-rating="up" title="Helpful answer">
                                <i data-lucide="thumbs-up"></i>
                            </button>
                            <button class="ai-feedback-btn ai-fb-down" data-rating="down" title="Not helpful">
                                <i data-lucide="thumbs-down"></i>
                            </button>
                        </div>
                        <button class="ai-copy-btn" title="Copy answer to clipboard">
                            <i data-lucide="copy"></i> Copy
                        </button>
                    </div>

                    ${sourcesHtml}
                </div>
            </div>
        `;

        // Prepend card so the latest is on top
        responseBoard.insertAdjacentHTML('afterbegin', cardHtml);

        // Bind citations click events
        const cardEl = document.getElementById(cardId);
        bindCitationsClickEvents(cardEl);

        // Bind feedback buttons
        bindFeedbackButtons(cardEl);

        // Bind copy button
        bindCopyButton(cardEl, data.answer);

        // Re-run Lucide icons
        lucide.createIcons();

        // Show Success Toast
        if (window.Toast) {
            window.Toast.success('Compliance analysis completed.');
        }

        // Refresh sidebar query log history
        fetchRecentQueries();
    }

    // Handles error and triggers Toast.error alerts
    function handleQueryError(err) {
        let msg = 'AI Compliance system encountered a network failure.';
        
        if (!navigator.onLine) {
            msg = 'Network connection lost. Please check your internet connectivity and try again.';
        } else if (err instanceof TypeError || err.message === 'Failed to fetch') {
            msg = 'Unable to establish a secure connection to the AVAGuard AI service. Please verify your connection.';
        } else if (err.status) {
            if (err.status === 429) {
                msg = err.message || 'Rate limit exceeded. Please wait a minute before querying again.';
            } else if (err.status === 400) {
                msg = err.message || 'Your query was rejected by our safety filters.';
            } else if (err.status === 403) {
                msg = err.message || 'AI compliance features are unconfigured or disabled for your organization.';
            } else if (err.status === 401) {
                msg = 'Your session has expired or is unauthorized. Please refresh the portal and log in again.';
            } else if (err.status === 504 || err.status === 502 || err.status === 503) {
                msg = 'Timeout: The backing LLM provider is currently unreachable or timed out. Please try again.';
            } else if (err.status >= 500) {
                msg = err.message || 'AVAGuard internal compliance generator error occurred. Gracefully falling back.';
            }
        } else if (err.message) {
            msg = err.message;
        }

        if (window.Toast) {
            window.Toast.error(msg);
        } else {
            console.error('[AI Error]', msg, err);
        }
    }

    // ── 3. Source Citation Modal Management ──
    function bindCitationsClickEvents(container) {
        if (!container) return;
        const badges = container.querySelectorAll('.ai-source-badge');
        badges.forEach(badge => {
            badge.addEventListener('click', function() {
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
        if (!sourceModalContainer) return;
        sourceModalContainer.classList.remove('visible');
        const cardModal = document.getElementById('ai-card-view-modal-container');
        if (!cardModal || !cardModal.classList.contains('visible')) {
            document.body.style.overflow = '';
        }
    }

    // Expose functions globally for close clicks
    window.openSourceModal = openSourceModal;
    window.closeSourceModal = closeSourceModal;

    // ── 4. Sidebar History Listing Loading ──
    function fetchRecentQueries() {
        if (!sidebarHistoryList) return;

        fetch('/api/ai/history/?page=1', {
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
            renderSidebarHistory(data.results || []);
        })
        .catch(() => {
            sidebarHistoryList.innerHTML = `
                <div style="padding: 16px; font-size: 12px; color: var(--avag-text-muted); text-align: center;">
                    Failed to sync recent log timeline.
                </div>
            `;
        });
    }

    function renderSidebarHistory(logs) {
        if (logs.length === 0) {
            sidebarHistoryList.innerHTML = `
                <div style="padding: 16px; font-size: 12px; color: var(--avag-text-muted); text-align: center;">
                    No recent compliance queries.
                </div>
            `;
            return;
        }

        let html = '';
        // Only show last 6 queries
        logs.slice(0, 6).forEach(log => {
            const dateStr = formatDate(log.created_at);
            html += `
                <div class="ai-sidebar-item" data-id="${log.id}" data-log='${JSON.stringify(log).replace(/'/g, "&apos;")}'>
                    <div class="ai-sidebar-item-q">${escapeHtml(log.query_text)}</div>
                    <div class="ai-sidebar-item-meta">
                        <span>${escapeHtml(log.model_used)}</span>
                        <span>${dateStr}</span>
                    </div>
                </div>
            `;
        });

        sidebarHistoryList.innerHTML = html;

        // Bind click events on sidebar items to show record modal
        const items = sidebarHistoryList.querySelectorAll('.ai-sidebar-item');
        items.forEach(item => {
            item.addEventListener('click', function() {
                const logData = JSON.parse(this.getAttribute('data-log'));
                showAuditLogCardModal(logData);
            });
        });
    }

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
                            ${escapeHtml(log.user_email || 'User')}
                        </span>
                        <span class="ai-timestamp">
                            <i data-lucide="clock" class="ai-meta-icon"></i>
                            ${formatDate(log.created_at)}
                        </span>
                    </div>
                    <div class="ai-badges">
                        ${log.mode === 'mock' ? `
                            <span class="ai-badge" style="background:#d97706; color:white;">
                                <i data-lucide="shield-alert"></i> MOCK
                            </span>
                        ` : `
                            <span class="ai-badge" style="background:#16a34a; color:white;">
                                <i data-lucide="cpu"></i> AI
                            </span>
                        `}
                        ${(function() {
                            const confidence = (log.confidence_level || 'none').toLowerCase();
                            if (confidence === 'high') {
                                return `<span class="ai-badge" style="background: rgba(0, 255, 136, 0.12); color: var(--avag-accent-success, #00ff88); border: 1px solid rgba(0, 255, 136, 0.2);"><span class="confidence-dot dot-high" style="width:6px; height:6px; border-radius:50%; display:inline-block; margin-right:4px; background:var(--avag-accent-success, #00ff88);"></span>High Match</span>`;
                            } else if (confidence === 'medium') {
                                return `<span class="ai-badge" style="background: rgba(255, 217, 61, 0.12); color: var(--avag-accent-warning, #ffd93d); border: 1px solid rgba(255, 217, 61, 0.2);"><span class="confidence-dot dot-medium" style="width:6px; height:6px; border-radius:50%; display:inline-block; margin-right:4px; background:var(--avag-accent-warning, #ffd93d);"></span>Medium Match</span>`;
                            } else if (confidence === 'low') {
                                return `<span class="ai-badge" style="background: rgba(255, 75, 75, 0.12); color: #ff4b4b; border: 1px solid rgba(255, 75, 75, 0.2);"><span class="confidence-dot dot-low" style="width:6px; height:6px; border-radius:50%; display:inline-block; margin-right:4px; background:#ff4b4b;"></span>Low Match</span>`;
                            } else {
                                return `<span class="ai-badge" style="background: rgba(255, 255, 255, 0.05); color: var(--avag-text-secondary, #808080); border: 1px solid rgba(255, 255, 255, 0.1);"><span class="confidence-dot dot-none" style="width:6px; height:6px; border-radius:50%; display:inline-block; margin-right:4px; background:var(--avag-text-secondary, #808080);"></span>No Match</span>`;
                            }
                        })()}
                        ${log.flagged ? `
                            <span class="ai-badge ai-badge-danger">
                                <i data-lucide="shield-alert"></i> Flagged
                            </span>
                        ` : `
                            <span class="ai-badge ai-badge-info">
                                <i data-lucide="server"></i> ${escapeHtml(log.model_used)}
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
        if (!sourceModalContainer || !sourceModalContainer.classList.contains('visible')) {
            document.body.style.overflow = '';
        }
    }

    window.closeCardModal = closeCardModal;

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
        if (!isoStr) return 'Just now';
        try {
            const date = new Date(isoStr);
            return date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) + ' ' +
                   date.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit', hour12: false });
        } catch (e) {
            return isoStr;
        }
    }

    // ── Feedback Buttons ──
    function bindFeedbackButtons(cardEl) {
        const group = cardEl.querySelector('.ai-feedback-group');
        if (!group) return;

        const queryId = group.dataset.queryId;
        const buttons = group.querySelectorAll('.ai-feedback-btn');

        buttons.forEach(btn => {
            btn.addEventListener('click', function() {
                const rating = this.dataset.rating;
                const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
                const csrfToken = csrfInput ? csrfInput.value : '';

                // Disable all feedback buttons in this group
                buttons.forEach(b => {
                    b.classList.add('ai-fb-disabled');
                    b.setAttribute('disabled', 'disabled');
                });
                this.classList.add('ai-fb-selected');

                fetch('/api/ai/feedback/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest'
                    },
                    body: JSON.stringify({ query_id: queryId, rating: rating })
                })
                .then(res => res.json())
                .then(data => {
                    if (window.Toast) {
                        window.Toast.success(rating === 'up' ? 'Thanks for the feedback!' : 'Feedback noted. We\'ll improve.');
                    }
                })
                .catch(() => {
                    if (window.Toast) {
                        window.Toast.error('Failed to submit feedback.');
                    }
                    // Re-enable on failure
                    buttons.forEach(b => {
                        b.classList.remove('ai-fb-disabled', 'ai-fb-selected');
                        b.removeAttribute('disabled');
                    });
                });
            });
        });
    }

    // ── Copy to Clipboard ──
    function bindCopyButton(cardEl, answerText) {
        const copyBtn = cardEl.querySelector('.ai-copy-btn');
        if (!copyBtn) return;

        copyBtn.addEventListener('click', function() {
            navigator.clipboard.writeText(answerText).then(() => {
                this.innerHTML = '<i data-lucide="check"></i> Copied';
                this.classList.add('ai-copy-done');
                lucide.createIcons();
                setTimeout(() => {
                    this.innerHTML = '<i data-lucide="copy"></i> Copy';
                    this.classList.remove('ai-copy-done');
                    lucide.createIcons();
                }, 2000);
            }).catch(() => {
                if (window.Toast) window.Toast.error('Copy failed.');
            });
        });
    }

    // ── Load Framework Options ──
    function loadFrameworks() {
        const select = document.getElementById('ai-framework-filter');
        if (!select) return;

        fetch('/api/ai/admin/stats/', {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(res => res.json())
        .then(data => {
            const frameworks = data.available_frameworks || [];
            frameworks.forEach(fw => {
                const opt = document.createElement('option');
                opt.value = fw;
                opt.textContent = fw;
                select.appendChild(opt);
            });
        })
        .catch(() => {
            // Silently fail — dropdown defaults to "All Frameworks"
        });
    }

    // Sync on page load inside DOMContentLoaded to support strict CSP (no inline scripts)
    document.addEventListener('DOMContentLoaded', function() {
        lucide.createIcons();
        fetchRecentQueries();
        loadFrameworks();
    });

})();
