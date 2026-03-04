// Mobile Menu Toggle
function toggleMobileMenu() {
    const navCenter = document.getElementById('navCenter');
    const navRight = document.getElementById('navRight');
    const body = document.body;
    
    // Toggle both menus
    const isActive = navCenter.classList.contains('active');
    
    if (isActive) {
        navCenter.classList.remove('active');
        navRight.classList.remove('active');
        body.style.overflow = '';
        removeOverlay();
    } else {
        navCenter.classList.add('active');
        navRight.classList.add('active');
        body.style.overflow = 'hidden';
        createOverlay();
    }
}

// Close Mobile Menu
function closeMobileMenu() {
    const navCenter = document.getElementById('navCenter');
    const navRight = document.getElementById('navRight');
    const body = document.body;
    
    navCenter.classList.remove('active');
    navRight.classList.remove('active');
    body.style.overflow = '';
    removeOverlay();
    
    // Close all dropdowns
    document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
        dropdown.classList.remove('active');
    });
}

// Toggle Dropdown
function toggleDropdown(event) {
    if (window.innerWidth <= 768) {
        event.preventDefault();
        const dropdown = event.currentTarget.parentElement;
        dropdown.classList.toggle('active');
    }
}

// Create Overlay
function createOverlay() {
    if (!document.querySelector('.mobile-overlay')) {
        const overlay = document.createElement('div');
        overlay.className = 'mobile-overlay';
        overlay.onclick = closeMobileMenu;
        document.body.appendChild(overlay);
        setTimeout(() => overlay.classList.add('active'), 10);
    }
}

// Remove Overlay
function removeOverlay() {
    const overlay = document.querySelector('.mobile-overlay');
    if (overlay) {
        overlay.classList.remove('active');
        setTimeout(() => overlay.remove(), 300);
    }
}

// Close menu on window resize
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        closeMobileMenu();
    }
});

// Close menu on ESC key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeMobileMenu();
    }
});
