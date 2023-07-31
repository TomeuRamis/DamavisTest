
class Node:
    def __init__(self, y, x, horizontal):
        self.x = x  #Position on the X axis
        self.y = y  #Position on the Y axis
        self.horizontal = horizontal  #Orientation of the rod
        self.children = [None]*5  #Children of this node
    
    def __str__(self):
        s1 = "Position ("+str(self.x)+","+str(self.y)+")\n"
        if(self.horizontal):
            s2 = "Position Horizontal"
        else:
            s2 = "Position Vertical"
        
        return s1 + s2

    #Create a child of the node based on the action to do
    def createChild(self, action):
        match action:
            case "up":
                self.children[0] = Node(self.y - 1,self.x, self.horizontal) 
            case "down":
                self.children[1] = Node(self.y + 1, self.x, self.horizontal) 
            case "right":
                self.children[2] = Node( self.y, self.x + 1, self.horizontal) 
            case "left":
                self.children[3] = Node(self.y, self.x - 1, self.horizontal) 
            case "rotate":
                self.children[4] = Node( self.y, self.x, not self.horizontal) 

    #Get the child based on the action
    def getChild(self, action):
        match action:
            case "up":
                return self.children[0]
            case "down":
                return self.children[1]
            case "right":
                return self.children[2]
            case "left":
                return self.children[3]
            case "rotate":
                return self.children[4]