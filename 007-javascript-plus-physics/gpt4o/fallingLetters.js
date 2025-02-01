const canvas = document.getElementById('falling-letters');
const ctx = canvas.getContext('2d');
const GRAVITY = 9.8; // Earth's gravity (m/s²)
const DENSITY = 1; // Density similar to water (arbitrary unit)

let letters = [];
let screenWidth, screenHeight;

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
const fontSizeRange = [20, 40]; // Size range for the letters

// Adjust the canvas size when the window resizes
window.addEventListener('resize', resizeCanvas);

function resizeCanvas() {
    screenWidth = window.innerWidth;
    screenHeight = window.innerHeight;
    canvas.width = screenWidth;
    canvas.height = screenHeight;
}

resizeCanvas();

// Helper function to generate a random letter
function randomLetter() {
    const index = Math.floor(Math.random() * alphabet.length);
    return alphabet[index];
}

// Class to represent each falling letter
class FallingLetter {
    constructor() {
        this.x = Math.random() * screenWidth; // Random horizontal position
        this.y = 0; // Start at the top
        this.dy = Math.random() * 3 + 1; // Random fall speed
        this.dx = Math.random() * 2 - 1; // Random horizontal drift
        this.size = Math.random() * (fontSizeRange[1] - fontSizeRange[0]) + fontSizeRange[0]; // Random size
        this.angle = Math.random() * 0.2 - 0.1; // Small random rotation angle
        this.letter = randomLetter(); // Random letter
        this.color = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`; // Random color
    }

    // Draw the letter at its current position
    draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);
        ctx.font = `${this.size}px sans-serif`;
        ctx.fillStyle = this.color;
        ctx.fillText(this.letter, 0, 0);
        ctx.restore();
    }

    // Update the position of the letter
    update() {
        // Gravity and drift effects
        this.dy += GRAVITY * DENSITY * 0.01; // Apply gravity
        this.x += this.dx;
        this.y += this.dy;

        // Collision detection: if the letter hits the bottom of the screen
        if (this.y + this.size > screenHeight) {
            this.dy = -this.dy * 0.8; // Reverse direction and reduce speed (bounce effect)
            this.y = screenHeight - this.size; // Ensure it's not going off-screen
        }

        // Collision with the sides of the screen
        if (this.x < 0 || this.x + this.size > screenWidth) {
            this.dx = -this.dx; // Reverse horizontal direction
        }

        // Randomize the angle to simulate wobble effect
        this.angle += Math.random() * 0.02 - 0.01;
    }
}

// Add a new letter to the falling letters array at regular intervals
function createLetter() {
    const letter = new FallingLetter();
    letters.push(letter);
}

// Main animation loop
function animate() {
    ctx.clearRect(0, 0, screenWidth, screenHeight); // Clear canvas

    // Create new letters randomly
    if (Math.random() < 0.1) {
        createLetter();
    }

    // Update and draw each letter
    letters.forEach((letter, index) => {
        letter.update();
        letter.draw();

        // Remove letter if it's out of the screen
        if (letter.y > screenHeight + letter.size) {
            letters.splice(index, 1);
        }
    });

    // Request the next frame
    requestAnimationFrame(animate);
}

// Start the animation
animate();

