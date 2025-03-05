class SokobanModel :
    def __init__(self):
        self.board = []

    def load (self, level_data):
        for ligne in level_data:
            a=[]
            for el in ligne:
                a.append(el)
            self.board.append(a)
        return self.board 

    def getPlayerPosition(self):
        for k in range(len(self.board)) :
            for i in range(len(self.board[k])) :
                if self.board[k][i]=='@' or self.board[k][i]=='*' :
                    self.position=i,k
                    return self.position

    def isEmpty (self, position):
        x=position[0]
        y=position[1]
        if self.board[y][x]== '-' or self.board[y][x]=='.':
            return True
        return False
    
    def isBox (self, position):
        x=position[0]
        y=position[1]
        if self.board[y][x]== '$' or self.board[y][x]=='*':
            return True
        return False
    
    def move (self, dx, dy):
        position= self.getPlayerPosition()
        x,y=position
        goal = x+dx,y+dy 
        d,v =goal
        goal2 = x+2*dx, y+2*dy 

        if self.isEmpty(goal) :
            if self.board[v][d]== "-":
                self.board[v][d]="@"
            else :
                self.board[v][d]="*"
            
        elif self.isBox(goal):
            if self.isEmpty(goal2):
                a,b=goal2
                self.board[v][d]="@"
                self.board[b][a]="$"
                
            else :
                return "la box que tu veux déplacer est face à un mur"
            
        
        
        else :
            return "Tu es face à un mur"
        
        if self.isBox(position):
            self.board[y][x]="."
        else :
            self.board[y][x]="-"

        return "OK"
    


class SokobanView :
    def __init__(self):
        self.play_board=[]
    def print (self,model):
        for ligne in model.board:
            for el in ligne :
                print(el,end="")
            print("",end="\n")




class SokobanController :
    def __init__(self):
        self.model = SokobanModel()
        self.view =SokobanView()

    def readfile (self, file):
        x = open(file,"r").read().strip().splitlines()
        self.model.load(x)
        

    def loop (self):
        while True :
            self.view.print(self.model)
            command =input("Où veux-tu aller?")
            
            if command =="w":
                dx=0
                dy=-1
            elif command =="s":
                dx=0
                dy=1
            elif command=="a":
                dx=-1
                dy=0
            elif command=="d":
                dx=1
                dy=0
            elif command=="q":
                break
            else :
                print("action invalide, donne w a s ou d")
                continue

            a=self.model.move(dx,dy)
            print(a)


sokoban = SokobanController()
sokoban.readfile("level1.xsb")
sokoban.loop()




    


