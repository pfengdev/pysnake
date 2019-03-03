from Wall import Wall

class Map:

	def __init__(self):
		self.walls = []
		self.initWalls()

	def initWalls(self):
		pass

	def addWall(self, wall):
		self.walls.append(wall)

	def getWalls(self):
		return self.walls

