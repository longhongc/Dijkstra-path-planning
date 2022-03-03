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
        #def form_obstacle()
        return False

    def solve(self): 
        pass

def start_simulation(): 
    success=False
    while (not success):
        # read input
        print("map width: 400, map height: 250")
        print("The robot is a circle with radius 5")
        print("Enter a start and goal point in the map")

        start_x = input("Start x:")
        start_y = input("Start y:")
        start = (start_x, start_y)

        goal_x = input("Goal x:")
        goal_y = input("Goal y:")
        goal = (goal_x, goal_y)

        print("Start pos: ({}, {})".format(start_x, start_y))
        print("Goal pos: ({}, {})".format(goal_x, goal_y))

        if (not Map.is_obstacle(start)):
            print("This start point is not valid.")
            success = False
        if (not Map.is_obstacle(goal)):
            print("This goal point is not valid.")
            restart = False
        print("---")

    return start, goal

if __name__ == "__main__":
    start, goal = start_simulation()
    my_map = Map(start, goal)



