import random
import pytest
from _pytest import monkeypatch


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


@pytest.fixture
def test_maze_size():
    width, height = 5, 5
    game = MazeGame(width, height)
    game.generate_maze()
    assert len(game.obstacle_positions) <= width * height // 5  # maksymalna liczba przeszkód
    assert game.start_pos is not None and game.end_pos is not None


def test_is_valid_position():
    width, height = 5, 5
    game = MazeGame(width, height)
    game.generate_maze()
    assert game.is_valid_position(0, 0) is True  # punkt startowy
    assert game.is_valid_position(width - 1, height - 1) is True  # punkt końcowy
    assert game.is_valid_position(width, height) is False  # poza planszą
    for obstacle in game.obstacle_positions:
        assert game.is_valid_position(*obstacle) is False  # przeszkody


def test_movement():
    width, height = 5, 5
    game = MazeGame(width, height)
    game.start_pos = (0, 0)
    game.end_pos = (width - 1, height - 1)
    game.obstacle_positions = {(1, 0), (0, 1), (1, 1)}
    assert game.play_game() == "You won!"  # gracz powinien dotrzeć do końca planszy


def test_input_direction():
    width, height = 5, 5
    game = MazeGame(width, height)
    game.start_pos = (0, 0)
    game.end_pos = (width - 1, height - 1)
    game.obstacle_positions = {(1, 0), (0, 1), (1, 1)}
    # Symuluj wprowadzenie nieprawidłowego kierunku ruchu przez gracza.
    with pytest.raises(SystemExit):
        input_values = ["invalid", "right"]
        monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
        game.play_game()


@pytest.mark.parametrize("direction, new_pos", [("up", (1, 2)), ("down", (1, 4)), ("left", (0, 3)), ("right", (2, 3))])
def test_is_valid_position(direction, new_pos):
    game = MazeGame(5, 5)
    game.generate_maze()
    assert game.is_valid_position(*new_pos) == True
    if direction == "up":
        game.obstacle_positions.add((new_pos[0], new_pos[1] - 1))
    elif direction == "down":
        game.obstacle_positions.add((new_pos[0], new_pos[1] + 1))
    elif direction == "left":
        game.obstacle_positions.add((new_pos[0] - 1, new_pos[1]))
    elif direction == "right":
        game.obstacle_positions.add((new_pos[0] + 1, new_pos[1]))
    assert game.is_valid_position(*new_pos) == False
    game.obstacle_positions.remove(new_pos)


@pytest.mark.parametrize("invalid_direction", ["invalid", "upleft", "downright", ""])
def test_play_game_invalid_direction(invalid_direction, capsys):
    newGame = MazeGame(5, 5)
    newGame.generate_maze()
    inputs = [invalid_direction, "down"]
    input_mock = lambda _: inputs.pop(0)
    newGame.input = input_mock
    newGame.play_game()
    captured = capsys.readouterr()
    assert "Invalid direction!" in captured.out


@pytest.mark.parametrize("invalid_direction", ["invalid", "upleft", "downright", ""])
def test_play_game_invalid_direction(invalid_direction, capsys):
    game = MazeGame(5, 5)
    game.generate_maze()
    inputs = [invalid_direction, "down"]
    input_mock = lambda _: inputs.pop(0)
    game.input = input_mock
    game.play_game()
    captured = capsys.readouterr()
    assert "Invalid direction!" in captured.out