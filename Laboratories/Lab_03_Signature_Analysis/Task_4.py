import numpy as np 
import cv2 
import Task_1, Task_2
"""
We implement black to white transition algorithm for the OTSU binarized image.
"""

def B2WTransition(img_file):
	img = cv2.imread(img_file, 0)
	height, width = img.shape
	prevPixel = img[0,0]
	countBW = 0
	for x in range(height):
		for y in range(width):
			curPixel = img[x,y]
			if (curPixel == 255) and (prevPixel == 0):
				countBW += 1
			prevPixel = curPixel
	return countBW

countBW = B2WTransition("x_y_cut_image.png")
print("Count: ", countBW)
