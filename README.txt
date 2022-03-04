# Dijkstra-path-planning
Simulation of a  point robot searching in a map with obstacle using Dijkstra.

## Run
```
python3 Dijkstra-pathplanning-Chang-Hong-Chen.py

```
After program start, enter start position and goal position.  
The map has width 400, height 250  

### Arguments option
```
python3 Dijkstra-pathplanning-Chang-Hong-Chen.py -r -p
```
**-r**: Render the searching process (takes a long time)   
**-p**: Print out the trajectory  

## Result
**videos**: ./pictures/dijkstra_10x.mp4
This video is speed up by 10x because of the slow rendering process.
start: (30, 30)
goal: (200, 200)
```
black: obstacle
red: robot size margin (5mm)
white: empty
blue: robot trajectory
green: goal
```

## Implementation details
1. Alternative way to deal with cost updating:   
Dijkstra requires cost updating with the openlist. However, this is a rather time costly process.
In this project, I didn't update the cost in the openlist.  
I put the same node with different cost into the openlist and skip the node poped out form openlist if it is already in closedlist.
Among all the same node, only the one with the lowest cost will be poped. And a node goes into the closedlist once it is poped. 
Therefore, there is no need to update the cost inside the openlist.

2. Obstacle margin for robot size:
In this project, the margins are form by moving the line out a certain value (the robot radius). 
However, this is a rather conservative apporach, because all the vertexs of obstacles should use a circular form of obstacle margin.  

3. The collision detection:
After forming the math description of the obstacle, this information is stored in a grid map. 
The collision is not examined on run time using the semi-algebraic models, and instead is examined with this grid map with less time.  
