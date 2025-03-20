// Select the canvas element and set up the context
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// Constants
const box = 20;
const canvasSize = 400;
canvas.width = canvasSize;
canvas.height = canvasSize;

// Snake and food
let snake = [{ x: box * 5, y: box * 5 }];
let food = { x: Math.floor(Math.random() * (canvasSize / box)) * box, y: Math.floor(Math.random() * (canvasSize / box)) * box };
let score = 0;
let direction = '';
let gameOverState = false;

// Game loop
function gameLoop() {
    if (gameOverState) {
        console.log('Game Over State: ', gameOverState);
        renderGameOver();
        return;
    }

    // Update snake position
    moveSnake();

    // Clear canvas
    ctx.clearRect(0, 0, canvasSize, canvasSize);

    // Draw food
    drawFood();

    // Draw snake
    drawSnake();

    // Draw score
    ctx.fillStyle = 'black';
    ctx.font = '20px Arial';
    ctx.fillText('Score: ' + score, box, box);

    setTimeout(gameLoop, 100);
}

// Movement function
function moveSnake() {
    const head = { ...snake[0] };

    if (direction === 'left') head.x -= box;
    if (direction === 'up') head.y -= box;
    if (direction === 'right') head.x += box;
    if (direction === 'down') head.y += box;

    if (head.x === food.x && head.y === food.y) {
        score += 1;
        food.x = Math.floor(Math.random() * (canvasSize / box)) * box;
        food.y = Math.floor(Math.random() * (canvasSize / box)) * box;
    } else {
        snake.pop(); // Remove last segment
    }

    if (gameOver()) {
        console.log('Game Over Triggered');
        gameOverState = true;
    }

    snake.unshift(head); // Add new head
}

// Check for game over
function gameOver() {
    const head = snake[0];
    const isCollision = head.x < 0 || head.x >= canvasSize || head.y < 0 || head.y >= canvasSize || snake.slice(1).some(segment => segment.x === head.x && segment.y === head.y);
    console.log('Collision Check: ', isCollision);
    return isCollision;
}

// Draw the food
function drawFood() {
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, box, box);
}

// Draw the snake
function drawSnake() {
    ctx.fillStyle = 'green';
    snake.forEach(segment => ctx.fillRect(segment.x, segment.y, box, box));
}

// Render game over screen
function renderGameOver() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.8)';
    ctx.fillRect(0, 0, canvasSize, canvasSize);
    ctx.fillStyle = 'white';
    ctx.font = '30px Arial';
    ctx.fillText('Game Over!', canvasSize / 4, canvasSize / 3);
    ctx.font = '20px Arial';
    ctx.fillText('Score: ' + score, canvasSize / 3, canvasSize / 2);
    ctx.fillText('Press R to Restart', canvasSize / 8, canvasSize * 2 / 3);
    ctx.fillText('Press Q to Quit', canvasSize / 8, canvasSize * 5 / 12);
}

// Restart game
function restartGame() {
    console.log('Restarting Game');
    snake = [{ x: box * 5, y: box * 5 }];
    food = { x: Math.floor(Math.random() * (canvasSize / box)) * box, y: Math.floor(Math.random() * (canvasSize / box)) * box };
    score = 0;
    direction = '';
    gameOverState = false;
    gameLoop();
}

// Handle keyboard input
window.addEventListener('keydown', (event) => {
    if (gameOverState) {
        console.log('Game Over: Key Pressed', event.key);
        if (event.key === 'r') restartGame();
        if (event.key === 'q') window.close();
        return;
    }

    if (event.key === 'ArrowLeft' && direction !== 'right') direction = 'left';
    if (event.key === 'ArrowUp' && direction !== 'down') direction = 'up';
    if (event.key === 'ArrowRight' && direction !== 'left') direction = 'right';
    if (event.key === 'ArrowDown' && direction !== 'up') direction = 'down';
});

gameLoop();