from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

print("Battleship!")

print("User place ships now:")
human = HumanPlayer()
print("Place destroyer")
human.placeShips("D" , 2)    # letter of ship and its size
print("Place cruiser")
human.placeShips("C" , 3)
print("Place submarine")
human.placeShips("S" , 3)
print("Place battleship")
human.placeShips("B" , 4)
print("Place aircraft carrier")
human.placeShips("A" , 5)
human.printShipGrid()

print("Computer places ships now:")
computer = ComputerPlayer()
computer.placeShips("D" , 2)
computer.placeShips("C" , 3)
computer.placeShips("S" , 3)
computer.placeShips("B" , 4)
computer.placeShips("A" , 5)
computer.printShipGrid()


while(True):
    human.GuessShips(computer)
    computer.GuessShips(human)










