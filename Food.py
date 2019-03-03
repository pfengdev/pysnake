import pygame
from enum import Enum
from Item import Item

class State(Enum):
	INIT = 0
	EATEN = 1
	DONE = 2

class Food(pygame.sprite.Sprite, Item):

	def getAmount(self):
		return self.amount

	def decrement(self):
		if self.state == State.EATEN:
			self.amount -= 1
		if self.amount == 0:
			self.state = State.DONE

	def changeStateToEaten(self):
		if self.state == State.INIT:
			self.state = State.EATEN

	def isStateDone(self):
		return self.state == State.DONE


	def __init__(self, amount):
		super(Food, self).__init__()
		self.state = State.INIT
		self.amount = amount