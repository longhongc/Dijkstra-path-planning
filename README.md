# Dijkstra-path-planning
Simulation of a  point robot searching in a map with obstacle using Dijkstra.

The obstacles are described using Half planes and semi-algebraic models.  
<img src="https://user-images.githubusercontent.com/28807825/156786066-20604f75-6ae5-4790-bef8-b86c05106cc7.png" alt="drawing" width="500"/>

The final result is visualized using OpenCV  
![dijkstra](https://user-images.githubusercontent.com/28807825/156787123-b84f5938-4de8-4851-8ae4-fd8193f59225.jpg)  
```
black: obstacle
red: robot size margin (5mm)
white: empty
blue: robot trajectory
```

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
