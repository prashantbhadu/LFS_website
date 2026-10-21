/**
 * OUR LITTLE WORLD ❤️ — Interactive Romantic Script
 * Features:
 * 1. Background floating romantic particles (hearts & sparkles)
 * 2. Questions toggle with heart-burst effect
 * 3. Lightbox viewer for all romantic polaroids
 * 4. Ambient romantic music synthesizer / audio player with play/pause
 * 5. Mobile responsive navigation
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initParticles();
  initQuestionCards();
  initLightbox();
  initRomanticMusic();
});

/* ----------------------------------------------------
   1. Mobile Navigation
   ---------------------------------------------------- */
function initMobileNav() {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const navMenu = document.querySelector('.nav-menu');
  if (!toggleBtn || !navMenu) return;

  toggleBtn.addEventListener('click', () => {
    navMenu.classList.toggle('open');
    const isOpen = navMenu.classList.contains('open');
    toggleBtn.setAttribute('aria-expanded', isOpen);
  });
}

/* ----------------------------------------------------
   2. Floating Romantic Canvas Particles (Hearts & Sparkles)
   ---------------------------------------------------- */
function initParticles() {
  const canvas = document.getElementById('particles-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const particles = [];
  const particleCount = 28;
  let particlesEnabled = true;

  class HeartParticle {
    constructor() {
      this.reset();
    }
    reset() {
      this.x = Math.random() * width;
      this.y = height + Math.random() * 50;
      this.size = Math.random() * 14 + 10;
      this.speedY = Math.random() * 0.8 + 0.4;
      this.speedX = (Math.random() - 0.5) * 0.6;
      this.opacity = Math.random() * 0.45 + 0.25;
      this.rotation = Math.random() * Math.PI * 2;
      this.rotSpeed = (Math.random() - 0.5) * 0.02;
      this.symbol = Math.random() > 0.3 ? '🌸' : (Math.random() > 0.5 ? '✨' : '💕');
    }
    update() {
      this.y -= this.speedY;
      this.x += this.speedX;
      this.rotation += this.rotSpeed;
      if (this.y < -30) {
        this.reset();
      }
    }
    draw() {
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate(this.rotation);
      ctx.globalAlpha = this.opacity;
      ctx.font = `${this.size}px serif`;
      ctx.fillText(this.symbol, 0, 0);
      ctx.restore();
    }
  }

  for (let i = 0; i < particleCount; i++) {
    const p = new HeartParticle();
    p.y = Math.random() * height; // initial spread
    particles.push(p);
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);
    if (particlesEnabled) {
      for (let p of particles) {
        p.update();
        p.draw();
      }
    }
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);

  // Toggle button support
  const particleToggleBtn = document.getElementById('toggle-particles-btn');
  if (particleToggleBtn) {
    particleToggleBtn.addEventListener('click', () => {
      particlesEnabled = !particlesEnabled;
      particleToggleBtn.classList.toggle('active', particlesEnabled);
      particleToggleBtn.title = particlesEnabled ? "Disable floating hearts" : "Enable floating hearts";
    });
  }
}

/* ----------------------------------------------------
   3. Questions Accordion & Heart Burst Animation
   ---------------------------------------------------- */
function initQuestionCards() {
  const cards = document.querySelectorAll('.question-card');
  if (!cards.length) return;

  cards.forEach(card => {
    const header = card.querySelector('.question-header');
    if (!header) return;

    header.addEventListener('click', (e) => {
      const isAlreadyOpen = card.classList.contains('open');
      card.classList.toggle('open', !isAlreadyOpen);

      if (!isAlreadyOpen) {
        triggerHeartBurst(e.clientX || header.getBoundingClientRect().left + 40, e.clientY || header.getBoundingClientRect().top + 20);
      }
    });
  });
}

function triggerHeartBurst(clientX, clientY) {
  const symbols = ['❤️', '💖', '✨', '🌸', '💕', '💗'];
  const count = 12;

  for (let i = 0; i < count; i++) {
    const el = document.createElement('div');
    el.className = 'heart-burst-particle';
    el.textContent = symbols[Math.floor(Math.random() * symbols.length)];

    const angle = (Math.PI * 2 * i) / count + (Math.random() - 0.5) * 0.5;
    const distance = Math.random() * 80 + 50;
    const tx = `${Math.cos(angle) * distance}px`;
    const ty = `${Math.sin(angle) * distance}px`;

    el.style.setProperty('--tx', tx);
    el.style.setProperty('--ty', ty);
    el.style.left = `${clientX + window.scrollX}px`;
    el.style.top = `${clientY + window.scrollY}px`;

    document.body.appendChild(el);

    setTimeout(() => {
      el.remove();
    }, 1100);
  }
}

/* ----------------------------------------------------
   4. Polaroid Lightbox Viewer
   ---------------------------------------------------- */
function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  if (!modal) return;

  const modalImg = modal.querySelector('#lightbox-img');
  const modalCaption = modal.querySelector('#lightbox-caption');
  const closeBtn = modal.querySelector('.lightbox-close');

  function openLightbox(src, captionText) {
    if (!src) return;
    modalImg.src = src;
    modalCaption.textContent = captionText || '';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  // Attach to all images with class 'lightbox-trigger' or images in polaroid-image-box
  document.addEventListener('click', (e) => {
    const target = e.target;
    if (target.matches('.lightbox-trigger') || target.closest('.polaroid-image-box') || target.closest('.question-photo-box img') || target.closest('.timeline-photo-box img') || target.closest('.quality-photo-frame img')) {
      const img = target.tagName === 'IMG' ? target : target.querySelector('img');
      if (img && img.src) {
        const caption = img.getAttribute('data-caption') || img.alt || '';
        openLightbox(img.src, caption);
      }
    }
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeLightbox);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeLightbox();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeLightbox();
    }
  });
}

/* ----------------------------------------------------
   5. Romantic Ambient Music Box (Web Audio API Synthesizer)
   ---------------------------------------------------- */
function initRomanticMusic() {
  const musicBtn = document.getElementById('music-toggle-btn');
  if (!musicBtn) return;

  let isPlaying = false;
  let audioCtx = null;
  let timerId = null;

  // Sweet music box chord progression (Cmaj7 - G/B - Am7 - Fmaj7)
  const notes = [
    // Melody note frequencies (Hz)
    523.25, 659.25, 783.99, 987.77, 1046.50, // C5, E5, G5, B5, C6
    587.33, 698.46, 880.00, 1174.66          // D5, F5, A5, D6
  ];

  const melodySequence = [
    { note: 523.25, dur: 0.6 }, // C5
    { note: 659.25, dur: 0.6 }, // E5
    { note: 783.99, dur: 0.8 }, // G5
    { note: 987.77, dur: 1.0 }, // B5
    { note: 880.00, dur: 0.8 }, // A5
    { note: 659.25, dur: 0.6 }, // E5
    { note: 698.46, dur: 0.6 }, // F5
    { note: 783.99, dur: 1.2 }, // G5
    { note: 659.25, dur: 0.6 }, // E5
    { note: 523.25, dur: 0.6 }, // C5
    { note: 587.33, dur: 0.8 }, // D5
    { note: 523.25, dur: 1.4 }, // C5
  ];

  let currentNoteIndex = 0;

  function playChimeNote(freq, duration) {
    if (!audioCtx || audioCtx.state === 'closed') return;
    try {
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

      // Sweet bell-like chime envelope
      gain.gain.setValueAtTime(0, audioCtx.currentTime);
      gain.gain.linearRampToValueAtTime(0.08, audioCtx.currentTime + 0.04);
      gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration + 0.6);

      osc.connect(gain);
      gain.connect(audioCtx.destination);

      osc.start();
      osc.stop(audioCtx.currentTime + duration + 0.7);
    } catch (err) {
      console.warn("Audio chime error:", err);
    }
  }

  function stepMelody() {
    if (!isPlaying) return;
    const step = melodySequence[currentNoteIndex];
    playChimeNote(step.note, step.dur);

    // Also add gentle harmonic bass note occasionally
    if (currentNoteIndex % 4 === 0) {
      playChimeNote(step.note / 2, step.dur * 1.5);
    }

    currentNoteIndex = (currentNoteIndex + 1) % melodySequence.length;
    timerId = setTimeout(stepMelody, step.dur * 850);
  }

  function startMusic() {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) {
        audioCtx = new AudioContextClass();
      }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    isPlaying = true;
    musicBtn.classList.add('active');
    musicBtn.setAttribute('aria-label', 'Pause Romantic Music');
    musicBtn.innerHTML = '🎵';
    stepMelody();
  }

  function stopMusic() {
    isPlaying = false;
    if (timerId) clearTimeout(timerId);
    musicBtn.classList.remove('active');
    musicBtn.setAttribute('aria-label', 'Play Romantic Music');
    musicBtn.innerHTML = '🎶';
  }

  musicBtn.addEventListener('click', () => {
    if (isPlaying) {
      stopMusic();
    } else {
      startMusic();
    }
  });
}
