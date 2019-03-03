import pygame
from Item import Item

class Wall(pygame.sprite.Sprite, Item):
	
	def __init__(self, x, y, width, height):
		self.surf = pygame.Surface((width*self.SIZE, height*self.SIZE))
		self.surf.fill((255,255,255))
		self.rect = self.surf.get_rect(left = x, top = y)