import pygame
from pygame.locals import *
from Snake import Snake
from SnakeRenderer import SnakeRenderer

WIDTH = 800
HEIGHT = 600
gameOver = False

pygame.init()
window = pygame.display.set_mode((800, 600))

background = pygame.Surface(window.get_size())
background.fill((100,200,255))

snakeRenderer = SnakeRenderer()

def running():
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				return False
		elif event.type == QUIT:
				return False
	return True

def render():
	window.blit(background, (0, 0))
	window.blit(snakeRenderer.surf, (400, 300))
	pygame.display.flip()

while running():
	render()

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

# moveSnake() {
# 	for (int i = position.size()-1; i > 0; i--) {
# 		position[i] = position[i-1];
# 	}
# 	head = positions[0];
# 	x = head.x;
# 	y = head.y;
# 	//not using && to avoid unnecessary check
# 	switch (DIRECTION) {
# 		LEFT: head = new Position(x - 1, y);
# 	} //etc
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