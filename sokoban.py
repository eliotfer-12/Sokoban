


play_boardbis= open("level1.xsb","r").read().strip().splitlines()
play_board=[]
for ligne in play_boardbis:
    a=[]
    for el in ligne:
        a.append(el)
    play_board.append(a)

def getPlayerPosition():
    print(play_board)
    x=0
    y=0
    for ligne in play_board :
        y+=1
        for el in ligne :
            if x==19:
                x=0
            x+=1
            if el=='@' :
                position=x,y
                return position
            
def isEmpty (position):
    x=position[0]
    y=position[1]
    if play_board[y][x]== '-' or '.':
        return True
    
    return False

def isBox (position):
    x=position[0]
    y=position[1]
    if play_board[y][x]== '$' or '*':
        return True
    
    return False

def Printboard ():
    for i in range (0,len(play_boardbis)):
        print(play_boardbis[i])


def player_box_movement () :
    command =input("Où veux-tu aller?")
    position = getPlayerPosition()
    d,v=position
    if command =="w":
        x,y = d, v-1
        goal2=x,y-1
    elif command =="s":
        x,y = d, v+1
        goal2=x,y+1
    elif command=="a":
        x,y = d-1, v
        goal2=x-1,y
    elif command=="d":
        x,y = d+1, v
        goal2=x+1,y
    else :
        return "action invalide, donne w a s ou d"

    goal=x,y

    
    if isEmpty(goal) :
        play_board[y][x]= "@"
        
    elif isBox(goal):
        if isEmpty(goal2):
            a,b=goal2
            play_board[y][x]="@"
            play_board[b][a]="$"
            
        else :
            return "la box que tu veux déplacer est face à un mur"
    
    else :
        return "Tu es face à un mur"
    
    if isBox(position):
        play_board[d][v]="."
    else :
        play_board[d][v]="-"

    return "OK"


b=4
while b!=0:
    action=player_box_movement()
    if action=="OK":
        Printboard()
    else:
        print(action)
        continue
    b=b-1






