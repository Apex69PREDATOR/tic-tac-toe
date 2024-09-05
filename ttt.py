def display_board(board,pos=0,player=""):
    if player!="":
        pos-=1
        r=(pos)//3
        c=pos-(r*3)
        board[r][c]=player
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j<len(board[i])-1:
                    print(board[i][j],end=" |")
            else:
                print(board[i][j])
        if i<len(board)-1:
            for k in range(len(board[i])):
                if k<len(board[i])-1:
                    print("---",end="")
                else:
                    print("--")
def check_win(board,player):
    if (board[0][0]==player and board[0][1]==player and board[0][2]==player)or (board[1][0]==player and board[1][1]==player and board[1][2]==player) or (board[2][0]==player and board[2][1]==player and board[2][2]==player) or (board[0][0]==player and board[1][0]==player and board[2][0]==player) or (board[0][1]==player and board[1][1]==player and board[2][1]==player) or (board[0][2]==player and board[1][2]==player and board[2][2]==player) or (board[0][0]==player and board[1][1]==player and board[2][2]==player) or (board[0][2]==player and board[1][1]==player and board[2][0]==player):
        return True
    else:
        return False
        
def play_game():
    board=[["1","2","3"],["4","5","6"],["7","8","9"]]
    occupy=[]
    i=1
    while True:
        player1=input("player 1 select 'x' or 'o' : ")
        if player1=='x':
           player2='o'
           break
        elif player1=='o':
            player2='x'
            break
        else:
            print("Please select between 'x' and 'o'")
    print("player1 :"+player1+"\nplayer2 :"+player2)
    display_board(board)
    while True:
        if i%2!=0:
            print(f"player {player1}'s turn")
            player=player1
        
        else:
            print(f"player {player2}'s turn")
            player=player2
        while True:
            pos=int(input("select position : "))
            if pos>9 or pos<1:
                print("select indices between 1 and 9")
            elif pos not in occupy:
                occupy.append(pos)
                break
            else:
                print(f"position {pos} is been occupied selecet any other position")
        display_board(board,pos,player)
        if check_win(board,player)==True:
            print(f"player {player} wins")
            break
        i+=1
        if i>9:
            print("match drawn")
            break
if __name__=="__main__":
    play_game()