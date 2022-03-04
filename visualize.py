import numpy as np
import cv2

def draw_grid_map(grid_map):
    grid_map[np.where(grid_map == 0)] = 255
    grid_map[np.where(grid_map == 1)] = 0

    cv2.imshow("Map", grid_map)
    cv2.waitKey(0)



