from SnakePiece import SnakePiece
from Position import Position

class Snake():

	INIT_SIZE = 3
	INIT_POS_X = 400
	INIT_POS_Y = 300

	def __init__(self):
		self.snakePieces = [];
		self.position = Position(self.INIT_POS_X, self.INIT_POS_Y)
		for i in range(self.INIT_SIZE):
			self.snakePieces.append(SnakePiece())


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