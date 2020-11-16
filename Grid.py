class Grid:

    def __init__(self):
        self.Grid = []
        rows = 11
        for rows in range(1, 11):
            self.Grid.append(["~"] * 10)

    def toString(self):
        for x in self.Grid:
            print(x)







