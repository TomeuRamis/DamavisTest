from Node import Node

#Performable actions ordered by preference. Not mutable during runtime.
ACTIONS = ("down", "right", "rotate", "up", "left")
#Defines the length of each side of the rod. When RODLENGTH = 0, the "rod" is 1x1.
RODLENGTH = 1


class SolutionTracker:
    movesSTR = ""
    totalMoves = 0
    currentMoves = 0
    bestSolution = float("inf")
    bestPossibleSolution = -1

def solution(labyrinth):

    SolutionTracker.movesSTR += "START"
    SolutionTracker.bestPossibleSolution = len(labyrinth) + len(labyrinth[0]) - 2 - RODLENGTH*2

    root = Node(1, 0, True)
    bestSolution = SearchSolution(root, 0)
    print("Best Solution: "+str(bestSolution))


def SearchSolution(node, moves):
    bs = float("inf")

    if bestSolutionFound():
        return bs
    
    #Check for end condition
    if isSolution(node):
        SolutionTracker.movesSTR += ",GOAL"
        if(moves < SolutionTracker.bestSolution):
            SolutionTracker.bestSolution = moves
        return moves
    
    if isWorstSolution(moves):
        return bs
    
    for action in ACTIONS:
        if(not isValid(node, action)):
            continue

        node.createChild(action)
        goDeeper(node, action)
        partial = SearchSolution(node.getChild(action), moves + 1)
        goBack(node.getChild(action))
        if(partial < bs):
            bs = partial

    return bs

def isWorstSolution(moves):
    return moves >= SolutionTracker.bestSolution

def bestSolutionFound():
    return SolutionTracker.bestPossibleSolution == SolutionTracker.bestSolution

def goBack(node):
    SolutionTracker.movesSTR += ",BACK"
    SolutionTracker.currentMoves -= 1

    if(node.horizontal):
        visitedHorizontal[node.y][node.x] = False
    else:
        visitedVertical[node.y][node.x] = False

def goDeeper(node,action):
    SolutionTracker.movesSTR += ","+action
    SolutionTracker.currentMoves += 1
    SolutionTracker.totalMoves += 1

    if(node.horizontal):
        visitedHorizontal[node.y][node.x] = True
    else:
        visitedVertical[node.y][node.x] = True
    
def isSolution(node):
    fx = len(labyrinth[0])-1     #Goal position X
    fy = len(labyrinth)-1  #Goal position Y

    if(node.horizontal):    #Rod position
        x = node.x + RODLENGTH
        y = node.y
    else:
        x = node.x
        y = node.y + RODLENGTH

    return (x == fx and y == fy)

def isValid(node, action):
    
    horizontal = node.horizontal
    x = node.x
    y = node.y
    
    match action:
        case "up":
            y = y - 1
        case "down":
            y = y + 1
        case "right":
            x = x + 1
        case "left":
            x = x - 1
        case "rotate":
            horizontal = not horizontal
            
    if(horizontal):
        xl = x-RODLENGTH
        xr = x+RODLENGTH
        yt = y
        yb = y
    else:
        xl = x
        xr = x
        yt = y-RODLENGTH
        yb = y+RODLENGTH

    if action == "rotate":
        #Check the 9x9 square for walls or obstacles
        for xi in range(x-RODLENGTH, x+RODLENGTH+1):
            for yi in range(y-RODLENGTH, y+RODLENGTH+1):
                if((xi < 0 or xi >= len(labyrinth[0])) or (yi < 0 or yi >= len(labyrinth)) or labyrinth[yi][xi] == "#"): 
                    return False    
    
    if((xl < 0 or xr >= len(labyrinth[0])) or (yt < 0 or yb >= len(labyrinth))): #Is within constraints
        return False
    
    #Check for obstacles
    for xi in range(xl, xr+1): #Obtstacles in the X axis
        if(labyrinth[y][xi] == "#"):
            return False
    for yi in range(yt, yb+1): #Obtstacles in the Y axis
        if(labyrinth[yi][x] == "#"):
            return False    

    if(horizontal and visitedHorizontal[y][x]): #Has been visited in horizontal position
        return False
    elif(not horizontal and visitedVertical[y][x]):    #Has been visited in vertical position
        return False

    return True

labyrinth = [[".",".",".",".",".",".",".",".",".","."],
            [".","#",".",".",".",".","#",".",".","."],
            [".","#",".",".",".",".",".",".",".","#"],
            [".",".",".",".",".",".",".",".","#","."],
            [".",".",".",".",".",".",".","#",".","."],
            [".","#","#","#","#",".","#",".",".","."],
            [".","#",".",".",".","#",".",".",".","."],
            [".",".",".",".",".",".","#",".",".","."],
            [".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".","."]]
#Init visited matrix
visitedHorizontal = [[ False for x in range(len(labyrinth[0])) ] for y in range(len(labyrinth)) ]
visitedVertical = [[ False for x in range(len(labyrinth[0])) ] for y in range(len(labyrinth)) ]
visitedHorizontal[0][1] = True

solution(labyrinth)