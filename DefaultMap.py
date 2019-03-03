from Map import Map
from Wall import Wall

class DefaultMap(Map):
	
	def initWalls(self):
		wall = Wall(0, 0, 1, 20)
		self.addWall(wall)
		wall = Wall(760, 0, 1, 20)
		self.addWall(wall)
		wall = Wall(0, 0, 20, 1)
		self.addWall(wall)
		wall = Wall(0, 760, 20, 1)
		self.addWall(wall)

	def __init__(self):
		super(DefaultMap, self).__init__()