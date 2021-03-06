import pygame
from Item import Item

class SnakePiece(pygame.sprite.Sprite, Item):

	def createSurface(self):
		surf = pygame.Surface((self.SIZE, self.SIZE))
		surf.fill((0, 0, 0))
		rect = (self.INNER_X, self.INNER_Y, self.INNER_SIZE, self.INNER_SIZE)
		surf.fill((0,255,0), rect)
		return surf

	def __init__(self, pos):
		super(SnakePiece, self).__init__()
		self.surf = self.createSurface()
		self.rect = self.surf.get_rect(left = pos[0], top = pos[1])

