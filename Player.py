class Player:

    def __init__(self):
        self.shipGrid = []
        self.guessGrid = []
        rows = 11
        for rows in range(1, 11):
            self.shipGrid.append(["~"] * 10)
            self.guessGrid.append(["~"] * 10)

    def printShipGrid(self):
        print("Ship Grid")
        for x in self.shipGrid:
            print(x)

    def printGuessGrid(self):
        print("Guess Grid")
        for x in self.guessGrid:
            print(x)

    def placeShips(self, ship , spaces):
        # pass means the method doesn't do anything, its just a placeholder for the
        # subclasses to overwrite
        pass

    # you will need to add code to this to confirm that there is only water in
    # spaces you are trying to put the ship in
    # right now it only confirms if the ship size is within the grid size
    def checkLegalPlacement( self , row , col , horiz , ship, spaces ):
        if( horiz == "H"):
            if( col + spaces > 9 ):
                return False
            elif (self.shipGrid[row][col] != '~'):
                return False
            else:
                if (self.shipGrid[row][col] == '~'):
                    for x in range(spaces):
                        if (self.shipGrid[row][col + x] != '~'):
                            return False
                else:
                    return True
        else:
            if (row + spaces > 9):
                return False
            elif (self.shipGrid[row][col] != '~'):
                return False
            else:
                if (self.shipGrid[row][col] == '~'):
                    for x in range(spaces):
                        if (self.shipGrid[row + x][col] != '~'):
                            return False
                else:
                    return True


    def placeShipInGrid( self , row , col , horiz , ship , spaces):
        if (horiz == "H"):
            for c in range(col, col + spaces):
                self.shipGrid[row][c] = ship
        elif (horiz == "V"):
            for r in range(row, row + spaces):
                self.shipGrid[r][col] = ship