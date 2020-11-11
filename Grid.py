class Grid:

    def __init__(self):
        rows, columns = (11, 11)
        self.Grid = [['~' for i in range(columns)] for j in range(rows)]
        for r in range(11):
            self.changeValue(0, r, Grid.letterToNum(Grid.numToLetter(r)))
        for c in range(11):
            self.changeValue(c, 0, Grid.numToLetter(c))

