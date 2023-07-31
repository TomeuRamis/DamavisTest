from Node import Node

#Performable actions ordered by preference. Not mutable during runtime.
ACTIONS = ("down", "right", "rotate", "up", "left")
#Defines the length of each side of the rod. When RODLENGTH = 0, the "rod" is 1x1.
RODLENGTH = 1

#Static variables stored in the SolutionTracker
class SolutionTracker:
    movesSTR = "START"
    totalMoves = 0
    currentMoves = 0
    bestSolution = float("inf")
    bestPossibleSolution = -1

def solution(labyrinth):
    
    SolutionTracker.bestPossibleSolution = len(labyrinth) + len(labyrinth[0]) - 2 - RODLENGTH * 2 #Init Solution Tracker
    #Create visited matrixes
    SolutionTracker.visitedHorizontal = [[ False for x in range(len(labyrinth[0])) ] for y in range(len(labyrinth)) ]
    SolutionTracker.visitedVertical = [[ False for x in range(len(labyrinth[0])) ] for y in range(len(labyrinth)) ]
    SolutionTracker.visitedHorizontal[0][RODLENGTH] = True #Check initial position as visited

    solutionFound = SearchSolution(Node(0, RODLENGTH, True), labyrinth, 0) #Start recursive search with "rod" at [0,1] in Horizontal position
    
    #Check for no solution found
    if solutionFound == float("inf"):
        solutionFound = -1

    return solutionFound


def SearchSolution(node, labyrinth, moves):
    bestSolution = float("inf")

    #Check for end condition (solution node)
    if isSolution(node, labyrinth):
        SolutionTracker.movesSTR += ",GOAL"
        if(moves < SolutionTracker.bestSolution):
            SolutionTracker.bestSolution = moves
        return moves
    
    #Has the optimal solution been found?
    if bestSolutionFound():
        return bestSolution
    
    #Is the current solution worst that the current best solution?
    if isWorstSolution(moves):
        return bestSolution
    
    #Move or rotate the rod
    for action in ACTIONS:

        if(not isValid(node, action, labyrinth)): #If the action is allowed
            continue

        node.createChild(action)    #Create new node in the tree structure  
        goDeeper(node, action)
        partial = SearchSolution(node.getChild(action), labyrinth,  moves + 1)  #Use recursivity to search a solution node
        goBack(node.getChild(action))

        #Is this the best solution found yet?
        if(partial < bestSolution): 
            bestSolution = partial

    return bestSolution


# Check if the current solution being investigated is worst than the best solution found.
# This allows for a pruning of the search tree.
def isWorstSolution(moves):
    return moves >= SolutionTracker.bestSolution


# Check if the best possible solution has already been found.
# This allows for a rapid exit when the global optimum solution has been found.
def bestSolutionFound():
    return SolutionTracker.bestPossibleSolution == SolutionTracker.bestSolution


#Update the SolutionTracker variables and the Visited Matrixes
def goBack(node, ):
    SolutionTracker.movesSTR += ",BACK"
    SolutionTracker.currentMoves -= 1

    if(node.horizontal):
        SolutionTracker.visitedHorizontal[node.y][node.x] = False
    else:
        SolutionTracker.visitedVertical[node.y][node.x] = False


#Update the SolutionTracker variables and the Visited Matrixes
def goDeeper(node,action):
    SolutionTracker.movesSTR += ","+action
    SolutionTracker.currentMoves += 1
    SolutionTracker.totalMoves += 1

    if(node.horizontal):
        SolutionTracker.visitedHorizontal[node.y][node.x] = True
    else:
        SolutionTracker.visitedVertical[node.y][node.x] = True
    

# Check if the current rod position is a valid solution 
def isSolution(node, labyrinth):
    fx = len(labyrinth[0])-1    #Goal position X
    fy = len(labyrinth)-1       #Goal position Y

    if(node.horizontal):        #Rod position
        x = node.x + RODLENGTH
        y = node.y
    else:
        x = node.x
        y = node.y + RODLENGTH

    return (x == fx and y == fy)


# Check is the action is valid.
# Checks if the resulting position will collide with any walls or obstacles,
# if the rotation action has enough space available and
# if the resulting position has been visited before
def isValid(node, action, labyrinth):
    #Current position
    horizontal = node.horizontal
    x = node.x
    y = node.y

    #Calculate future position
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

    #Calculate left, right, top and bottom rod positions        
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

    #Check the 9x9 square for walls or obstacles
    if action == "rotate":
        for xi in range(x-RODLENGTH, x+RODLENGTH+1):
            for yi in range(y-RODLENGTH, y+RODLENGTH+1):
                if((xi < 0 or xi >= len(labyrinth[0])) or (yi < 0 or yi >= len(labyrinth)) or labyrinth[yi][xi] == "#"): 
                    return False    
                
    #Check if it will collide with any walls
    if((xl < 0 or xr >= len(labyrinth[0])) or (yt < 0 or yb >= len(labyrinth))): 
        return False
    
    #Check for obstacles
    for xi in range(xl, xr+1): #Obtstacles in the X axis
        if(labyrinth[y][xi] == "#"):
            return False
    for yi in range(yt, yb+1): #Obtstacles in the Y axis
        if(labyrinth[yi][x] == "#"):
            return False    

    if(horizontal and SolutionTracker.visitedHorizontal[y][x]):     #Has been visited in horizontal position
        return False
    elif(not horizontal and SolutionTracker.visitedVertical[y][x]): #Has been visited in vertical position
        return False

    return True

#labyrinth = [[".",".",".",".",".",".",".",".","."],
#            ["#",".",".",".","#",".",".",".","."],
#            [".",".",".",".","#",".",".",".","."],
#            [".","#",".",".",".",".",".","#","."],
#            [".","#",".",".",".",".",".","#","."]]

#print(solution(labyrinth))
