import numpy as np 
import cv2 
"""
We implement bounding box algorithm for the OTSU binarized image.
"""

def bounding_box(img_file):
	img = cv2.imread(img_file, 0)
	height, width = img.shape
	print(height, width)
	left, right = width, 0
	top, bottom = height, 0

	for x in range(height-1):
		for y in range(width-1):
			color = img[x,y]
			if color == 0:
				if x > right:
					right = x
				if x < left:
					left = x 
				if y > bottom:
					bottom = y
				if y < top:
					top = y


	print("The bounding box is: ")
	print("Top: ", top, " Bottom: ", bottom, " Left: ", left, " Right: ", right)
	bounding_box = cv2.rectangle(img, (top, left), (bottom, right), (0,0,0), 3)
	bounding_box_image = img[left:right, top:bottom]
	cv2.imwrite('detected_box.png', bounding_box)
	return top, bottom, right, left
