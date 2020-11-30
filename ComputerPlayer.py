from Player import Player

import random

hits = 0

class ComputerPlayer(Player):

    # Places ships based on the letter inputted and the number of spaces the ship takes up
    def placeShips(self, ship, spaces):  # places ships
        while (True):  # while the ship placement is in the grid it runs the code placing the ship
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            direction = random.randint(0, 1)
            horiz = "V"
            if (direction == 1):  # if the random number generated is 1 then the ship is horizontal
                horiz = "H"

            inGrid = self.checkLegalPlacement(row, col, horiz, ship, spaces)
            if (inGrid == False):  # if the ship is not in the grid inGrid becomes false and it reruns the code
                continue
            self.placeShipInGrid(row, col, horiz, ship, spaces)
            break
    # computer guesses the on the computer guess grid and compares it to the player input grid inputted in the method
    def GuessShips(self, p):
        global hits
        while (True):  # reruns the guess ship code until the amount of hits becomes 17
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            print("Computer guessed (" + str(row) + ", " + str(col) + ")")
            if (row > 9 or row < 0 or col > 9 or col < 0):  # if placement is out of bounds
                print("Out of bounds, try again")
            else: 
                if (p.shipGrid[row][col] == '~'):  # prints miss if the random coordinate does not correspond with a ship
                    print("miss")
                    self.guessGrid[row][col] = 'o'
                    break

                elif (self.guessGrid[row][col] == 'o' or self.guessGrid[row][col] == 'x'):  # if coordinate on guess is already o tells computer to enter in a new coordinate
                    print('already guessed there pick new coordinate')

                else:
                    print("hit")
                    self.guessGrid[row][col] = 'x'
                    hits += 1
                    if (hits == 17):  # if the total number of hits becomes 17 then the computer one. Ends the code
                        print("Computer Won, better luck next time")
                        quit()
                    break
