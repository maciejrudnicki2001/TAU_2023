import random


class MazeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.start_pos = None
        self.end_pos = None
        self.obstacle_positions = set()

    def generate_maze(self):
        # Generate start and end positions
        while not self.start_pos or not self.end_pos or self.start_pos == self.end_pos:
            self.start_pos = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            self.end_pos = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))

        # Generate obstacle positions
        for i in range(random.randint(self.width * self.height // 10, self.width * self.height // 5)):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) != self.start_pos and (x, y) != self.end_pos:
                self.obstacle_positions.add((x, y))

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacle_positions

    def print_maze(self, current_pos):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == current_pos:
                    print("A", end="")
                elif (x, y) == self.end_pos:
                    print("B", end="")
                elif (x, y) in self.obstacle_positions:
                    print("X", end="")
                else:
                    print(".", end="")
            print()

    def play_game(self):
        current_pos = self.start_pos
        while current_pos != self.end_pos:
            self.print_maze(current_pos)
            direction = input("Enter direction (up/down/left/right): ")
            if direction == "up":
                new_pos = (current_pos[0], current_pos[1] - 1)
            elif direction == "down":
                new_pos = (current_pos[0], current_pos[1] + 1)
            elif direction == "left":
                new_pos = (current_pos[0] - 1, current_pos[1])
            elif direction == "right":
                new_pos = (current_pos[0] + 1, current_pos[1])
            else:
                print("Invalid direction!")
                continue
            if self.is_valid_position(*new_pos):
                current_pos = new_pos
                self.start_pos = current_pos
            else:
                print("You hit an obstacle!")
        print("You won!")


# Example usage
game = MazeGame(5, 5)
game.generate_maze()
game.play_game()
