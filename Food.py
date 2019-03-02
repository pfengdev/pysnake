from enum import Enum
from Item import Item

class State(Enum):
	INIT = 0
	EATEN = 1
	DONE = 2

class Food(Item):

	def getAmount(self):
		return self.amount

	def decrement(self):
		if self.state == EATEN:
			self.amount -= 1
		if self.amount == 0:
			self.state = self.DONE

	def changeStateToEaten(self):
		if self.state == self.INIT:
			self.state = EATEN

	def isStateDone(self):
		return self.state == self.DONE


	def __init__(self, amount):
		self.state = INIT
		self.amount = amount