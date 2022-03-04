import numpy as np
import sys 
import time

# for waiting calculation
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
def run_spinning_cursor(): 
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    sys.stdout.write('\b')
 
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
    norm = np.sqrt(pow(a, 2) + pow(b, 2))
    a, b = a / norm, b / norm 
    d = -(a * p1[0] + b * p1[1])
    return a, b, d
