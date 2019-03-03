import pygame
from pygame.locals import *
from SnakePiece import SnakePiece
from Direction import Direction

class Snake:

	INIT_SIZE = 3
	INIT_POS_X = 400
	INIT_POS_Y = 400

	def __init__(self):
		self.snakePieces = [];
		self.direction = Direction.RIGHT
		for i in range(self.INIT_SIZE):
			self.snakePieces.append(SnakePiece((self.INIT_POS_X-i*SnakePiece.SIZE, self.INIT_POS_Y)))
		self.foodList = [];
		self.doGrow = False

	def getHead(self):
		return self.snakePieces[0];

	def grow(self):
		if not self.doGrow:
			del self.snakePieces[-1]
		self.doGrow = False

	def move(self):
		head = self.snakePieces[0]
		x = head.rect.x;
		y = head.rect.y;
		if self.direction == Direction.LEFT:
			x -= SnakePiece.SIZE
		elif self.direction == Direction.UP:
			y -= SnakePiece.SIZE
		elif self.direction == Direction.DOWN:
			y += SnakePiece.SIZE
		elif self.direction == Direction.RIGHT:
			x += SnakePiece.SIZE
		self.snakePieces.insert(0, SnakePiece((x, y)))

	def processFood(self):
		if (self.foodList):
			food = self.foodList[0]
			food.decrement();
			self.doGrow = True
			if (food.isStateDone()):
				self.foodList.remove(food);


	def handleInput(self, events):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_w and self.direction != Direction.DOWN:
					self.direction = Direction.UP
				elif event.key == K_s and self.direction != Direction.UP:
					self.direction = Direction.DOWN
				elif event.key == K_a and self.direction != Direction.RIGHT:
					self.direction = Direction.LEFT
				elif event.key == K_d and self.direction != Direction.LEFT:
					self.direction = Direction.RIGHT

	def getSnakePieces(self):
		return self.snakePieces

	def eat(self, food):
		food.changeStateToEaten();
		self.foodList.append(food);

	def update(self):
		self.processFood();
		self.grow();
		self.move();


	def collideSelf(self):
		head = self.snakePieces[0]
		for i in range(1, len(self.snakePieces)-1):
			if head.rect.x == self.snakePieces[i].rect.x and head.rect.y == self.snakePieces[i].rect.y:
				return True
		return False