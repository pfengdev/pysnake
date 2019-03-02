import random
from Food import Food
from RegularFood import RegularFood
from SnakePiece import SnakePiece

class SpawnFood:

	def spawn(self, otherSprites, gridInfo):
		x = random.randint(0, gridInfo.colNum) * SnakePiece.SIZE
		y = random.randint(0, gridInfo.rowNum) * SnakePiece.SIZE
		retry = True
		while retry:
			retry = False
			for otherSprite in otherSprites:
				if otherSprite.rect.x == x and otherSprite.rect.y == y:
					retry = True
					break
					
		return RegularFood(x, y);

	def __init__(self, gridInfo):
		self.gridInfo = gridInfo