/**
 * AVAGuard Main JavaScript
 * Core functionality for sidebar, navigation, and global utilities
 */

(function() {
    'use strict';

    // Constants
    const STORAGE_KEY = 'avaguard_sidebar_collapsed';
    const MOBILE_BREAKPOINT = 991;

    /**
     * Initialize sidebar functionality
     */
    function initSidebar() {
        const sidebar = document.getElementById('sidebar');
        const toggle = document.getElementById('sidebarToggle');

        if (!sidebar || !toggle) return;

        // Load saved state
        const isCollapsed = localStorage.getItem(STORAGE_KEY) === 'true';
        if (isCollapsed) {
            sidebar.classList.add('collapsed');
        }

        // Toggle handler
        toggle.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            const nowCollapsed = sidebar.classList.contains('collapsed');
            localStorage.setItem(STORAGE_KEY, nowCollapsed);
        });

        // Handle responsive collapse
        function handleResize() {
            if (window.innerWidth <= MOBILE_BREAKPOINT) {
                sidebar.classList.add('collapsed');
            }
        }

        // Initial check
        handleResize();
        
        // Listen for resize
        window.addEventListener('resize', handleResize);

        // Mobile Menu Button Logic
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        if (mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', function() {
                sidebar.classList.toggle('mobile-open');
            });
        }
    }

    /**
     * Initialize tooltips for collapsed sidebar
     */
    function initTooltips() {
        const navItems = document.querySelectorAll('.nav-item[data-tooltip]');
        navItems.forEach(function(item) {
            item.addEventListener('mouseenter', function() {
                const sidebar = document.getElementById('sidebar');
                if (sidebar && sidebar.classList.contains('collapsed')) {
                    // Show tooltip
                    const tooltip = this.getAttribute('data-tooltip');
                    this.setAttribute('title', tooltip);
                }
            });
        });
    }

    /**
     * Initialize message auto-dismiss
     */
    function initMessages() {
        const messages = document.querySelectorAll('.message');
        messages.forEach(function(msg) {
            setTimeout(function() {
                msg.style.opacity = '0';
                msg.style.transform = 'translateY(-10px)';
                setTimeout(function() {
                    msg.remove();
                }, 300);
            }, 5000);
        });
    }

    /**
     * Format date utility
     */
    function formatDate(date, format) {
        const d = new Date(date);
        const options = { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' };
        return d.toLocaleDateString('en-US', options);
    }

    /**
     * Debounce utility
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = function() {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    /**
     * Toggle custom date inputs visibility
     */
    function toggleCustomDates(select) {
        const container = document.getElementById('customDates');
        if (!container) return;
        
        if (select.value === 'custom') {
            container.style.display = 'flex';
        } else {
            container.style.display = 'none';
            // Auto-submit for non-custom ranges
            select.form.submit();
        }
    }

    /**
     * Initialize Global Dropdown Menus
     */
    function initDropdowns() {
        // Function to close all open dropdowns
        function closeAllDropdowns(exceptToggle) {
            document.querySelectorAll('.avag-dropdown-container.active').forEach(function(container) {
                if (!exceptToggle || container !== exceptToggle.closest('.avag-dropdown-container')) {
                    container.classList.remove('active');
                    const toggle = container.querySelector('.avag-dropdown-toggle');
                    if (toggle) toggle.setAttribute('aria-expanded', 'false');
                    
                    const menu = container.querySelector('.avag-dropdown-menu');
                    if (menu) {
                        menu.style.position = '';
                        menu.style.top = '';
                        menu.style.bottom = '';
                        menu.style.right = '';
                        menu.style.transformOrigin = '';
                    }
                }
            });
        }

        document.addEventListener('click', function(e) {
            const isDropdownBtn = e.target.closest('.avag-dropdown-toggle');
            
            if (!e.target.closest('.avag-dropdown-menu')) {
                closeAllDropdowns(isDropdownBtn);
            }

            // Toggle clicked dropdown
            if (isDropdownBtn) {
                e.preventDefault();
                e.stopPropagation();
                const container = isDropdownBtn.closest('.avag-dropdown-container');
                const isActive = container.classList.contains('active');
                const menu = container.querySelector('.avag-dropdown-menu');
                
                if (isActive) {
                    closeAllDropdowns();
                } else {
                    container.classList.add('active');
                    isDropdownBtn.setAttribute('aria-expanded', 'true');
                    
                    // Portal / Floating Menu Rendering (Escapes overflow: hidden containers)
                    if (menu) {
                        const rect = isDropdownBtn.getBoundingClientRect();
                        const menuHeight = 160; // Estimated height of standard actions
                        
                        menu.style.position = 'fixed';
                        menu.style.right = (window.innerWidth - rect.right) + 'px';
                        
                        // Smart Positioning: Automatic upward opening if insufficient space below
                        if (rect.bottom + menuHeight > window.innerHeight && rect.top > menuHeight) {
                            // Drop UP
                            menu.style.top = 'auto';
                            menu.style.bottom = (window.innerHeight - rect.top + 4) + 'px';
                            menu.style.transformOrigin = 'bottom right';
                        } else {
                            // Drop DOWN
                            menu.style.bottom = 'auto';
                            menu.style.top = (rect.bottom + 4) + 'px';
                            menu.style.transformOrigin = 'top right';
                        }
                    }
                }
            }
        });

        // Close dropdowns on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeAllDropdowns();
            }
        });

        // Close dropdowns on scroll (Native behavior for fixed portals)
        document.addEventListener('scroll', function(e) {
            // Ignore scroll inside the menu itself
            if (e.target.closest && e.target.closest('.avag-dropdown-menu')) return;
            closeAllDropdowns();
        }, true); // Use capture phase to catch scrolls on all overflow containers
    }

    /**
     * Initialize everything on DOM ready
     */
    document.addEventListener('DOMContentLoaded', function() {
        initSidebar();
        initTooltips();
        initMessages();
        initDropdowns();
    });

    // Expose utilities globally
    window.AVAGuard = {
        formatDate: formatDate,
        debounce: debounce,
        toggleCustomDates: toggleCustomDates
    };

    // Also expose to global scope for easy access in inline onchange
    window.toggleCustomDates = toggleCustomDates;

})();
