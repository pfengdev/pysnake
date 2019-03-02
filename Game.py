import pygame
from pygame.locals import *
from Snake import Snake
from SnakePiece import SnakePiece
from SpawnFood import SpawnFood
from GridInfo import GridInfo

WIDTH = 800
HEIGHT = 800
ROW_NUM = HEIGHT/SnakePiece.SIZE
COL_NUM = WIDTH/SnakePiece.SIZE
gameOver = False

pygame.init()
window = pygame.display.set_mode((800, 600))

background = pygame.Surface(window.get_size())
background.fill((0,0,0))

gridInfo = GridInfo((WIDTH, HEIGHT, ROW_NUM, COL_NUM))
snake = Snake()
spawnFood = SpawnFood(gridInfo)
snakePieces = []
food = []
running = True

def checkRunning(events):
	for event in events:
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				return False
		elif event.type == QUIT:
				return False
	return True

def render():
	window.blit(background, (0, 0))
	for snakePiece in snake.getSnakePieces():
		window.blit(snakePiece.surf, snakePiece.rect)
	for f in food:
		window.blit(f.surf, f.rect)
	pygame.display.flip()

def updateSnake():
	snake.move()

def update():
	updateSnake()

def handleInput(events):
	snake.handleInput(events)

while running:
	render()
	events = pygame.event.get()
	running = checkRunning(events)
	handleInput(events)
	update()
	if not food:
		food.append(spawnFood.spawn(snake.getSnakePieces(), gridInfo))


# gameLoop() {
# 	while(!gameOver) {
# 		if (shouldSpawnFood) {
# 			spawnFood();
# 		}
# 		moveSnake();
# 		checkSnakeEatFood();
# 		if (checkSnakeDie()) {
# 			gameOver = true;
# 		}
# 	}
# 	displayGameOver();
# }

# checkSnakeEatFood() {
# 	head = positions[0];
# 	if head.equals(food.position) {
# 		snake.eat(food);
# 		shouldSpawnFood = true;
# 	}
# }

# checkSnakeDie() {
# 	snake.collideSelf();
# 	checkSnakeHitWall();
# }

# private checkSnakeHitWall() {
# 	return head.x < 0 || head.x > COL_SIZE || head.y < 0 || head.y > ROW_SIZE;
# }