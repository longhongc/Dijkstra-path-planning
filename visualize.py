import numpy as np
import cv2

def draw_grid_map(grid_map):
    rows, cols = grid_map.shape
    color_map = np.zeros((rows, cols, 3))
    color_map[np.where(grid_map == 0)] = np.array([255, 255, 255])
    color_map[np.where(grid_map == 1)] = np.array([0, 0, 0])
    color_map[np.where(grid_map == 2)] = np.array([0, 0, 255])
    color_map[np.where(grid_map == 3)] = np.array([255, 145, 0])  

    #big_grid_map =  cv2.resize(grid_map, (1600, 1000))
    #cv2.imshow("Map", big_grid_map)
    cv2.imshow("Map", color_map)
    cv2.waitKey(0)



