from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

print("Welcome to Battleship!")

print("Player one place ships now:")
human = HumanPlayer()
computer = ComputerPlayer()

human.printGuessGrid()
human.printShipGrid()
print("Place destroyer")
human.placeShips("D" , 2)    # letter of ship and its size
human.printShipGrid()
print("Place cruiser")
human.placeShips("C" , 3)
human.printShipGrid()