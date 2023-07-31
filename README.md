# DamavisTest
Damavis coding test by Bartomeu Ramis.

# The challange
The goal is to carry the rod from the top left corner of the labyrinth to the bottom
right corner. This rod is not exactly the lightest thing you can imagine, so the
participant would naturally want to do it as fast as possible.

Find the minimal number of moves required to carry the rod through the labyrinth.
The labyrinth can be represented as a rectangular matrix, some cells of which are
marked as blocked, and the rod can be represented as a 1 × 3 rectangle. The rod
can't collide with the blocked cells or the walls, so it's impossible to move it into a
position in which one of its cells coincides with the blocked cell or the wall. The goal
is thus to move the rod into position in which one of its cells is in the bottom right
cell of the labyrinth.

There are 5 types of moves that the participant can perform: move the rod one cell
down or up, to the right or to the left, or to change its orientation from vertical to
horizontal and vice versa. The rod can only be rotated about its center, and only if the
3 × 3 area surrounding it is clear from the obstacles or the walls.
The rod is initially positioned horizontally, and its left cell lies in [0, 0].

# Solution
In order to find the optimal solution to this problem, it has been decided to use a tree structure with a recursive algorithm.
The tree strcutre, is made of Nodes. Each node holds the position of the rod in each instance, the orientation (Horizontal or Vertical) and 
the 5 posible children (each posible move: up, down, left, right and rotate).

Using this tree structure we used a recursive algorithm to explore all possible solutions and return the lowest number of moves needed to reach the goal.

To increase efficiency we created the SolutionTracker structure, which allows for some optimisations such as pruning and 
a rapid exit when finding the best solution (global minimum).

The labyrinth can be tested from the Labyrinth.py file uncomenting the last lines, where the variable labyrinth is defined and the method solution is called.
