interface Food {
	State { NOT_EATEN ,EATEN, DONE }

	Food(Position) {

	}

	displayImage()/getImage();

	getSize();

	changeStateToEaten(); //if eaten, then don't displayimage

	decrement(); //change state to DONE when 0

	isStateDone();
}