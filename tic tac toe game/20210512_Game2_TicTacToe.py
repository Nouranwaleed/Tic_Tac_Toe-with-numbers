print("TIC-TAC-TOE")
print("Player 1 must insert an odd number from (1,3,5,7,9)")
print("Player 2 must insert an even number from (0,2,4,6,8)")
print("Use are allowed to use each number only once")

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

player = "1"

def Tic_Tac_Toe ():
    print ("|" ,board[0],"|",board[1] ,"|", board[2],"|")
    print (".............")
    print ("|" ,board[3],"|",board[4] ,"|", board[5],"|")
    print (".............")
    print ("|" ,board[6],"|",board[7] ,"|", board[8],"|")

def win():
    if (board[0]+board[1]+board[2]==15):
          print ("CONGRATULATIONS YOU WON!")
          return True
    if (board[0]+board[3]+board[6]==15):
          print ("CONGRATULATIONS YOU WON!")
          return True
    if (board[1]+board[4]+board[7]==15):
          print ("CONGRATULATIONS YOU WON!")
          return True
    if (board[3]+board[4]+board[5]==15):
          print ("CONGRATULATIONS YOU WON!")
          return True
    if (board[2]+board[5]+board[8]==15):
          print ("CONGRATULATIONS YOU WON!")
          return True
    if (board[6]+board[7]+board[8]==15):
          print ("CONGRATULATIONS YOU WON!")
          return True
    if (board[0]+board[4]+board[8]==15):
          print ("CONGRATULATIONS YOU WON!")
          return True
    if (board[2]+board[4]+board[6]==15):
          print ("CONGRATULATIONS YOU WON!")
          return True
    else: return False

def Insert(x1,x2):
    board[x2] = x1
    Tic_Tac_Toe()

def odd (x, x2):
    while  (x%2==0):
        x = int(input ("Please enter an odd number: "))
    Insert (x ,x2)      

def even (x ,x2) :
    while  (x%2!=0):
        x = int(input ("Please enter an even number: "))
    Insert (x ,x2)        

def Turn(s):
    print ("Player " + s +" turn")
    x = int (input ("Please enter a number: "))
    x1 = int (input ("Please enter number's place: "))
    if player == "1":
        odd(x, x1)
    else: even(x, x1)          

Tic_Tac_Toe ()
while (True):
    Turn(player)
    if win(): break
    else:
        if player == "1": player = "2"
        else: player = "1"

