from Player import Player
from ComputerPlayer import ComputerPlayer

computer = ComputerPlayer()

hits = 0

class HumanPlayer(Player):

    def placeShips(self, ship, spaces):  # places ships
        while (True):
            row = int(input("Enter the row coordinate where ship starts "))
            col = int(input("Enter the col coordinate where ship starts "))
            horiz = input("Horizontal or Vertical? (H/V) ")
            if (row > 9 or row < 0 or col > 9 or col < 0):  # if placement is out of bounds
                print("Out of bounds, try again")
                continue
            horiz = horiz.upper()
            if (horiz != "V" and horiz != "H"):  # if direction is invalid
                print("Only horizonatal or vertical, try again")
                continue
            inGrid = self.checkLegalPlacement(row, col, horiz, ship, spaces)
            if (inGrid == False):  # if placed invalidly
                print("Illegal placement, try again")
                continue
            self.placeShipInGrid(row, col, horiz, ship, spaces)
            break

    def GuessShips(self, c):
        global hits
        while (True):
            self.printGuessGrid()
            row = int(input("Enter the row coordinate where you want to guess "))
            col = int(input("Enter the col coordinate where you want to guess "))
            if (row > 9 or row < 0 or col > 9 or col < 0):  # if placement is out of bounds
                print("Out of bounds, try again")
                continue
            else:
                if (c.shipGrid[row][col] == '~'):
                    print("miss")
                    self.guessGrid[row][col] = 'o'
                    break
                elif (self.guessGrid[row][col] == 'o' or self.guessGrid[row][col] == 'x'):
                    print('already guessed there pick new coordinate')
                    continue
                else:
                    print("hit")
                    self.guessGrid[row][col] = 'x'
                    hits = hits + 1
                    print(hits)
                    if (hits == 17):
                        print("You Won!!!")
                        quit()
                    break
