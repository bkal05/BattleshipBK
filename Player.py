class Player:

    def __init__(self):
        self.shipGrid = []
        self.guessGrid = []
        rows = 11
        for rows in range(1, 11): # for loop that traverses array of length 10
            self.shipGrid.append(["~"] * 10)
            self.guessGrid.append(["~"] * 10)

    # printShipGrid prints the Player/Computer Placing Ships Grid
    def printShipGrid(self):
        print("Ship Grid")
        for x in self.shipGrid: # for loop that traverses 2D ship array
            print(x)

    # printGuessGrid prints the player/computer guessing ships grid
    def printGuessGrid(self):
        print("Guess Grid")
        for x in self.guessGrid: # for loop that traverses 2D guess array
            print(x)

    # placeShips is a placeholder method
    def placeShips(self, ship, spaces):
        # pass means the method doesn't do anything, its just a placeholder for the
        # subclasses to overwrite
        pass

    # makeGuesses is also a placeholder method, which is used for the subclasses to overwrite
    def makeGuesses(self):
        pass

    # checkLegalPlacement determines if the coordinates inputted by the player are legal
    def checkLegalPlacement( self , row , col , horiz , ship, spaces ):
        if( horiz == "H"): # if user says horizontal
            if( col + spaces > 9 ): # if the column inputted + the amount of spaces of the ship exceeds the amount of columns
                return False
            elif (self.shipGrid[row][col] != '~'): # if there is already a ship in that coordinate
                return False
            else: # if not
                if (self.shipGrid[row][col] == '~'): # if it is a valid coordinate
                    for x in range(spaces): # for loop that traverses number of coordinates a ship takes
                        if (self.shipGrid[row][col + x] != '~'): # if there is a ship occupying any of the coordinates
                            return False
                else:
                    return True
        else: # if vertical
            if (row + spaces > 9): # if the row inputted + amount of spaces of ship exceeds amount of rows
                return False
            elif (self.shipGrid[row][col] != '~'): # if there is already a ship in that coordinate
                return False
            else:
                if (self.shipGrid[row][col] == '~'): # if it is a valid coordinate
                    for x in range(spaces): # for loop that traverses number of coordinates a ship takes
                        if (self.shipGrid[row + x][col] != '~'): # if there is a ship occupying any of the coordinates
                            return False
                else:
                    return True


    # placeShipInGrid places the ship based on location, type of ship, and direction
    def placeShipInGrid( self , row , col , horiz , ship , spaces):
        if (horiz == "H"): # if user inputs horizontal
            for c in range(col, col + spaces): # for loop that traverses from inputted column to the end of the ship column
                self.shipGrid[row][c] = ship
        elif (horiz == "V"): # if user inputs vertical
            for r in range(row, row + spaces): # for loop that traverses from inputted row to end of ship column
                self.shipGrid[r][col] = ship