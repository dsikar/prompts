const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Set canvas size
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// Physics constants
const GRAVITY = 9.8;
const DENSITY = 1000;
const DRAG_COEFFICIENT = 0.47;
const RESTITUTION = 0.6;
const FRICTION = 0.3;

// Letter generation settings
const SPAWN_INTERVAL = 1000;
const MIN_SIZE = 20;
const MAX_SIZE = 40;
const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

class Letter {
    constructor(x, y, char, fontSize) {
        this.x = x;
        this.y = y;
        this.char = char;
        this.fontSize = fontSize;
        this.velocityX = (Math.random() - 0.5) * 2;
        this.velocityY = 0;
        this.rotation = Math.random() * Math.PI * 2;
        this.angularVelocity = (Math.random() - 0.5) * 0.1;
        
        const area = fontSize * fontSize;
        const volume = area * (fontSize / 10);
        this.mass = DENSITY * volume / 1000000;
    }

    update(dt) {
        // Apply gravity
        this.velocityY += GRAVITY * dt;

        // Apply drag force
        const dragForceX = 0.5 * DRAG_COEFFICIENT * this.velocityX * Math.abs(this.velocityX);
        const dragForceY = 0.5 * DRAG_COEFFICIENT * this.velocityY * Math.abs(this.velocityY);
        
        this.velocityX -= (dragForceX / this.mass) * dt;
        this.velocityY -= (dragForceY / this.mass) * dt;

        // Update position
        this.x += this.velocityX * dt * 50;
        this.y += this.velocityY * dt * 50;

        // Update rotation
        this.rotation += this.angularVelocity;

        // Screen boundary collision
        if (this.x < 0 || this.x > canvas.width) {
            this.velocityX *= -RESTITUTION;
            this.x = this.x < 0 ? 0 : canvas.width;
        }

        if (this.y > canvas.height - this.fontSize) {
            this.velocityY *= -RESTITUTION;
            this.y = canvas.height - this.fontSize;
            this.velocityX *= (1 - FRICTION);
        }
    }

    draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.rotation);
        ctx.font = `${this.fontSize}px Arial`;
        ctx.fillStyle = '#FFFFFF';
        ctx.fillText(this.char, -this.fontSize/3, this.fontSize/3);
        ctx.restore();
    }
}

// Letter management
const letters = [];
let lastSpawnTime = 0;

function spawnLetter() {
    const char = LETTERS[Math.floor(Math.random() * LETTERS.length)];
    const fontSize = MIN_SIZE + Math.random() * (MAX_SIZE - MIN_SIZE);
    const x = Math.random() * (canvas.width - fontSize);
    letters.push(new Letter(x, -fontSize, char, fontSize));
}

// Animation loop
let lastTime = performance.now();

function animate(currentTime) {
    const dt = (currentTime - lastTime) / 1000;
    lastTime = currentTime;

    // Clear canvas
    ctx.fillStyle = '#1a1a1a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Spawn new letters
    if (currentTime - lastSpawnTime >= SPAWN_INTERVAL) {
        spawnLetter();
        lastSpawnTime = currentTime;
    }

    // Update and draw letters
    for (let i = letters.length - 1; i >= 0; i--) {
        letters[i].update(dt);
        letters[i].draw();
        
        // Remove letters that are off screen
        if (letters[i].y > canvas.height + MAX_SIZE * 2) {
            letters.splice(i, 1);
        }
    }

    requestAnimationFrame(animate);
}

animate(performance.now());
