import random

#Class that defines the individual pieces of a player
class Piece:
    tile = 0

    def __init__(self, name):
        self.name = name

    def getPieceName(self):
        return self.name


#Defines the user player and the AI player
class Player:

    def __init__(self, name, tile):
        self.name = name
        self.tile = tile
        self.Piece1 = Piece('Piece 1')
        self.Piece2 = Piece('Piece 2')
        self.Piece3 = Piece('Piece 3')

    #Multiple getters and setters for the tile, pieces, and player name.
    def setTile(piece, tile):
        piece.tile = tile

    def addTile(piece, spaces):
        piece.tile += spaces

    def getName(self):
        return self.name
    
    def getPieceOne(self):
        return self.Piece1
    
    def getPieceTwo(self):
        return self.Piece2

    def getPieceThree(self):
        return self.Piece3

    def getTile(piece):
        return piece.tile

    def printName(self):
        print(self.name)


def GameBoard(player, piece):
    tileNum = piece.tile

    #Depending on the value of the tile, any of these cases may happen that may change the value.
    if tileNum == 3:
        print("You landed on a fan! It carries you to tile 13!")
        piece.tile = 13
        print(f"{player.name}'s {piece.getPieceName()} is now at tile {piece.tile}")
        #print(player.name + "'s " + piece.getPieceName() + " is now at tile " + str(piece.tile) + ".")
    elif tileNum == 11:
        print("Oh no! You landed on a duct! You fall back to tile 5.")
        piece.tile = 5
        print(f"{player.name}'s {piece.getPieceName()} is now at tile {piece.tile}")
    elif tileNum == 12:
        print("You landed on a fan! It carries you to tile 25!")
        piece.tile = 25
        print(f"{player.name}'s {piece.getPieceName()} is now at tile {piece.tile}")
    elif tileNum == 14:
        print("Horrible! You landed on a teleporter! It transports you back to the beginning...")
        piece.tile = 0
        print(f"{player.name}'s {piece.getPieceName()} is now at tile {piece.tile}")
    elif tileNum == 16:
        print("You landed on a fan! It carries you to tile 21!")
        piece.tile = 21
        print(f"{player.name}'s {piece.getPieceName()} is now at tile {piece.tile}")
    elif tileNum == 24:
        print("Horrible! You landed on a teleporter! It transports you back to the beginning...")
        piece.tile = 0
        print(f"{player.name}'s {piece.getPieceName()} is now at tile {piece.tile}")
    elif tileNum == 26:
        print("Oh no! You landed on a duct! You fall back to tile 18.")
        piece.tile = 18
        print(f"{player.name}'s {piece.getPieceName()} is now at tile {piece.tile}")
    elif tileNum >= 28:
        print(f"{player.name}'s {piece.getPieceName()} got to the end of the board!")
    else:
        print(f"{player.name}'s {piece.getPieceName()} is now at tile {piece.tile}")



def rollDice():
    #Rolls the dice to get a number between 1-4 and uses that as the amount of spaces a piece can move.
    roll = random.randrange(1, 5)

    print(f"You rolled a {roll}!")    
    return roll

def rollOption():
    #Makes the decisions for the AI. This controls which piece it will move.
    roll2 =  random.randrange(1,4)
    return roll2

def playerPieces(player):
    #Prints the piece locations of the give player object.
    print(f"{player.name}'s Pieces")
    print(f"""
        -----------------
        Piece 1: {player.Piece1.tile}
        Piece 2: {player.Piece2.tile}
        Piece 3: {player.Piece3.tile}
        -----------------
        """)

#When this becomes, false, the game ends.
gameStatus = True

print("Enter your name!")

inputName = str(input())

#print("What difficulty would you like? (Enter 'easy' 'medium' or 'hard')")
#print("WARNING: Diffculty cannot be changed mid-game.")
#difficulty = str(input())

Player1 = Player(inputName, 0)
Player2 = Player('AI', 0)

#This determines whose turn it is. When 1, it is the user's turn. When it is 2, it is the AI's turn.
playerTurn = 1

#The object of the game is to get all 3 of a player's piece to at least tile 28.
#When a piece is >= 28, a player cannot select that piece
#The game ends when all 3 pieces of an individual player reacges the end.
while (gameStatus):
    if playerTurn == 1:
        numSpaces = rollDice()
        #Second while loop was made so that when a person inputs 'info', we can enable 'continue' to not reroll the dice.
        while (playerTurn == 1):
            print("Move which piece? (Enter '1', '2', or '3')")
            print("Rules and information? (Enter 'info')")
            print("Enter 'end' to exit the game.")
            userInput = str(input())
            if userInput == 'info' or userInput == 'Info':
                print("""
                Get all three of your pieces to tile 28; the end of the board!
            
                There are special tiles called 'Fans', 'Teleporters', and 'Ducts'
                Fans move pieces forward, ducts move pieces backward, and teleporters send you back to the start.
            
                Fans are on tiles: 3, 12, and 16
                Ducts are on tiles: 11, and 26
                Teleporters are on tiles: 14 and 24
                """) 
                
                #continue
            elif userInput == '1':
                if Player1.Piece1.tile < 28:
                    Player1.Piece1.tile += numSpaces
                    GameBoard(Player1, Player1.Piece1)
                    playerTurn = 2
                    playerPieces(Player1)
                else:
                    print("This piece is already at the end. Enter a different piece.")
            elif userInput == '2':
                if Player1.Piece2.tile < 28:
                    Player1.Piece2.tile +=  numSpaces
                    GameBoard(Player1, Player1.Piece2)
                    playerTurn = 2
                    playerPieces(Player1)
                else:
                    print("This piece is already at the end. Enter a different piece.")
            elif userInput == '3':
                if Player1.Piece3.tile < 28:
                    Player1.Piece3.tile +=  numSpaces
                    GameBoard(Player1, Player1.Piece3)
                    playerTurn = 2
                    playerPieces(Player1)
                else:
                    print("This piece is already at the end. Enter a different piece.")
            elif userInput == 'end' or userInput =='End':
                gameStatus = False
                break
            else:
                print("Invalid input: Please try again.")

            if Player1.Piece1.tile >= 28 and Player1.Piece2.tile >= 28 and Player1.Piece3.tile >= 28:
                print(f'{Player1.name} got all of their pieces to the end! {Player1.name} won!')
                gameStatus = False

        

    elif playerTurn == 2:
        AIAction = rollOption()
        print("Player 2 rolls the dice!")
        if AIAction == 1 and Player2.Piece1.tile < 28:
            Player2.Piece1.tile += rollDice()
            GameBoard(Player2, Player2.Piece1)
            playerTurn = 1
            playerPieces(Player2)
        elif AIAction == 2 and Player2.Piece2.tile < 28:
            Player2.Piece2.tile += rollDice()
            GameBoard(Player2, Player2.Piece2)
            playerTurn = 1
            playerPieces(Player2)
        elif AIAction == 3 and Player2.Piece3.tile < 28:
            Player2.Piece3.tile += rollDice()
            GameBoard(Player2, Player2.Piece3)
            playerTurn = 1
            playerPieces(Player2)
        else:
            continue

        if Player2.Piece1.tile >= 28 and Player2.Piece2.tile >= 28 and Player2.Piece3.tile >= 28:
            print(f"{Player2.name} got all of their pieces to the end! {Player2.name} won!")
            gameStatus = False

