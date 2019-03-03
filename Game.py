import pygame
from pygame.locals import *
from Snake import Snake
from SnakePiece import SnakePiece
from FoodCreator import FoodCreator
from GridInfo import GridInfo
from DefaultMap import DefaultMap
from Wall import Wall

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
		self.map = DefaultMap()
		self.walls = pygame.sprite.Group()
		for wall in self.map.getWalls():
			self.walls.add(wall)

	def checkRunning(self, events):
		if self.gameOver:
			return False
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
		for wall in self.walls:
			self.window.blit(wall.surf, wall.rect)
		pygame.display.flip()

	def update(self):
		self.snake.update()

	def handleInput(self, events):
		self.snake.handleInput(events)

	def shouldSpawnFood(self):
		return not self.foodList

	def spawnFood(self):
		if self.shouldSpawnFood():
			otherSprites = [];
			otherSprites.extend(self.snake.getSnakePieces())
			otherSprites.extend(self.walls)
			newFood = self.foodCreator.createFood(otherSprites)
			self.foodList.append(newFood)

	def checkSnakeEatFood(self):
		head = self.snake.getSnakePieces()[0];
		if self.foodList:
			food = self.foodList[0]
		if self.foodList and head.rect.x == self.foodList[0].rect.x and head.rect.y == self.foodList[0].rect.y:
			self.snake.eat(food)
			self.foodList.remove(food)
			food.kill()

	def checkCollisions(self):
		if self.snake.collideSelf() or pygame.sprite.spritecollideany(self.snake.getHead(), self.walls):
			self.gameOver = True

	def run(self):
		while self.running:
			self.render()
			events = pygame.event.get()
			self.running = self.checkRunning(events)
			self.handleInput(events)
			self.update()
			self.checkSnakeEatFood()
			self.spawnFood()
			self.checkCollisions()
			pygame.time.wait(5)

game = Game()
game.run()