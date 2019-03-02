import pygame
from pygame.locals import *
from Snake import Snake
from SnakePiece import SnakePiece
from SpawnFood import SpawnFood
from GridInfo import GridInfo

class Game:
	WIDTH = 800
	HEIGHT = 800
	ROW_NUM = HEIGHT/SnakePiece.SIZE
	COL_NUM = WIDTH/SnakePiece.SIZE
	gameOver = False

	pygame.init()
	window = pygame.display.set_mode((WIDTH, HEIGHT))

	background = pygame.Surface(window.get_size())
	background.fill((0,0,0))

	gridInfo = GridInfo((WIDTH, HEIGHT, ROW_NUM, COL_NUM))
	snake = Snake()
	spawnFood = SpawnFood(gridInfo)
	snakePieces = []
	food = []
	running = True

	def checkRunning(self, events):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					return False
			elif event.type == QUIT:
					return False
		return True

	def render(self):
		self.window.blit(self.background, (0, 0))
		for snakePiece in self.snake.getSnakePieces():
			self.window.blit(snakePiece.surf, snakePiece.rect)
		for f in self.food:
			self.window.blit(f.surf, f.rect)
		pygame.display.flip()

	def updateSnake(self):
		self.snake.move()

	def update(self):
		self.updateSnake()

	def handleInput(self, events):
		self.snake.handleInput(events)

	def shouldSpawnFood(self):
		return not self.food

	def spawnFood(self):
		if self.shouldSpawnFood():
			self.food.append(self.spawnFood.spawn(self.snake.getSnakePieces(), self.gridInfo))

	def run(self):
		while self.running:
			self.render()
			events = pygame.event.get()
			self.running = self.checkRunning(events)
			self.handleInput(events)
			self.update()
			pygame.time.wait(5)

game = Game()
game.run()

# self.checkSnakeEatFood()
# def checkSnakeEatFood(self):
# 	head = self.snake.getSnakePieces[0];
# 	if head.rect.x == food[0].rect.x and head.rect.y == food[0].rect.y:
# 		self.snake.eat(food)

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

# checkSnakeDie() {
# 	snake.collideSelf();
# 	checkSnakeHitWall();
# }

# private checkSnakeHitWall() {
# 	return head.x < 0 || head.x > COL_SIZE || head.y < 0 || head.y > ROW_SIZE;
# }