from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

print("Battleship!")

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
print("Place submarine")
human.placeShips("S" , 3)
human.printShipGrid()
print("Place battleship")
human.placeShips("B" , 4)
human.printShipGrid()
print("Place aircraft carrier")
human.placeShips("A" , 5)
human.printShipGrid()
