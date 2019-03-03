import pygame
from Food import Food

class RegularFood(Food):
	
	AMOUNT = 1

	def __init__(self, x, y):
		super(RegularFood, self).__init__(self.AMOUNT)
		self.surf = pygame.Surface((self.SIZE, self.SIZE))
		self.surf.fill((0,0,0))
		rect = (self.INNER_X, self.INNER_Y, self.INNER_SIZE, self.INNER_SIZE)
		self.surf.fill((255, 0, 0), rect)
		self.rect = self.surf.get_rect(left = x, top = y)