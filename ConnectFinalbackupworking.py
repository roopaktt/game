Board=[[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]

ValidColumn=0
ValidRow=0
global WinnerFound
WinnerFound=False
def initialise():
    
    for row in range(0,5):
            for column in range(0,7):
                    print(Board[row][column],end=' ')
            print("")
def SetUpGame():
    global ThisPlayer
    ThisPlayer='#'
    global GameFinished
    GameFinished=False
    

def OutputBoard():
    print("Connect 4 Game ")
    for row in range(0,5):
            for column in range(0,7):
                    print(Board[row][column],end=' ')
            print(" ")
def ThisPlayerMakesMove():
    global ValidColumn
    global ValidRow
    ValidColumn=ThisPlayerChoosesColumn()
    ValidRow = FindNextFreePositionInColumn()
    Board[ValidRow][ValidColumn]=ThisPlayer
    
def ThisPlayerChoosesColumn():
    global ColumnNumber
    ColumnNumber=int(input("Input a valid column "))
    print("Player ",ThisPlayer)
    while ColumnNumberValid()!=True:
        print("Player ",ThisPlayer)
        ColumnNumber=int(input("Input a valid column "))
    return ColumnNumber
 
   
def ColumnNumberValid():
    Valid=False
    if ColumnNumber>= 0 and ColumnNumber<=6:
        if Board[0][ColumnNumber]==0:
            Valid=True
    return Valid

def FindNextFreePositionInColumn():
    global ThisRow
    ThisRow=4
    while Board[ThisRow][ValidColumn]!=0:
        ThisRow=ThisRow-1
    return ThisRow
def CheckIfThisPlayerHasWon():
    
    CheckHorizontalLineInValidRow()
    if WinnerFound==False:
        CheckVerticalLineInValidColumn()
    if WinnerFound == True:
        GameFinshed = True
        print(ThisPlayer," is the winner ")
    else:
        CheckForFullBoard()

def CheckHorizontalLineInValidRow():
    for i in range(4,0):
        if Board[ValidRow][i]==ThisPlayer and Board[ValidRow][i-1]==ThisPlayer and Board[ValidRow][i-2]==ThisPlayer and Board[ValidRow][i-3]==ThisPlayer:
            WinnerFound=True
            

def CheckVerticalLineInValidColumn():
    if ValidRow==4 or ValidRow==3 or ValidRow==2:
        if Board[ValidRow][ValidColumn]==ThisPlayer and Board[ValidRow-1][ValidColumn]==ThisPlayer and Board[ValidRow-2][ValidColumn]==ThisPlayer and Board[ValidRow-3][ValidColumn]==ThisPlayer:
            WinnerFound=True
            

  
def SwapThisPlayer():
    global ThisPlayer
    if ThisPlayer=='#':
        ThisPlayer='*'
    else:
        ThisPlayer='#'
          
def CheckForFullBoard():
    BlankFound=False
    ThisRow=4
    ThisColumn=6
    while ThisColumn==0 or BlankFound==True:
        ThisRow=ThisRow-1
        while ThisRow==0 or BlankFound==True:
            ThisColumn = ThisColumn+1
            if Board[ThisRow][ThisColumn]==0:
                BlankFound=True
    if BlankFound==False:
        print("It is a draw")
        GameFinished=True
    


print("Connect 4 Game ")
def main():
    
    SetUpGame()
    OutputBoard()
    while GameFinished==False:
        print("valid Row ",ValidRow)
        ThisPlayerMakesMove()
        OutputBoard()
        CheckIfThisPlayerHasWon()
        if GameFinished==False:
            SwapThisPlayer()
            print("Column Numbe ",ColumnNumber)
            
       
    
main()
    

