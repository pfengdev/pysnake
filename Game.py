import pygame
from pygame.locals import *
from Snake import Snake

WIDTH = 800
HEIGHT = 600
gameOver = False

pygame.init()
window = pygame.display.set_mode((800, 600))

background = pygame.Surface(window.get_size())
background.fill((0,0,0))

snake = Snake()
snakePieces = []
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



# Food spawnFood() {
# 	int x;
# 	int y;
# 	boolean retry = true;
# 	while (retry) {
# 		Position.randPos(ROW_SIZE, COL_SIZE);
# 		retry = false;
# 		for (Position : snake.getPositions()) {
# 			if (position.equals(coordinate)) {
# 				retry = true;
# 				break;
# 			}
# 		}
# 	}
# 	return new Food(position);
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