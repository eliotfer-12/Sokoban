


play_boardbis= open("level1.xsb","r").read().strip().splitlines()
play_board=[]
for ligne in play_boardbis:
    a=[]
    for el in ligne:
        a.append(el)
    play_board.append(a)

def getPlayerPosition():
    x=-1
    y=-1
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
    if play_board[y][x]== '-' or play_board[y][x]=='.':
        return True
    
    return False

def isBox (position):
    x=position[0]
    y=position[1]
    if play_board[y][x]== '$' or play_board[y][x]=='*':
        return True
    
    return False

def Printboard ():
    for ligne in play_board:
        for el in ligne :
            print(el,end="")
        print("",end="\n")


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
    elif command=="q":
        return "Quit"
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
        play_board[v][d]="."
    else :
        play_board[v][d]="-"

    return "OK"


while True:
    action=player_box_movement()
    if action=="OK":
        Printboard()
    elif action=="Quit":
        print("La partie est terminée")
        break
    else:
        print(action)
        continue
    






