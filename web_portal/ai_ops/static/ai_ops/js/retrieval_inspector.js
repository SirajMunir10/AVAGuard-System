/**
 * AVAGuard AI Operations — RAG Retrieval Inspector Script
 */

document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    // DOM Elements
    const emptyState = document.getElementById('inspector-empty-state');
    const loadingState = document.getElementById('inspector-loading-state');
    const pipelineContainer = document.getElementById('inspector-pipeline-container');
    const queryForm = document.getElementById('inspect-query-form');
    const queryInput = document.getElementById('inspect-query-input');
    const submitBtn = document.getElementById('inspect-submit-btn');
    const submitSpinner = document.getElementById('inspect-spinner');
    const historyDropdown = document.getElementById('history-query-select');

    // Load recent queries to populate replay list
    loadQueryHistoryList();
    loadInspectorFrameworks();

    // Setup Lucide icons if available
    if (window.lucide) {
        window.lucide.createIcons();
    }

    // Toggle Stage collapsible behavior
    window.toggleStage = function(stageId) {
        const stage = document.getElementById(stageId);
        if (stage) {
            stage.classList.toggle('collapsed');
        }
    };

    // Load history helper
    function loadQueryHistoryList() {
        if (!historyDropdown) return;

        fetch('/api/ai/admin/audit/?page_size=20', {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            const results = data.results || [];
            historyDropdown.innerHTML = '<option value="">-- Choose Past Query --</option>';
            results.forEach(item => {
                const truncatedQuery = item.query_text.length > 50 
                    ? item.query_text.substring(0, 50) + '...' 
                    : item.query_text;
                const option = document.createElement('option');
                option.value = item.id;
                option.textContent = `${item.user_email}: ${truncatedQuery}`;
                historyDropdown.appendChild(option);
            });
        })
        .catch(err => console.error('Failed to load audit history for replay:', err));
    }

    // Run Live Inspection Profiler
    window.runLiveInspection = function(event) {
        event.preventDefault();
        const queryText = queryInput.value.trim();
        if (!queryText) return;

        showLoading();

        // Get CSRF Token
        let csrfToken = '';
        const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
        if (csrfInput) csrfToken = csrfInput.value;

        fetch('/api/ai/admin/inspect/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({
                query: queryText,
                framework: document.getElementById('inspect-framework-filter') ? document.getElementById('inspect-framework-filter').value : ''
            })
        })
        .then(async response => {
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || 'Failed to inspect query.');
            }
            return data;
        })
        .then(data => {
            renderInspectionData(data);
        })
        .catch(err => {
            showError(err.message || 'An error occurred during profiling.');
        });
    };

    // Load and replay historical query by ID
    window.loadHistoricalQuery = function(queryId) {
        if (!queryId) {
            resetInspector();
            return;
        }

        showLoading();

        fetch(`/api/ai/admin/inspect/?query_id=${queryId}`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(async response => {
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || 'Failed to fetch query logs.');
            }
            return data;
        })
        .then(data => {
            // Adapt query log format to match direct inspection format
            const adaptedData = {
                query: data.query,
                sanitized_query: data.sanitized_query,
                is_safe: true, // Safety violations aren't fully answered
                confidence: data.confidence,
                retrieval_ms: data.retrieval_ms,
                rerank_ms: data.rerank_ms,
                total_candidates: data.sources ? data.sources.length : 0,
                avg_reranker_score: data.avg_reranker_score || 0.0,
                top_reranker_score: data.top_reranker_score || 0.0,
                chunks: (data.sources || []).map((src, i) => {
                    const scoreDetail = (data.reranker_scores || [])[i] || {};
                    return {
                        filename: src.filename,
                        relative_path: src.relative_path || '',
                        word_count: src.word_count || 0,
                        hybrid_rank: scoreDetail.hybrid_rank || (i + 1),
                        reranker_score: src.score,
                        final_rank: scoreDetail.final_rank || (i + 1),
                        snippet: src.snippet || '',
                        metadata: src.metadata || {}
                    };
                }),
                generation: {
                    answer: data.response_text,
                    model: data.model_used,
                    tokens: data.token_count,
                    latency_ms: data.latency_ms
                }
            };
            
            // Set input value
            queryInput.value = data.query;
            renderInspectionData(adaptedData);
        })
        .catch(err => {
            showError(err.message || 'Failed to retrieve audit log details.');
        });
    };

    function showLoading() {
        emptyState.classList.add('avag-hide');
        pipelineContainer.classList.add('avag-hide');
        loadingState.classList.remove('avag-hide');
        
        submitBtn.setAttribute('disabled', 'disabled');
        submitSpinner.classList.remove('avag-hide');
    }

    function showError(message) {
        loadingState.classList.add('avag-hide');
        emptyState.classList.remove('avag-hide');
        submitBtn.removeAttribute('disabled');
        submitSpinner.classList.add('avag-hide');

        if (window.Toast) {
            window.Toast.error(message);
        } else {
            alert(message);
        }
    }

    function resetInspector() {
        emptyState.classList.remove('avag-hide');
        pipelineContainer.classList.add('avag-hide');
        loadingState.classList.add('avag-hide');
        submitBtn.removeAttribute('disabled');
        submitSpinner.classList.add('avag-hide');
        queryInput.value = '';
    }

    function renderInspectionData(data) {
        // Hide loading states
        loadingState.classList.add('avag-hide');
        pipelineContainer.classList.remove('avag-hide');
        submitBtn.removeAttribute('disabled');
        submitSpinner.classList.add('avag-hide');

        // Expand first three stages, collapse generation by default
        document.getElementById('stage-query').classList.remove('collapsed');
        document.getElementById('stage-retrieval').classList.remove('collapsed');
        document.getElementById('stage-reranking').classList.remove('collapsed');
        document.getElementById('stage-generation').classList.add('collapsed');

        // === 1. Render Stage 1: Query & Intent ===
        document.getElementById('val-raw-query').textContent = data.query;
        document.getElementById('val-sanitized-query').textContent = data.sanitized_query || data.query;
        document.getElementById('val-sanitization-latency').textContent = '0.45 ms'; // Fast regex sanitization
        
        const qTokens = Math.ceil((data.query || '').split(' ').length * 1.3);
        document.getElementById('val-query-tokens').textContent = `~${qTokens}`;

        const safetyBadge = document.getElementById('badge-intent-safety');
        if (data.is_safe !== false) {
            safetyBadge.className = 'stage-badge badge-success';
            safetyBadge.textContent = 'Safe';
        } else {
            safetyBadge.className = 'stage-badge badge-danger';
            safetyBadge.textContent = 'Flagged';
        }

        // === 2. Render Stage 2: Retrieval ===
        document.getElementById('badge-candidate-count').textContent = `${data.total_candidates} candidates`;
        document.getElementById('val-retrieval-latency').textContent = `${parseFloat(data.retrieval_ms || 0).toFixed(2)} ms`;
        
        // Detect embedding model from chunk metadata
        let embModel = 'BAAI/bge-base-en-v1.5';
        if (data.chunks && data.chunks.length > 0 && data.chunks[0].metadata && data.chunks[0].metadata.embedding_model) {
            embModel = data.chunks[0].metadata.embedding_model;
        }
        document.getElementById('val-embedding-model').textContent = embModel;

        // Build RRF rank table
        const tbody = document.getElementById('retrieval-tbody');
        tbody.innerHTML = '';

        if (!data.chunks || data.chunks.length === 0) {
            tbody.innerHTML = `<tr><td colspan="4" style="padding: 24px; text-align: center; color: var(--avag-text-secondary);">No documents retrieved. Knowledge base is empty or threshold was too high.</td></tr>`;
        } else {
            // Sort chunks by hybrid rank (RRF order) to show initial retrieval rank
            const sortedByHybrid = [...data.chunks].sort((a, b) => a.hybrid_rank - b.hybrid_rank);
            sortedByHybrid.forEach((chunk, i) => {
                const tr = document.createElement('tr');
                tr.style.borderBottom = '1px solid rgba(255, 255, 255, 0.04)';
                
                // Extract framework/category folder info from chunk
                let framework = chunk.metadata && chunk.metadata.framework ? chunk.metadata.framework : '--';
                let category = chunk.metadata && chunk.metadata.category ? chunk.metadata.category : '';
                let displayPath = category ? `${framework} (${category})` : framework;

                // Make a simplified RRF score mapping
                let rrfScore = (1 / (60 + (chunk.hybrid_rank || i + 1))).toFixed(5);

                tr.innerHTML = `
                    <td style="padding: 12px 16px;"><span class="badge-rank">#${chunk.hybrid_rank || i + 1}</span></td>
                    <td style="padding: 12px 16px; font-weight: 500; color: var(--avag-text-primary);">${chunk.filename}</td>
                    <td style="padding: 12px 16px; color: var(--avag-text-secondary);">${displayPath}</td>
                    <td style="padding: 12px 16px; font-family: monospace; color: var(--avag-accent-primary);">${rrfScore}</td>
                `;
                tbody.appendChild(tr);
            });
        }

        // === 3. Render Stage 3: Reranking ===
        const confBadge = document.getElementById('badge-confidence-level');
        const confidence = (data.confidence || 'none').toLowerCase();
        
        let confColor = 'badge-success';
        if (confidence === 'medium') confColor = 'badge-warning';
        else if (confidence === 'low') confColor = 'badge-danger';
        else if (confidence === 'none') confColor = 'badge-info';

        confBadge.className = `stage-badge ${confColor}`;
        confBadge.textContent = `${confidence} confidence`;

        document.getElementById('val-rerank-latency').textContent = `${parseFloat(data.rerank_ms || 0).toFixed(2)} ms`;
        document.getElementById('val-avg-relevance').textContent = parseFloat(data.avg_reranker_score || 0).toFixed(4);
        
        const passedCount = data.chunks ? data.chunks.filter(c => c.reranker_score >= 0.45).length : 0;
        document.getElementById('val-passed-count').textContent = `${passedCount} / ${data.chunks ? data.chunks.length : 0}`;

        // Build reranked chunks details
        const chunksContainer = document.getElementById('reranked-chunks-container');
        chunksContainer.innerHTML = '';

        if (!data.chunks || data.chunks.length === 0) {
            chunksContainer.innerHTML = `<div style="padding: 24px; text-align: center; color: var(--avag-text-secondary); border: 1px dashed var(--avag-border-color); border-radius: 8px;">No matching compliance vectors passed relevance thresholds.</div>`;
        } else {
            // Sort chunks by final_rank (Cross-Encoder score descending)
            const sortedByCE = [...data.chunks].sort((a, b) => a.final_rank - b.final_rank);
            sortedByCE.forEach((chunk, i) => {
                const chunkCard = document.createElement('div');
                chunkCard.style.padding = '18px';
                chunkCard.style.border = '1px solid var(--avag-border-color)';
                chunkCard.style.borderRadius = '8px';
                chunkCard.style.background = 'rgba(255, 255, 255, 0.01)';
                chunkCard.style.display = 'flex';
                chunkCard.style.flexDirection = 'column';
                chunkCard.style.gap = '10px';

                // Detect if it passed the threshold
                const passed = chunk.reranker_score >= 0.45;
                const statusBadge = passed 
                    ? '<span class="stage-badge badge-success" style="padding: 2px 6px;">PASSED</span>' 
                    : '<span class="stage-badge badge-danger" style="padding: 2px 6px;">FILTERED</span>';

                chunkCard.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                        <div style="display: flex; align-items: center; gap: 8px;">
                            <span class="badge-rank" style="background: rgba(0, 255, 136, 0.12); color: var(--avag-accent-success);">#${chunk.final_rank || i + 1}</span>
                            <span style="font-weight: 600; color: var(--avag-text-primary);">${chunk.filename}</span>
                            <span style="font-size: 11px; color: var(--avag-text-secondary);">(${chunk.word_count} words)</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 12px;">
                            <span style="font-size: 12px; color: var(--avag-text-secondary);">Initial Hybrid: <strong>#${chunk.hybrid_rank}</strong></span>
                            <span style="font-size: 12px; color: var(--avag-text-secondary);">CE Score: <strong style="color: var(--avag-accent-primary); font-family: monospace;">${parseFloat(chunk.reranker_score).toFixed(4)}</strong></span>
                            ${statusBadge}
                        </div>
                    </div>
                    <pre class="snippet-pre" style="max-height: 120px; overflow-y: auto; font-size: 13px;">${chunk.snippet}</pre>
                `;
                chunksContainer.appendChild(chunkCard);
            });
        }

        // === 4. Render Stage 4: Generation ===
        const genData = data.generation || {};
        
        let displayModel = genData.model || 'mock';
        if (displayModel === 'none' && passedCount === 0) {
            displayModel = 'No Generation (Skipped - Empty Knowledge Grounding)';
        }
        document.getElementById('val-generation-model').textContent = displayModel;

        const respTokens = genData.tokens || 0;
        document.getElementById('val-generation-tokens').textContent = respTokens > 0 ? respTokens : '--';

        const totalLatency = genData.latency_ms || (parseFloat(data.retrieval_ms || 0) + parseFloat(data.rerank_ms || 0) + 1200);
        document.getElementById('val-total-latency').textContent = `${(totalLatency / 1000).toFixed(2)} seconds`;

        const responseTextDiv = document.getElementById('val-generation-response');
        if (genData.answer) {
            responseTextDiv.innerHTML = formatMarkdownResponse(genData.answer);
            document.getElementById('badge-generation-status').className = 'stage-badge badge-success';
            document.getElementById('badge-generation-status').textContent = 'Success';
        } else if (passedCount === 0) {
            responseTextDiv.textContent = "I don't have sufficient information in my knowledge base to answer this question confidently. (Safe fallback bypass active).";
            document.getElementById('badge-generation-status').className = 'stage-badge badge-warning';
            document.getElementById('badge-generation-status').textContent = 'Bypassed';
        } else {
            responseTextDiv.textContent = "LLM generation details not available in inspection view. Replay an audit log query or use deepseek/openai configuration to generate full responses.";
            document.getElementById('badge-generation-status').className = 'stage-badge badge-info';
            document.getElementById('badge-generation-status').textContent = 'Ready';
        }

        // Trigger Lucide to render icons inside new cards
        if (window.lucide) {
            window.lucide.createIcons();
        }
    }

    // Quick regex-based Markdown text formatter
    function formatMarkdownResponse(text) {
        if (!text) return '';
        let html = text
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
        
        // Headers
        html = html.replace(/^### (.*?)$/gm, '<h5 style="margin-top: 16px; margin-bottom: 8px; font-weight: 600; color: var(--avag-text-primary);">$1</h5>');
        html = html.replace(/^## (.*?)$/gm, '<h4 style="margin-top: 20px; margin-bottom: 10px; font-weight: 700; color: var(--avag-text-primary);">$1</h4>');
        
        // Bold
        html = html.replace(/\*\*(.*?)\*\*/g, '<strong style="color: var(--avag-text-primary);">$1</strong>');
        
        // Inline code
        html = html.replace(/`(.*?)`/g, '<code style="font-family: monospace; background: rgba(255,255,255,0.06); padding: 2px 6px; border-radius: 4px; color: var(--avag-accent-primary);">$1</code>');
        
        // Lists
        html = html.replace(/^\- (.*?)$/gm, '<li style="margin-left: 16px; list-style-type: disc; margin-bottom: 4px;">$1</li>');
        
        // Paragraphs (breaks)
        html = html.replace(/\n\n/g, '<br><br>');
        
        return html;
    }

    // Load available frameworks for the inspector dropdown
    function loadInspectorFrameworks() {
        const select = document.getElementById('inspect-framework-filter');
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
        .catch(() => {});
    }

    // Auto-replay query if query_id is in URL query parameters
    const urlParams = new URLSearchParams(window.location.search);
    const queryIdParam = urlParams.get('query_id');
    if (queryIdParam) {
        setTimeout(() => {
            window.loadHistoricalQuery(queryIdParam);
        }, 150);
    }
});
