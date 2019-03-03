import pygame
from pygame.locals import *
from Snake import Snake
from SnakePiece import SnakePiece
from FoodCreator import FoodCreator
from GridInfo import GridInfo

class Game:
	WIDTH = 800
	HEIGHT = 800
	ROW_NUM = HEIGHT/SnakePiece.SIZE
	COL_NUM = WIDTH/SnakePiece.SIZE

	def __init__(self):

		pygame.init()
		self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

		self.background = pygame.Surface(self.window.get_size())
		self.background.fill((0,0,0))

		self.gridInfo = GridInfo((self.WIDTH, self.HEIGHT, self.ROW_NUM, self.COL_NUM))
		self.snake = Snake()
		self.foodCreator = FoodCreator(self.gridInfo)
		self.snakePieces = []
		self.foodList = []
		self.running = True
		self.gameOver = False

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
		for f in self.foodList:
			self.window.blit(f.surf, f.rect)
		pygame.display.flip()

	def update(self):
		self.snake.update()

	def handleInput(self, events):
		self.snake.handleInput(events)

	def shouldSpawnFood(self):
		return not self.foodList

	def spawnFood(self):
		if self.shouldSpawnFood():
			newFood = self.foodCreator.createFood(self.snake.getSnakePieces())
			self.foodList.append(newFood)

	def checkSnakeEatFood(self):
		head = self.snake.getSnakePieces()[0];
		if self.foodList:
			food = self.foodList[0]
		if self.foodList and head.rect.x == self.foodList[0].rect.x and head.rect.y == self.foodList[0].rect.y:
			self.snake.eat(food)
			self.foodList.remove(food)
			food.kill()

	def run(self):
		while self.running:
			self.render()
			events = pygame.event.get()
			self.running = self.checkRunning(events)
			self.handleInput(events)
			self.update()
			self.checkSnakeEatFood()
			self.spawnFood()
			pygame.time.wait(5)

game = Game()
game.run()

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