from queue import PriorityQueue
from copy import deepcopy

SIDE = 3
puzzleSize = SIDE * SIDE  


class Node:
    def __init__(self, state, parent, operator, g, h):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.g = g
        self.h = h
        self.f = self.g + self.h
        if parent is None:
            self.moves = operator
        else:
            self.moves = parent.moves + '-' + operator

    def __lt__(self, other):
        return self.f < other.f


def ASTAR(start_node):

    OPEN = PriorityQueue()
    OPEN.put((start_node.f, start_node))
    CLOSED = []
    search_cnt = 0
    expand_cnt = 0
    while not (OPEN.empty()):
        search_cnt += 1
        node = OPEN.get()[1]

        if goaltest(node.state):
            print("search count => ",search_cnt)
            print("expand count => ",expand_cnt)
            return node

        for i in expand(node):
            if not i.state in CLOSED:
                OPEN.put((i.f,i))
                expandcnt += 1
        CLOSED.append(node.state)

    return None


def goaltest(state):
    if state == goal_state:
        return 1
    else:
        return 0


def heuristic(state):
    return sum([abs(state.index(i)//3-goal_state.index(i)//3) + abs(state.index(i)%3-goal_state.index(i)%3) for i in range(1,9)])


def expand(node):
    nodeList = []
    state = node.state
    blank = state.index(0)  # location of blank
    row = int(blank / SIDE)
    col = blank % SIDE

    # up
    if not (row == 0):
        child_state = deepcopy(state)
        child_state[blank] = child_state[blank - SIDE]
        child_state[blank - SIDE] = 0
        nodeList.append(Node(child_state, node, "U", node.g + 1, heuristic(child_state)))
    # down
    if not (row == SIDE - 1):
        child_state = deepcopy(state)
        child_state[blank] = child_state[blank + SIDE]
        child_state[blank + SIDE] = 0
        nodeList.append(Node(child_state, node, "D", node.g + 1, heuristic(child_state)))
    # left
    if not (col == 0):
        child_state = deepcopy(state)
        child_state[blank] = child_state[blank - 1]
        child_state[blank - 1] = 0
        nodeList.append(Node(child_state, node, "L", node.g + 1, heuristic(child_state)))
    # right
    if not (col == SIDE - 1):
        child_state = deepcopy(state)
        child_state[blank] = child_state[blank + 1]
        child_state[blank + 1] = 0
        nodeList.append(Node(child_state, node, "R", node.g + 1, heuristic(child_state)))

    return nodeList


def print_state(state):
    for i in range(3):
        for j in range(3):
            print(state[i * 3 + j], end="\t")
        print("")
    print("")


def print_solution_path(node):
    if (node == None): return
    print_solution_path(node.parent)
    print_state(node.state)

start_state = [1, 2, 3,
              8, 0, 4,
              7, 6, 5]
goal_state = [7, 8, 1,
             6, 0, 2,
             5, 4, 3]

print("Start state")
print_state(start_state)
print("Goal state")
print_state(goal_state)

start_node = Node(start_state, None, "Start", 0, heuristic(start_state))
print("Start A* search")
goal_node = ASTAR(start_node)
print(" Finished")


if (goal_node == None):
    print("A* Failed ")
else:
    print("A* Succeeded ")
    print("solution path: ", goal_node.moves)
    print_solution_path(goal_node)
