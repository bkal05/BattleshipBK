from Player import Player

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