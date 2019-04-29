import numpy as np 
import cv2 
"""
We implement centroid computing algorithm for the OTSU binarized image.
"""
def centroid_computation(img_file):
	img = cv2.imread(img_file, 0)
	height, width = img.shape
	cx, cy, n = 0,0, 0
	for x in range(height):
		for y in range(width):
			if img[x,y] == 0:
				cx = cx + x 
				cy = cy + y
				n += 1
	cx = cx // n
	cy = cy // n 
	print("Centeroid: ", " cX: ", cx, " cY: ", cy)
	centeroid_image = cv2.circle(img, (cy, cx), 10, 200, -1)
	cv2.imwrite('centeroid_image.png', centeroid_image)
	return cx, cy
