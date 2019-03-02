from SnakePiece import SnakePiece
from Position import Position
from Direction import Direction

class Snake():

	INIT_SIZE = 3
	INIT_POS_X = 400
	INIT_POS_Y = 300

	def __init__(self):
		self.snakePieces = [];
		self.direction = Direction.RIGHT
		for i in range(self.INIT_SIZE):
			self.snakePieces.append(SnakePiece(self.INIT_POS_X-i*SnakePiece.WIDTH, self.INIT_POS_Y))

	def getHead(self):
		return self.snakePieces[0];

	def move(self):
		del snakePieces[-1]
		head = snakePieces[0]
		x = head.pos.x;
		y = head.pos.y;
		pos
		if self.direction == Direction.LEFT:
			pos = Position(x - self.WIDTH, y)
		elif self.direction == Direction.UP:
			pos = Position(x, y - self.HEIGHT)
		elif self.direction == Direction.DOWN:
			pos = Position(x, y + self.HEIGHT)
		elif self.direction == Direction.RIGHT:
			pos = Position(x + self.WIDTH, y);
		self.snakePieces.insert(0, SnakePiece(pos.x, pos, y))

	def update(self):
		move()

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