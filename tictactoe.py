import random;

def printBoard():
    for x in range(rows):
        print("\n+---+---+---+");
        print("|", end="");
        for y in range(columns):
            print("", board[x][y], end=" |")
    print("\n+---+---+---+");

def modifyArray(num, turn):
    num -= 1;
    if (num==0):
        board[0][0]=turn;
    elif(num==1):
        board[0][1]=turn;
    elif(num==2):
        board[0][2]=turn;
    elif(num==3):
        board[1][0]=turn;
    elif(num==4):
        board[1][1]=turn;
    elif(num==5):
        board[1][2]=turn;
    elif(num==6):
        board[2][0]=turn;
    elif(num==7):
        board[2][1]=turn;
    elif(num==8):
        board[2][2]=turn;

def checkWinner(board):
#Horizontal winner
    if(board[0][0] == "X" and  board[0][1] =="X" and board[0][2] == "X"):
        print("X is the winner");
        return "X";

    elif(board[0][0] == "O" and  board[0][1] =="O" and board[0][2] == "O"):
        print("O is the winner");
        return "O";

    elif(board[1][0] == "X" and  board[1][1] =="X" and board[1][2] == "X"):
        print("X is the winner");
        return "X";

    elif(board[1][0] == "O" and  board[1][1] =="O" and board[1][2] == "O"):
        print("O is the winner");
        return "0";

    elif(board[2][0] == "X" and  board[2][1] =="X" and board[2][2] == "X"):
        print("X is the winner");
        return "X";

    elif(board[2][0] == "O" and  board[2][1] =="O" and board[2][2] == "O"):
        print("O is the winner");
        return "O";

#Vertical winner 
    
    elif(board[0][0] == "X" and  board[1][0] =="X" and board[2][0] == "X"):
        print("X is the winner");
        return "X";

    elif(board[0][0] == "O" and  board[1][0] =="O" and board[2][0] == "O"):
        print("O is the winner");
        return "O";

    elif(board[0][1] == "X" and  board[1][1] =="X" and board[2][1] == "X"):
        print("X is the winner");
        return "X";

    elif(board[0][1] == "O" and  board[1][1] =="O" and board[2][1] == "O"):
        print("O is the winner");
        return "O";

    elif(board[0][2] == "X" and  board[1][2] =="X" and board[2][2] == "X"):
        print("X is the winner");
        return "X";

    elif(board[0][2] == "O" and  board[1][2] =="O" and board[2][2] == "O"):
        print("O is the winner");
        return "O";

# Diagonal winner
    elif(board[0][0] == "X" and  board[1][1] =="X" and board[2][2] == "X"):
        print("X is the winner");
        return "X";

    elif(board[0][0] == "O" and  board[1][1] =="O" and board[2][2] == "O"):
        print("O is the winner");
        return "O";
    
    elif(board[0][2] == "X" and  board[1][1] =="X" and board[2][0] == "X"):
        print("X is the winner");
        return "X";

    elif(board[0][2] == "O" and  board[1][1] =="O" and board[2][0] == "O"):
        print("O is the winner");
        return "O";

    else: 
        return "N";


print("Welcome to Tic Tac Toe");

possibleNumbers= [1,2,3,4,5,6,7,8,9];
board=[[1,2,3], [4,5,6], [7,8,9]];
rows =3;
columns=3;
gameEnd= False;
turn="X";
turnCounter=0;

while(gameEnd == False):
    if(turnCounter % 2 == 0):
        printBoard();
        numberpicked = int(input("\nChoose a number from 1-9: "));
        if(numberpicked >=1 and numberpicked <= 9):
            modifyArray(numberpicked,"X");
            possibleNumbers.remove(numberpicked);
            turnCounter+=1;
        else:
            print("Invalid number. Please try again")

#Computers turn
    else:
        while(True):
            computerChoice = random.choice(possibleNumbers);
            print("\nComputer choice: ", computerChoice);
            if(computerChoice in possibleNumbers):
                modifyArray(computerChoice,"O");
                possibleNumbers.remove(computerChoice);
                turnCounter+=1;
                break;
    winner = checkWinner(board)
   
    if(winner != "N"):
        printBoard();
        print("\nGame over! Thank you for playing :)");
        break;
    
    if (winner == "N" and turnCounter == 9):
        printBoard();
        print("\nIt's a tie! Thanks for playing :)");
        gameEnd=True;
    

