#Performable actions ordered by preference. Not mutable during runtime.
actions = frozenset(["right", "down", "rotate", "up", "left"])

class Node:
    def __init__(self, x, y, horizontal):
        self.x = x  #Position on the X axis
        self.y = y  #Position on the Y axis
        self.horizontal = horizontal  #Orientation of the rod
        self.children = []  #Children of this node
    
    def createChild(self, action):
        match action:
            case "up":
                self.children[0] = Node(self + 1, self.y, self.horizontal) 
            case "down":
                self.children[1] = Node(self.x - 1, self.y, self.horizontal) 
            case "right":
                self.children[2] = Node(self.x, self.y + 1, self.horizontal) 
            case "left":
                self.children[3] = Node(self.x, self.y - 1, self.horizontal) 
            case "rotate":
                self.children[4] = Node(self.x, self.y, not self.horizontal) 




