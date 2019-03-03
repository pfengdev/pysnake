import random
from Food import Food
from RegularFood import RegularFood
from SnakePiece import SnakePiece

class FoodCreator:

	def __init__(self, gridInfo):
		self.gridInfo = gridInfo

	def createFood(self, otherSprites):
		retry = True
		while retry:
			x = random.randint(0, self.gridInfo.colNum) * SnakePiece.SIZE
			y = random.randint(0, self.gridInfo.rowNum) * SnakePiece.SIZE
			retry = False
			for otherSprite in otherSprites:
				if otherSprite.rect.x == x and otherSprite.rect.y == y:
					retry = True
					break
					
		return RegularFood(x, y)