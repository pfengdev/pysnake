from SnakePiece import SnakePiece
from Direction import Direction
from pygame.locals import *

class Snake():

	INIT_SIZE = 3
	INIT_POS_X = 400
	INIT_POS_Y = 300

	def __init__(self):
		self.snakePieces = [];
		self.direction = Direction.RIGHT
		for i in range(self.INIT_SIZE):
			self.snakePieces.append(SnakePiece((self.INIT_POS_X-i*SnakePiece.SIZE, self.INIT_POS_Y)))

	def getHead(self):
		return self.snakePieces[0];

	def move(self):
		del self.snakePieces[-1]
		head = self.snakePieces[0]
		x = head.rect.x;
		y = head.rect.y;
		pos = None
		if self.direction == Direction.LEFT:
			x -= SnakePiece.SIZE
		elif self.direction == Direction.UP:
			y -= SnakePiece.SIZE
		elif self.direction == Direction.DOWN:
			y += SnakePiece.SIZE
		elif self.direction == Direction.RIGHT:
			x += SnakePiece.SIZE
		self.snakePieces.insert(0, SnakePiece((x, y)))

	def handleInput(self, key):
		if key == K_w and self.direction != Direction.DOWN:
			self.direction = Direction.UP
		elif key == K_s and self.direction != Direction.UP:
			self.direction = Direction.DOWN
		elif key == K_a and self.direction != Direction.RIGHT:
			self.direction = Direction.LEFT
		elif key == K_d and self.direction != Direction.LEFT:
			self.direction = Direction.RIGHT

	def getSnakePieces(self):
		return self.snakePieces


	# List<Position> position = Array? (for basic case only need to add to the back, must be back because user input will change front.
	# 	Process needs to do in order)

	# List<Food> eatenFood = LinkedList(); //constant removal, removing is easier. although most of time only one food at a time

	# DIRECTION { LEFT, UP, RIGHT, DOWN }

	# eat(Food food) {
	# 	//changing the state of an object. good or bad? maybe return?
	# 	food.changeStateToEaten();
	# 	//should i make my own copy?
	# 	eatenFood.add(food);
	# }

	# processFood() {
	# 	if (eatenFood != null && !eatenFood.isEmpty()) {
	# 		eatenFood.get(0).decrement();
	# 		if (eatenFood.isDone()) {
	# 			eatenFood.remove(0);
	# 		}
	# 	}
	# }

	# collideSelf() {
	# 	if (positions == null || positions.isEmpty()) {
	# 		//something wrong
	# 		//or is this unnecessary error?
	# 	}
	# 	Position head = positions.get(0);
	# 	for (i = 1; i < positions.length; i++) {
	# 		if head.equals(positions[i]) return true
	# 	}
	# 	return false
	# }

	# getPositions() {

	# }