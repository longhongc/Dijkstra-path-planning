import numpy as np
from queue import PriorityQueue

class Node:
    def __init__(self, pos=(0, 0), parent=None): 
        self.pos = pos
        self.parent = parent
        self.cost = 0

class Dijkstra: 
    def __init__(self, init_pos, goal_pos):
        self.queue = []
        # use set for faster checking visited 
        self.visited = set()

        init_node = Node(state=init_state)
        self.add_node(init_pos)

        self.init_pos = init_pos
        self.goal_pos = goal_pos

    def add_node(self, node): 
        pass

    def find_child_nodes(self, node): 
        action_sets = [(-1, 1), (0, 1), (1, 1),
                       (-1, 0),         (1, 0),
                       (-1,-1), (0,-1), (1,-1)]
        pass

    def search(self):
        pass

class Map:
    #mm
    width = 400 
    height = 250 
    
    def __init__(self, start, goal):
        pass

    @classmethod
    def is_obstacle(self, pos): 
        occupancy_grid_map = np.zeros((Map.width, Map.height))

        # ax+by+d=0
        def create_line(p1, p2):
            assert(p1!=p2),"point1 equals to point2, cannot form line"

            tangent_vector = (p2[0]-p1[0], p2[1]-p1[1])
            if (tangenet_vector[0]==0):
                normal_vector = (1,0)
            elif (tangenet_vector[1]==0): 
                normal_vector = (0,1)
            else:
                normal_vector = (1/(p2[0]-p1[0]), -1/(p2[1]-p1[1]))
            a, b = normal_vector
            d = -(a * p1[0] + b * p1[1])
            return a, b, d

        #def form_obstacle()
        return False

    def solve(self): 
        pass

def start_simulation(): 
    success = False
    while (not success):
        # read input
        print("map width: 400, map height: 250")
        print("The robot is a circle with radius 5")
        print("Enter a start and goal point in the map")

        start_x = int(input("Start x:"))
        start_y = int(input("Start y:"))
        start = (start_x, start_y)

        goal_x = int(input("Goal x:"))
        goal_y = int(input("Goal y:"))
        goal = (goal_x, goal_y)

        print("Start pos: ({}, {})".format(start_x, start_y))
        print("Goal pos: ({}, {})".format(goal_x, goal_y))

        success = True

        if (Map.is_obstacle(start)):
            print("This start point is not valid.")
            success = False
        if (Map.is_obstacle(goal)):
            print("This goal point is not valid.")
            restart = False
        print("---")

    return start, goal

# ax+by+d=0
def create_line(p1, p2):
    assert(p1!=p2),"point1 equals to point2, cannot form line"

    tangent_vector = (p2[0]-p1[0], p2[1]-p1[1])
    if (tangent_vector[0]==0):
        normal_vector = (1,0)
    elif (tangent_vector[1]==0): 
        normal_vector = (0,1)
    else:
        normal_vector = (1/(p2[0]-p1[0]), -1/(p2[1]-p1[1]))
    a, b = normal_vector
    d = -(a * p1[0] + b * p1[1])
    return a, b, d

if __name__ == "__main__":
    start, goal = start_simulation()
    my_map = Map(start, goal)
    a, b, d = create_line(start, goal)
    print(a)
    print(b)
    print(d)
    print(a*start[0]+b*start[1]+d)
    print(a*goal[0]+b*goal[1]+d)



