class Node:
    def __init__(self, pos=(0, 0), parent=None): 
        self.pos = pos
        self.parent = parent
        self.cost = 0

class Dijkstra: 
    def __init__(self, start, goal):
        pass

    def is_valid(self, node): 

    def add_node(self, node): 
        pass

    def find_child_nodes(self, node): 
        action_sets = [(-1, 1), (0, 1), (1, 1),
                       (-1, 0),       , (1, 0)
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

    def solve(self): 
        pass
