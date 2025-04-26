//index.js

const hamburger = document.getElementById('hamburger'); 
const menu = document.querySelector('.menu'); 

hamburger.addEventListener('click', function () { 
    const hamIcon = this.querySelector('.hamburger-icon'); 
    const crossIcon = this.querySelector('.cross-icon'); 

    // Toggle classes for visibility instead of inline styles
    hamIcon.classList.toggle('hidden');
    crossIcon.classList.toggle('hidden');
    menu.classList.toggle('menu-open');
});