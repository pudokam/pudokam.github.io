/*
	CUSTOM.JS - NAVIGATION ACTIVE LINK HIGHLIGHTER

	This script runs on every page and highlights the current page link
	in the top navigation. It reads the current pathname and compares it
	to each nav item href, then adds the 'active' class to the matching link.
*/

(function() {
	
	// Set the active nav link based on current page
	const currentPage = window.location.pathname.split('/').pop() || 'index.html';
	const navLinks = document.querySelectorAll('#nav-top a.nav-link');
	
	navLinks.forEach(link => {
		link.classList.remove('active');
		const href = link.getAttribute('href');
		
		// Check if this link matches the current page
		if (href === currentPage || (currentPage === '' && href === 'index.html')) {
			link.classList.add('active');
		}
	});
	
	// Add a mobile nav toggle button if the header nav exists.
	const navTop = document.getElementById('nav-top');
	if (navTop) {
		const toggleButton = document.createElement('button');
		toggleButton.id = 'nav-toggle';
		toggleButton.type = 'button';
		toggleButton.setAttribute('aria-label', 'Toggle navigation');
		toggleButton.setAttribute('aria-expanded', 'false');
		toggleButton.innerHTML = '<span class="nav-toggle-icon"></span><span class="nav-toggle-text">Menu</span>';
		navTop.parentNode.insertBefore(toggleButton, navTop);
	
		toggleButton.addEventListener('click', () => {
			const isOpen = navTop.classList.toggle('open');
			toggleButton.setAttribute('aria-expanded', String(isOpen));
		});
	}
})();

