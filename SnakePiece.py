import pygame
from Position import Position

class SnakePiece(pygame.sprite.Sprite):

	WIDTH = 50
	HEIGHT = 50

	def __init__(self, x, y):
		super(SnakePiece, self).__init__()
		self.surf = pygame.Surface((self.WIDTH, self.HEIGHT))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect(left = x, top = y)