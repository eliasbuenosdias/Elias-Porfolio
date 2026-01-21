// Register ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Custom Cursor Logic
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
    cursorDot.style.left = `${mouseX}px`;
    cursorDot.style.top = `${mouseY}px`;
});

// Animation Loop for smooth cursor
function animateCursor() {
    // Linear interpolation (Lerp) for smoothness
    outlineX += (mouseX - outlineX) * 0.15;
    outlineY += (mouseY - outlineY) * 0.15;

    cursorOutline.style.left = `${outlineX}px`;
    cursorOutline.style.top = `${outlineY}px`;

    requestAnimationFrame(animateCursor);
}
animateCursor();

// Create Particle Trail
document.addEventListener('mousemove', (e) => {
    createParticle(e.clientX, e.clientY);
});

function createParticle(x, y) {
    if (Math.random() > 0.5) return; // Limit particles

    const particle = document.createElement('div');
    particle.classList.add('cursor-particle');
    document.body.appendChild(particle);

    // Random direction
    const destX = x + (Math.random() - 0.5) * 50;
    const destY = y + (Math.random() - 0.5) * 50;

    particle.style.left = `${x}px`;
    particle.style.top = `${y}px`;

    gsap.to(particle, {
        x: destX - x,
        y: destY - y,
        opacity: 0,
        scale: 0,
        duration: 0.5 + Math.random() * 0.5,
        onComplete: () => {
            particle.remove();
        }
    });
}

// Cursor Hover Effects
const hoverables = document.querySelectorAll('a, button, .project-card');

hoverables.forEach(el => {
    el.addEventListener('mouseenter', () => {
        gsap.to(cursorOutline, {
            scale: 1.5,
            backgroundColor: 'rgba(255, 255, 255, 0.1)',
            border: 'none',
            duration: 0.2
        });
    });

    el.addEventListener('mouseleave', () => {
        gsap.to(cursorOutline, {
            scale: 1,
            backgroundColor: 'transparent',
            border: '1px solid rgba(255, 255, 255, 0.5)',
            duration: 0.2
        });
    });
});

// Hero Animation
const tl = gsap.timeline();

tl.from('.hero-title .line', {
    y: 100,
    opacity: 0,
    duration: 1,
    stagger: 0.2,
    ease: 'power4.out',
    delay: 0.5
})
    .from('.hero-subtitle', {
        y: 20,
        opacity: 0,
        duration: 0.8,
        ease: 'power3.out'
    }, '-=0.5')
    .from('.cta-container .btn', {
        y: 20,
        opacity: 0,
        duration: 0.8,
        stagger: 0.1,
        ease: 'power3.out'
    }, '-=0.5')
    .from('.hero-visual', {
        scale: 0.8,
        opacity: 0,
        duration: 1.5,
        ease: 'power2.out'
    }, '-=1'); // Overlap with text animation

// Hover Reveal Animation
const revealContainer = document.querySelector('.reveal-image-container');
const revealImg = document.querySelector('.reveal-img');
const revealTriggers = document.querySelectorAll('.hover-reveal');

revealTriggers.forEach(trigger => {
    trigger.addEventListener('mouseenter', (e) => {
        const imgSrc = trigger.getAttribute('data-img');
        revealImg.src = imgSrc;

        gsap.to(revealContainer, {
            opacity: 1,
            scale: 1,
            rotation: Math.random() * 10 - 5, // Random tilt
            duration: 0.3,
            ease: 'power2.out'
        });
    });

    trigger.addEventListener('mouseleave', () => {
        gsap.to(revealContainer, {
            opacity: 0,
            scale: 0.8,
            duration: 0.3,
            ease: 'power2.in'
        });
    });

    // Image follows mouse
    trigger.addEventListener('mousemove', (e) => {
        gsap.to(revealContainer, {
            x: e.clientX + 20, // Offset
            y: e.clientY + 20,
            duration: 0.2, // Lag
            ease: 'power1.out'
        });
    });
});

// Scroll Animations for Sections
const sections = document.querySelectorAll('section');

sections.forEach(section => {
    // Avoid double animation for hero which uses timeline
    if (section.id === 'hero') return;

    gsap.from(section.children, {
        scrollTrigger: {
            trigger: section,
            start: 'top 80%',
            toggleActions: 'play none none reverse'
        },
        y: 50,
        opacity: 0,
        duration: 1,
        ease: 'power3.out',
        stagger: 0.2
    });
});

// Timeline Item Animation
gsap.utils.toArray('.timeline-item').forEach((item, i) => {
    gsap.from(item, {
        scrollTrigger: {
            trigger: item,
            start: 'top 85%',
        },
        x: -50,
        opacity: 0,
        duration: 0.8,
        ease: 'power2.out',
        delay: i * 0.1
    });
});
