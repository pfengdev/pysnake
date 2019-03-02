import pygame
from Snake import Snake 

class SnakeRenderer(pygame.sprite.Sprite):

	WIDTH = 100
	HEIGHT = 100

	def __init__(self):
		super(SnakeRenderer, self).__init__()
		self.surf = pygame.Surface((self.WIDTH, self.HEIGHT))
		self.surf.fill((255, 255, 255))

