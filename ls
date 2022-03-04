[1mdiff --git a/__pycache__/setting.cpython-38.pyc b/__pycache__/setting.cpython-38.pyc[m
[1mdeleted file mode 100644[m
[1mindex 8a74214..0000000[m
Binary files a/__pycache__/setting.cpython-38.pyc and /dev/null differ
[1mdiff --git a/__pycache__/utils.cpython-38.pyc b/__pycache__/utils.cpython-38.pyc[m
[1mdeleted file mode 100644[m
[1mindex 3b4c2d5..0000000[m
Binary files a/__pycache__/utils.cpython-38.pyc and /dev/null differ
[1mdiff --git a/__pycache__/visualize.cpython-38.pyc b/__pycache__/visualize.cpython-38.pyc[m
[1mdeleted file mode 100644[m
[1mindex 73b8b9a..0000000[m
Binary files a/__pycache__/visualize.cpython-38.pyc and /dev/null differ
[1mdiff --git a/visualize.py b/visualize.py[m
[1mindex 2ebfe64..517442d 100644[m
[1m--- a/visualize.py[m
[1m+++ b/visualize.py[m
[36m@@ -23,6 +23,7 @@[m [mdef draw_grid_map(grid_map):[m
 [m
     cv2.imshow("Map", color_map)[m
     cv2.waitKey(1)[m
[32m+[m[32m    cv2.imwrite('dijkstra.jpg', color_map)[m
 [m
 def draw_search(process, solution, grid_map, render_process=False): [m
     rows, cols = grid_map.shape[m
