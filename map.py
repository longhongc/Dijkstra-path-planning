import numpy as np
from queue import PriorityQueue

from utils import *

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
    occupancy_grid_map = np.zeros((height+1, width+1))
    
    def __init__(self, start, goal):
        pass

    @classmethod
    def form_obstacle_map(self): 
        # boundary
        b_line1 = create_line((0,0), (0,250))
        b_line2 = create_line((0,250), (400,250))
        b_line3 = create_line((400,250), (400,0))
        b_line4 = create_line((0,0), (400,0))

        # hexagon
        edge = np.tan(np.pi/6) * 70 
        h_line1 = create_line((165, 100 + edge/2), (165, 100 - edge/2))
        h_line2 = create_line((165, 100 + edge/2), (200, 100 + edge))
        h_line3 = create_line((200, 100 + edge), (235, 100 + edge/2))
        h_line4 = create_line((235, 100 + edge/2), (235, 100 - edge/2))
        h_line5 = create_line((200, 100 - edge), (235, 100 - edge/2))
        h_line6 = create_line((165, 100 - edge/2), (200, 100 - edge))

        print(h_line6)

        rows, cols = Map.occupancy_grid_map.shape 
        for i in range(0, rows):
            for j in range(0, cols): 
                # transform from top-left (0,0) to bottom-left (0,0)
                x = j
                y = rows - 1 - i

                # boundary
                if ((b_line1[0] * x + b_line1[1] * y + b_line1[2]) <= 0 or \
                    (b_line2[0] * x + b_line2[1] * y + b_line2[2]) >= 0 or \
                    (b_line3[0] * x + b_line3[1] * y + b_line3[2]) >= 0 or \
                    (b_line4[0] * x + b_line4[1] * y + b_line4[2]) <= 0 ): 
                    Map.occupancy_grid_map[i, j]=1

                # hexagon
                if ((h_line1[0] * x + h_line1[1] * y + h_line1[2]) >= 0 and \
                    (h_line2[0] * x + h_line2[1] * y + h_line2[2]) >= 0 and \
                    (h_line3[0] * x + h_line3[1] * y + h_line3[2]) <= 0 and \
                    (h_line4[0] * x + h_line4[1] * y + h_line4[2]) <= 0 and \
                    (h_line5[0] * x + h_line5[1] * y + h_line5[2]) <= 0 and \
                    (h_line6[0] * x + h_line6[1] * y + h_line6[2]) >= 0 ): 
                    Map.occupancy_grid_map[i, j]=1



    @classmethod
    def is_valid(self, pos): 
        rows, cols = Map.occupancy_grid_map.shape 
        x, y = pos
        j = x
        i = rows - 1 - y
        return Map.occupancy_grid_map[i, j]==0

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

        if (not Map.is_valid(start)):
            print("This start point is not valid.")
            success = False
        if (not Map.is_valid(goal)):
            print("This goal point is not valid.")
            restart = False
        print("---")

    return start, goal



if __name__ == "__main__":
    #start, goal = start_simulation()
    #my_map = Map(start, goal)
    Map.form_obstacle_map()
    print(Map.occupancy_grid_map[115,:])


