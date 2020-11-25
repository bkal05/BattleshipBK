from Player import Player
from ComputerPlayer import ComputerPlayer
class HumanPlayer( Player ):

    def placeShips(self, ship , spaces):  # places ships
        while (True):
            row = int(input("Enter the row coordinate where ship starts"))
            col = int(input("Enter the col coordinate where ship starts"))
            horiz = input("Horizontal or Vertical? (H/V)")
            if (row > 9 or row < 0 or col > 9 or col < 0):  # if placement is out of bounds
                print("Out of bounds, try again")
                continue
            horiz = horiz.upper()
            if (horiz != "V" and horiz != "H"):  # if direction is invalid
                print("Only horizonatal or vertical, try again")
                continue
            inGrid = self.checkLegalPlacement(row, col, horiz, ship , spaces)
            if (inGrid == False):  # if placed invalidly
                print("Illegal placement, try again")
                continue
            self.placeShipInGrid(row, col, horiz, ship , spaces)
            break

    def GuessShips(self, c):
        x = 0
        while (x < 17):
            self.printGuessGrid()
            row = int(input("Enter the row coordinate where you want to guess"))
            col = int(input("Enter the col coordinate where you want to guess"))
            if (row > 9 or row < 0 or col > 9 or col < 0):  # if placement is out of bounds
                print("Out of bounds, try again")
                continue
            if (c.shipGrid[row][col] == '~'):
                print("miss")
                self.guessGrid[row][col] = 'o'
                continue
            if (self.guessGrid[row][col] == 'o'):
                print('already guessed there pick new coordinate')
                continue
            if (c.shipGrid[row][col] == 'D'):
                print("hit")
                self.guessGrid[row][col] = 'x'
                x + 1
                continue
            if (c.shipGrid[row][col] == 'C'):
                print("hit")
                self.guessGrid[row][col] = 'x'
                x + 1
                continue
            if (c.shipGrid[row][col] == 'S'):
                print("hit")
                self.guessGrid[row][col] = 'x'
                x + 1
                continue

            if (c.shipGrid[row][col] == 'B'):
                print("hit")
                self.guessGrid[row][col] = 'x'
                x + 1
                continue

            if (c.shipGrid[row][col] == 'A'):
                print("hit")
                self.guessGrid[row][col] = 'x'
                x + 1
