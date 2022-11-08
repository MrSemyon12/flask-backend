const GRID_SIZE = 20;
const BG_COLOUR = "#231f20";
const SNAKE_COLOUR = "#c2c2c2";
const FOOD_COLOUR = "#e66916";
const FRAME_RATE = 10;

let canvas, ctx;
let gameActive = "";

let localData = {
  last_score: [],
  best_score: 3,
};

ls = JSON.parse(localStorage.getItem("localData"));
if (ls != null) localData = ls;
console.log(localData);

let player = {
  pos: {
    x: 3,
    y: 10,
  },
  vel: {
    x: 1,
    y: 0,
  },
  snake: [
    { x: 1, y: 10 },
    { x: 2, y: 10 },
    { x: 3, y: 10 },
  ],
};

let food = {};

function init() {
  canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");

  canvas.width = canvas.height = 600;

  ctx.fillStyle = BG_COLOUR;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  randomFood();

  document.addEventListener("keydown", keydown);
}

function keydown(e) {
  let keyCode = e.keyCode;
  switch (keyCode) {
    case 37: {
      // left
      if (player.vel.x !== 1) player.vel = { x: -1, y: 0 };
      break;
    }
    case 65: {
      // left
      if (player.vel.x !== 1) player.vel = { x: -1, y: 0 };
      break;
    }
    case 38: {
      // up
      if (player.vel.y !== 1) player.vel = { x: 0, y: -1 };
      break;
    }
    case 87: {
      // up
      if (player.vel.y !== 1) player.vel = { x: 0, y: -1 };
      break;
    }
    case 39: {
      // right
      if (player.vel.x !== -1) player.vel = { x: 1, y: 0 };
      break;
    }
    case 68: {
      // right
      if (player.vel.x !== -1) player.vel = { x: 1, y: 0 };
      break;
    }
    case 40: {
      // down
      if (player.vel.y !== -1) player.vel = { x: 0, y: 1 };
      break;
    }
    case 83: {
      // down
      if (player.vel.y !== -1) player.vel = { x: 0, y: 1 };
      break;
    }
  }
}

function paintGame() {
  ctx.fillStyle = BG_COLOUR;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  let size = canvas.width / GRID_SIZE;

  ctx.fillStyle = FOOD_COLOUR;
  ctx.fillRect(food.x * size, food.y * size, size, size);

  paintPlayer(size);
}

function paintPlayer(size) {
  ctx.fillStyle = SNAKE_COLOUR;
  for (let cell of player.snake) {
    ctx.fillRect(cell.x * size, cell.y * size, size, size);
  }
}

function randomFood() {
  food = {
    x: Math.floor(Math.random() * GRID_SIZE),
    y: Math.floor(Math.random() * GRID_SIZE),
  };

  for (let cell of player.snake) {
    if (cell.x === food.x && cell.y === food.y) {
      return randomFood();
    }
  }
}

function checkWall() {
  if (player.pos.x < 0) {
    player.pos.x = GRID_SIZE - 1;
    return;
  }
  if (player.pos.x === GRID_SIZE) {
    player.pos.x = 0;
    return;
  }
  if (player.pos.y < 0) {
    player.pos.y = GRID_SIZE - 1;
    return;
  }
  if (player.pos.y === GRID_SIZE) {
    player.pos.y = 0;
  }
}

function gameLoop() {
  player.pos.x += player.vel.x;
  player.pos.y += player.vel.y;

  checkWall();

  player.snake.push({ ...player.pos });

  if (food.x === player.pos.x && food.y === player.pos.y) {
    if (player.snake.length === 400) {
      gameActive = "WIN";
      return;
    }
    randomFood();
  } else {
    player.snake.shift();
  }

  let cnt = 0;
  for (let cell of player.snake) {
    if (cell.x === player.pos.x && cell.y === player.pos.y) {
      cnt++;
      if (cnt > 1) {
        gameActive = "LOSE";
        return;
      }
    }
  }
}

function endGame() {
  if (localData.best_score < player.snake.length)
    localData.best_score = player.snake.length;

  localData.last_score.push(player.snake.length);
  if (localData.last_score.length > 10) localData.last_score.shift();

  localStorage.setItem("localData", JSON.stringify(localData));
  alert(`YOU ${gameActive}!\n
    Score: ${player.snake.length}\n
    Best: ${localData.best_score}\n
    Last: ${localData.last_score}`);
}

function startGameInterval() {
  const interval = setInterval(() => {
    gameLoop();

    if (gameActive) {
      clearInterval(interval);
      endGame();
    } else {
      paintGame();
    }
  }, 1000 / FRAME_RATE);
}

init();
startGameInterval();
