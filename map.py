import numpy as np
from queue import PriorityQueue
import argparse

from utils import *
from visualize import *

class Node:
    def __init__(self, pos=(0, 0), cost=float('inf'), parent=None): 
        self.pos = pos
        self.cost = cost
        self.parent = parent

    def __lt__(self, other): 
        return self.cost < other.cost

    def __gt__(self, other): 
        return self.cost > other.cost

class Dijkstra: 
    def __init__(self, start_pos, goal_pos):
        self.open_list = PriorityQueue()
        # use set for faster checking visited 
        self.closed_list = set()
        self.closed_list_gui = []

        start_node = Node(start_pos, 0)
        self.add_node(start_node)

        self.start_pos = start_pos
        self.goal_pos = goal_pos

    def add_node(self, node): 
        self.open_list.put((node.cost, node))
        pass

    def find_child_nodes(self, node): 
        x, y = node.pos
        action_sets = [(-1, 1), (0, 1), (1, 1),
                       (-1, 0),         (1, 0),
                       (-1,-1), (0,-1), (1,-1)]

        childs = []
        for action in action_sets:
            child_pos = (x+action[0], y+action[1])
            if(Map.is_valid(child_pos) and \
               (not child_pos in self.closed_list) ): 
                cost = 1 if action[0]==0 or action[1]==0 else 1.4
                child = Node(pos=child_pos, parent=node, cost=node.cost+cost)
                childs.append(child)

        return childs

    # after finding the goal, backtrack to find the path
    def generate_path(self, node):
        path = []
        # backtrack
        while(node.parent != None):
            path.append(node.pos)
            node = node.parent
        path.append(self.start_pos)
        path.reverse()

        print("Searched nodes: ", len(self.closed_list))
        print("Solution steps: ", len(path))
        return self.closed_list_gui, path 

    def search(self):
        while(self.open_list.qsize() != 0):
            run_spinning_cursor()

            current = self.open_list.get()
            ccost, cnode = current
            if(cnode.pos in self.closed_list):
                continue
            self.closed_list.add(cnode.pos)
            self.closed_list_gui.append(cnode.pos)

            # check if arrive goal
            if(cnode.pos == self.goal_pos):
                print("Success")
                return self.generate_path(cnode)

            childs = self.find_child_nodes(cnode)
            for child in childs:
                self.add_node(child)
        else:
            print("Search fails")
            sys.exit(1)

class Map:
    #mm
    width = 400 
    height = 250 
    occupancy_grid_map = np.zeros((height+1, width+1))
    robot_radius = 5
    
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    @classmethod
    def form_obstacle_map(self): 
        # boundary
        b_line1 = create_line((0,0), (0,250))
        b_line2 = create_line((0,250), (400,250))
        b_line3 = create_line((400,250), (400,0))
        b_line4 = create_line((0,0), (400,0))

        # frisbee
        # outer triangle
        ot_line1 = create_line((35, 185), (115, 210))
        ot_line2 = create_line((105, 100), (115, 210))
        ot_line3 = create_line((35, 185), (105, 100))
        # inner triangle
        it_line1 = create_line((80, 185), (115, 210))
        it_line2 = create_line((105, 100), (115, 210))
        it_line3 = create_line((80, 185), (105, 100))

        # hexagon
        edge = np.tan(np.pi/6) * 70 
        h_line1 = create_line((165, 100 + edge/2), (165, 100 - edge/2))
        h_line2 = create_line((165, 100 + edge/2), (200, 100 + edge))
        h_line3 = create_line((200, 100 + edge), (235, 100 + edge/2))
        h_line4 = create_line((235, 100 + edge/2), (235, 100 - edge/2))
        h_line5 = create_line((200, 100 - edge), (235, 100 - edge/2))
        h_line6 = create_line((165, 100 - edge/2), (200, 100 - edge))

        # circle
        center = (300, 185)
        c_x, c_y = center
        c_r = 40

        rows, cols = Map.occupancy_grid_map.shape 
        for i in range(0, rows):
            for j in range(0, cols): 
                # transform from top-left (0,0) to bottom-left (0,0)
                x = j
                y = rows - 1 - i

                # boundary with clearance
                if ((b_line1[0] * x + b_line1[1] * y + b_line1[2]) <=  Map.robot_radius or \
                    (b_line2[0] * x + b_line2[1] * y + b_line2[2]) >= -Map.robot_radius or \
                    (b_line3[0] * x + b_line3[1] * y + b_line3[2]) >= -Map.robot_radius or \
                    (b_line4[0] * x + b_line4[1] * y + b_line4[2]) <=  Map.robot_radius ): 
                    Map.occupancy_grid_map[i, j]=2

                    # boundary
                    if ((b_line1[0] * x + b_line1[1] * y + b_line1[2]) <= 0 or \
                        (b_line2[0] * x + b_line2[1] * y + b_line2[2]) >= 0 or \
                        (b_line3[0] * x + b_line3[1] * y + b_line3[2]) >= 0 or \
                        (b_line4[0] * x + b_line4[1] * y + b_line4[2]) <= 0 ): 
                        Map.occupancy_grid_map[i, j]=1

                # frisbee with clearance
                if ((ot_line1[0] * x + ot_line1[1] * y + ot_line1[2]) >= -Map.robot_radius and \
                    (ot_line2[0] * x + ot_line2[1] * y + ot_line2[2]) <=  Map.robot_radius and \
                    (ot_line3[0] * x + ot_line3[1] * y + ot_line3[2]) >= -Map.robot_radius): 
                    Map.occupancy_grid_map[i, j]=2

                    # frisbee
                    # check outer triangle 
                    if ((ot_line1[0] * x + ot_line1[1] * y + ot_line1[2]) >=0 and \
                        (ot_line2[0] * x + ot_line2[1] * y + ot_line2[2]) <=0 and \
                        (ot_line3[0] * x + ot_line3[1] * y + ot_line3[2]) >=0 ): 
                        Map.occupancy_grid_map[i, j]=1

                        # inner triangle fill red
                        if ((it_line1[0] * x + it_line1[1] * y + it_line1[2]) >= 0 and \
                            (it_line2[0] * x + it_line2[1] * y + it_line2[2]) <= 0 and \
                            (it_line3[0] * x + it_line3[1] * y + it_line3[2]) >= 0 ): 
                            Map.occupancy_grid_map[i, j]=2

                # inner triangle recover white
                if ((it_line1[0] * x + it_line1[1] * y + it_line1[2]) >= Map.robot_radius and \
                    (it_line2[0] * x + it_line2[1] * y + it_line2[2]) <= Map.robot_radius*2  and \
                    (it_line3[0] * x + it_line3[1] * y + it_line3[2]) >= Map.robot_radius ): 
                    Map.occupancy_grid_map[i, j]=0
               
                # hexagon with clearance
                if ((h_line1[0] * x + h_line1[1] * y + h_line1[2]) >=  -Map.robot_radius and \
                    (h_line2[0] * x + h_line2[1] * y + h_line2[2]) >=  -Map.robot_radius and \
                    (h_line3[0] * x + h_line3[1] * y + h_line3[2]) <=  Map.robot_radius  and \
                    (h_line4[0] * x + h_line4[1] * y + h_line4[2]) <=  Map.robot_radius  and \
                    (h_line5[0] * x + h_line5[1] * y + h_line5[2]) <=  Map.robot_radius and \
                    (h_line6[0] * x + h_line6[1] * y + h_line6[2]) >=  -Map.robot_radius ): 
                    Map.occupancy_grid_map[i, j]=2

                    # hexagon 
                    if ((h_line1[0] * x + h_line1[1] * y + h_line1[2]) >= 0 and \
                        (h_line2[0] * x + h_line2[1] * y + h_line2[2]) >= 0 and \
                        (h_line3[0] * x + h_line3[1] * y + h_line3[2]) <= 0 and \
                        (h_line4[0] * x + h_line4[1] * y + h_line4[2]) <= 0 and \
                        (h_line5[0] * x + h_line5[1] * y + h_line5[2]) <= 0 and \
                        (h_line6[0] * x + h_line6[1] * y + h_line6[2]) >= 0 ): 
                        Map.occupancy_grid_map[i, j]=1

                # circle
                if (pow((x-c_x), 2) + pow((y-c_y), 2)) <= pow(c_r+Map.robot_radius, 2): 
                    Map.occupancy_grid_map[i, j]=2
                    if (pow((x-c_x), 2) + pow((y-c_y), 2)) <= pow(c_r, 2): 
                        Map.occupancy_grid_map[i, j]=1

    @classmethod
    def is_valid(self, pos): 
        rows, cols = Map.occupancy_grid_map.shape 
        x, y = pos
        j = x
        i = rows - 1 - y
        return Map.occupancy_grid_map[i, j]==0

    def solve(self): 
        graph = Dijkstra(self.start, self.goal)
        process, solution = graph.search()

        return process, solution

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
            success = False
        print("---")

    return start, goal



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--render", help="Render the whole process (This will take a long time)", action="store_true")
    parser.add_argument("-p", "--print", help="Print out the solution", action="store_true")

    args = parser.parse_args()
    Map.form_obstacle_map()
    start, goal = start_simulation()
    my_map = Map(start, goal)
    process, sol = my_map.solve()
    if args.print:
        for pos in sol:
            print(pos)
 
    draw_search(process, sol, Map.occupancy_grid_map, render_process=args.render)
    #draw_grid_map(Map.occupancy_grid_map)



 
