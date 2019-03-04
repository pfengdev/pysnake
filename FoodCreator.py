import pygame
import random
from Food import Food
from RegularFood import RegularFood
from SnakePiece import SnakePiece

class FoodCreator:

	def __init__(self, gridInfo):
		self.gridInfo = gridInfo

	def createFood(self, otherSprites):
		retry = True
		x = None
		y = None
		food = None
		while retry:
			x = random.randint(0, self.gridInfo.colNum-1) * SnakePiece.SIZE
			y = random.randint(0, self.gridInfo.rowNum-1) * SnakePiece.SIZE
			retry = False
			food = RegularFood(x, y)
			if pygame.sprite.spritecollideany(food, otherSprites):
				retry = True
		return food