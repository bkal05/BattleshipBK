from Player import Player

import random

hits = 0

class ComputerPlayer(Player):

    def placeShips(self, ship, spaces):  # places ships
        while (True):
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            direction = random.randint(0, 1)
            horiz = "V"
            if (direction == 1):
                horiz = "H"

            inGrid = self.checkLegalPlacement(row, col, horiz, ship, spaces)
            if (inGrid == False):
                continue
            self.placeShipInGrid(row, col, horiz, ship, spaces)
            break

    def GuessShips(self, p):
        global hits
        while (True):
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            print("Computer guessed (" + str(row) + ", " + str(col) + ")")
            if (row > 9 or row < 0 or col > 9 or col < 0):  # if placement is out of bounds
                print("Out of bounds, try again")
            else:
                if (p.shipGrid[row][col] == '~'):
                    print("miss")
                    self.guessGrid[row][col] = 'o'
                    break

                elif (self.guessGrid[row][col] == 'o' or self.guessGrid[row][col] == 'x'):
                    print('already guessed there pick new coordinate')

                else:
                    print("hit")
                    self.guessGrid[row][col] = 'x'
                    hits += 1
                    if (hits == 17):
                        print("Computer Won, better luck next time")
                        quit()
                    break



