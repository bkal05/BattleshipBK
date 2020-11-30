from Player import Player
from ComputerPlayer import ComputerPlayer

computer = ComputerPlayer()

hits = 0

class HumanPlayer(Player):

    def placeShips(self, ship, spaces):  # places ships
        while (True):  # checks if placement is valid, runs until placement is valid
            row = int(input("Enter the row coordinate where ship starts "))
            col = int(input("Enter the col coordinate where ship starts "))
            horiz = input("Horizontal or Vertical? (H/V) ")
            if (row > 9 or row < 0 or col > 9 or col < 0):  # if placement is out of bounds, continue to beginning of loop for new placement
                print("Out of bounds, try again")
                continue
            horiz = horiz.upper()
            if (horiz != "V" and horiz != "H"):  # if direction is invalid, continue to beginning of loop for new placement
                print("Only horizonatal or vertical, try again")
                continue
            inGrid = self.checkLegalPlacement(row, col, horiz, ship, spaces)
            if (inGrid == False):  # if placed invalidly, continue to beginning of loop for new placement
                print("Illegal placement, try again")
                continue
            self.placeShipInGrid(row, col, horiz, ship, spaces)
            break

    def GuessShips(self, c):  # guesses ships
        global hits
        while (True):  # runs until user enters a valid guess coordinate
            self.printGuessGrid()
            row = int(input("Enter the row coordinate where you want to guess "))
            col = int(input("Enter the col coordinate where you want to guess "))
            if (row > 9 or row < 0 or col > 9 or col < 0):  # if placement is out of bounds, get new coordinate
                print("Out of bounds, try again")
                continue
            else:  # if valid guess
                if (c.shipGrid[row][col] == '~'):  # if guess is a miss, edit guess grid appropriately
                    print("miss")
                    self.guessGrid[row][col] = 'o'
                    break
                elif (self.guessGrid[row][col] == 'o' or self.guessGrid[row][col] == 'x'):  # if guess is a repeat of a previous guess, returns to beginning of loop
                    print('already guessed there pick new coordinate')
                    continue
                else:  # adjust grid appropriately for a hit, and increment hits by one
                    print("hit")
                    self.guessGrid[row][col] = 'x'
                    hits = hits + 1
                    print(hits)
                    if (hits == 17):  # if user has correctly guessed 17 coordinates, they win
                        print("You Won!!!")
                        quit()
                    break
