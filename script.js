// Register ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Custom Cursor Logic (Kept Simple)
const cursorDot = document.querySelector('.cursor-dot');
const cursorOutline = document.querySelector('.cursor-outline');

// Mouse position
let mouseX = 0;
let mouseY = 0;

// Cursor Outline position (for smooth lag)
let outlineX = 0;
let outlineY = 0;

window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;

    // Dot follows instantly
    if (cursorDot) {
        cursorDot.style.left = `${mouseX}px`;
        cursorDot.style.top = `${mouseY}px`;
    }
});

// Animation Loop for smooth cursor
function animateCursor() {
    if (!cursorOutline) return;

    // Linear interpolation (Lerp) for smoothness
    outlineX += (mouseX - outlineX) * 0.15;
    outlineY += (mouseY - outlineY) * 0.15;

    cursorOutline.style.left = `${outlineX}px`;
    cursorOutline.style.top = `${outlineY}px`;

    requestAnimationFrame(animateCursor);
}
animateCursor();


// Sidebar Active State on Scroll
const sections = document.querySelectorAll('.content-section');
const navLinks = document.querySelectorAll('.sidebar-nav a');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        // Logic to highlight link when section is in middle of viewport
        if (pageYOffset >= (sectionTop - window.innerHeight / 2)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').includes(current)) {
            link.classList.add('active');
        }
    });
});

// Reveal Animations for Main Content
gsap.utils.toArray('.content-section').forEach(section => {
    // Animate children elements
    const elements = section.querySelectorAll('h2, .line, p, .exp-row, .gallery-item, .skill-box');

    gsap.from(elements, {
        scrollTrigger: {
            trigger: section,
            start: 'top 80%',
        },
        y: 30,
        opacity: 0,
        duration: 0.8,
        stagger: 0.05,
        ease: 'power2.out'
    });
});
