import numpy as np
import cv2

def draw_grid_map(grid_map):
    rows, cols = grid_map.shape
    color_map = np.zeros((rows, cols, 3))
    color_map[np.where(grid_map == 0)] = np.array([255, 255, 255])
    color_map[np.where(grid_map == 1)] = np.array([0, 0, 0])
    color_map[np.where(grid_map == 2)] = np.array([0, 0, 255])
    color_map[np.where(grid_map == 3)] = np.array([255, 180, 0])  
    color_map[np.where(grid_map == 4)] = np.array([255, 145, 0])  

    #big_grid_map =  cv2.resize(grid_map, (1600, 1000))
    #cv2.imshow("Map", big_grid_map)
    cv2.imshow("Map", color_map)
    cv2.waitKey(10)
    #cv2.waitKey(0)

def draw_search(process, solution, grid_map, render_process=False): 
    rows, cols = grid_map.shape
    if render_process:
        process_map = grid_map.copy()
        for step in process:  
            x, y = step
            j = x
            i = rows - 1 - y
            process_map[i, j] = 3
            draw_grid_map(process_map)

    for pos in solution: 
        c_x, c_y = pos
        for x in range(c_x-5, c_x+5+1): 
            for y in range(c_y-5, c_y+5+1): 
                if(pow((x-c_x), 2) + pow((y-c_y), 2)) <= pow(5, 2): 
                    j = x
                    i = rows - 1 - y
                    grid_map[i, j]=4
    draw_grid_map(grid_map)
    cv2.waitKey(0)
