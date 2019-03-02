class Game {
	int ROW_SIZE;
	int COL_SIZE;
	bool gameOver = false;

	gameLoop() {
		while(!gameOver) {
			if (shouldSpawnFood) {
				spawnFood();
			}
			moveSnake();
			checkSnakeEatFood();
			if (checkSnakeDie()) {
				gameOver = true;
			}
		}
		displayGameOver();
	}
	


	Food spawnFood() {
		int x;
		int y;
		boolean retry = true;
		while (retry) {
			Position.randPos(ROW_SIZE, COL_SIZE);
			retry = false;
			for (Position : snake.getPositions()) {
				if (position.equals(coordinate)) {
					retry = true;
					break;
				}
			}
		}
		return new Food(position);
	} 

	moveSnake() {
		for (int i = position.size()-1; i > 0; i--) {
			position[i] = position[i-1];
		}
		head = positions[0];
		x = head.x;
		y = head.y;
		//not using && to avoid unnecessary check
		switch (DIRECTION) {
			LEFT: head = new Position(x - 1, y);
		} //etc
	}

	checkSnakeEatFood() {
		head = positions[0];
		if head.equals(food.position) {
			snake.eat(food);
			shouldSpawnFood = true;
		}
	}

	checkSnakeDie() {
		snake.collideSelf();
		checkSnakeHitWall();
	}

	private checkSnakeHitWall() {
		return head.x < 0 || head.x > COL_SIZE || head.y < 0 || head.y > ROW_SIZE;
	}
}