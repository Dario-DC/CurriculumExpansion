import random


class Grid:
    def __init__(self):
        self.reset_grid()

    def __str__(self):
        grid = f'┌{"─"*9}┐\n'
        for row in self.grid:
            grid += '|' + ' '.join(row) + '|\n'
        grid += f'└{"─"*9}┘'
        return grid

    def reset_grid(self):
        self.grid = [[" "] * 5 for _ in range(5)]


class Pound:
    def __init__(self, x, y):
        self.position = (x, y)
        self.symbol = "#"
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def move(self):
        direction = random.choice(self.moves)
        x, y = self.position
        x_move, y_move = direction
        new_x = (x + x_move) % 5
        new_y = (y + y_move) % 5
        self.position = (new_x, new_y)


class Dot(Pound):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.moves = [(0, 0), (2, 0), (0, 2), (-2, 0), (0, -2)]
        self.symbol = "o"

    def move(self):
        direction = random.choices(self.moves, weights=(1, 1, 3, 1, 1))[0]
        x, y = self.position
        x_move, y_move = direction
        new_x = (x + x_move) % 5
        new_y = (y + y_move) % 5
        self.position = (new_x, new_y)


def arrange_players(grid, player1, player2):
    grid.reset_grid()
    x1, y1 = player1.position
    x2, y2 = player2.position
    if player1.position != player2.position:
        grid.grid[x1][y1] = player1.symbol
        grid.grid[x2][y2] = player2.symbol
        return True
    grid.grid[x1][y1] = "X"
    return False


def play():
    grid = Grid()
    player1 = Pound(random.randrange(5), random.randrange(5))
    player2 = Dot(random.randrange(5), random.randrange(5))

    while arrange_players(grid, player1, player2):
        print(grid)
        player1.move()
        player2.move()
    print("Game Over!")
    print(grid)


play()
