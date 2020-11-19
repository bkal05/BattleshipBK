from Grid import Grid


class Player:

    def __init__(self):
        self.ownGrid = Grid()
        self.opponentGrid = Grid()
        self.boatsRemaining = 16

    def placeShips(self, letter):
        if letter.upper() == 'D':
            # ask for 1 coordinate, then ask whether horizontal or vertical, confirm it works
            x1 = int(input("enter 1st x coordinate: "))
            y1 = int(input("enter 1st y coordinate: "))
            x2 = int(input("enter 2nd x coordinate: "))
            y2 = int(input("enter 2nd y coordinate: "))
            Grid[x1][y1] = 'D'
            Grid[x2][y2] = 'D'
            self.boatsRemaining -= 2

        if letter.upper() == 'S':
            x1 = int(input("enter 1st x coordinate: "))
            y1 = int(input("enter 1st y coordinate: "))
            x2 = int(input("enter 2nd x coordinate: "))
            y2 = int(input("enter 2nd y coordinate: "))
            x3 = int(input("enter 3rd x coordinate: "))
            y3 = int(input("enter 2rd y coordinate: "))
            Grid[x1][y1] = 'S'
            Grid[x2][y2] = 'S'
            Grid[x3][y3] = 'S'
            self.boatsRemaining -= 3

        if letter.upper() == 'C':
            x1 = int(input("enter 1st x coordinate: "))
            y1 = int(input("enter 1st y coordinate: "))
            x2 = int(input("enter 2nd x coordinate: "))
            y2 = int(input("enter 2nd y coordinate: "))
            x3 = int(input("enter 3rd x coordinate: "))
            y3 = int(input("enter 2rd y coordinate: "))
            Grid[x1][y1] = 'C'
            Grid[x2][y2] = 'C'
            Grid[x3][y3] = 'C'
            self.boatsRemaining -= 3

        if letter.upper() == 'S':
            x1 = int(input("enter 1st x coordinate: "))
            y1 = int(input("enter 1st y coordinate: "))
            x2 = int(input("enter 2nd x coordinate: "))
            y2 = int(input("enter 2nd y coordinate: "))
            x3 = int(input("enter 3rd x coordinate: "))
            y3 = int(input("enter 2rd y coordinate: "))
            x4 = int(input("enter 4th x coordinate: "))
            y4 = int(input("enter 4th y coordinate: "))
            Grid[x1][y1] = 'B'
            Grid[x2][y2] = 'B'
            Grid[x3][y3] = 'B'
            Grid[x4][y4] = 'B'
            self.boatsRemaining -= 4

        if letter.upper() == 'A':
            x1 = int(input("enter 1st x coordinate: "))
            y1 = int(input("enter 1st y coordinate: "))
            x2 = int(input("enter 2nd x coordinate: "))
            y2 = int(input("enter 2nd y coordinate: "))
            x3 = int(input("enter 3rd x coordinate: "))
            y3 = int(input("enter 2rd y coordinate: "))
            x4 = int(input("enter 4th x coordinate: "))
            y4 = int(input("enter 4th y coordinate: "))
            x5 = int(input("enter 5th x coordinate: "))
            y5 = int(input("enter 5th y coordinate: "))
            Grid[x1][y1] = 'A'
            Grid[x2][y2] = 'A'
            Grid[x3][y3] = 'A'
            Grid[x4][y4] = 'A'
            Grid[x5][y5] = 'A'
            self.boatsRemaining -= 5

    # if orientation.lower() != "vertical" and orientation.lower() != "horizontal":
    #  return "Please enter a valid orientation"

    #   print(T[0][0])

    #  T[0][0] = 'H'
    #  print(T[0][0])