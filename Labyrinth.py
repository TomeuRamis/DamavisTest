from Node import Node
#Performable actions ordered by preference. Not mutable during runtime.
actions = ("down", "right", "up", "left")

Depth = 0
bestSolution = float("inf")


def solution(labyrinth):
    root = Node(1, 0, True)
    bestSolution = SearchSolution(root, 0)
    print("Best Solution: "+str(bestSolution))

def SearchSolution(node, moves):
    bs = float("inf")
    #Check for end condition
    if isSolution(node):
        return moves
    
    for action in actions:
        if(not isValid(node, action)):
            continue

        node.createChild(action)
        moves = SearchSolution(node.getChild(action), moves + 1)
        if(moves < bs):
            bs = moves
    
    return bs

    
def isSolution(node):
    fx = len(labyrinth[0])-1     #Goal position X
    fy = len(labyrinth)-1  #Goal position Y

    if(node.horizontal):    #Rod position
        x = node.x + 1
        y = node.y
    else:
        x = node.x
        y = node.y + 1

    return (x == fx and y == fy)

def isValid(node, action):
    if action == "rotate":
        #TODO check if posible
        print("Rotate")

    match action:
        case "up":
            x = node.x
            y = node.y - 1
        case "down":
            x = node.x
            y = node.y + 1
        case "right":
            x = node.x + 1
            y = node.y
        case "left":
            x = node.x - 1
            y = node.y
            
    if(node.horizontal):
        xl = x-1
        xr = x+1
        yt = y
        yb = y
    else:
        xl = x
        xr = x
        yt = y-1
        yb = y+1

    if((xl < 0 or xr >= len(labyrinth[0])) or (yt < 0 or yb >= len(labyrinth))): #Is within constraints
        return False
    
    #TODO check for obstacles

    if(node.horizontal and visitedHorizontal[y][x]): #Has been visited in horizontal position
        return False
    elif(not node.horizontal and visitedVertical[y][x]):    #Has been visited in vertical position
        return False
    
    if(node.horizontal):
        visitedHorizontal[y][x] = True
    else:
        visitedVertical[y][x] = True
    return True

labyrinth = [[".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."]]

#Init visited matrix
visitedHorizontal = [[ False for x in range(len(labyrinth[0])) ] for y in range(len(labyrinth)) ]
visitedVertical = [[ False for x in range(len(labyrinth[0])) ] for y in range(len(labyrinth)) ]
visitedHorizontal[0][1] = True

solution(labyrinth)