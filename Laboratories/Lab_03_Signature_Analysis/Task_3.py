import numpy as np 
import cv2 
import Task_1, Task_2
"""
We implement dividing the image at centroid algorithm for the OTSU binarized image.
"""

def divide_image(img_file, top, bottom, right, left, cx, cy):
	img = cv2.imread(img_file, 0)
	print("Forming Cuts!")
	cut_img = cv2.rectangle(img, (top, left), (cy, cx), (0,255,0), 3)
	cut_img = cv2.rectangle(cut_img, (top, cx), (cy, right), (0,255,0), 3)
	cut_img = cv2.rectangle(cut_img, (cy, left), (bottom, cx), (0,255,0), 3)
	cut_img = cv2.rectangle(cut_img, (cy, cx), (bottom, right), (0,255,0), 3)
	
	top_left = img[left:cx, top:cy]
	bottom_left = img[cx:right, top:cy]
	top_right = img[left:cx, cy:bottom]
	bottom_right = img[cx:right, cy:bottom]

	cv2.imwrite("x_y_cut_image.png", cut_img)
	cv2.imwrite("top_left_image.png", top_left)
	cv2.imwrite("bottom_left_image.png", bottom_left)
	cv2.imwrite("top_right_image.png", top_right)
	cv2.imwrite("bottom_right_image.png", bottom_right)
	return top_left, bottom_left, top_right, bottom_right

top, bottom, right, left = Task_1.bounding_box("bin_sig.png")
cx, cy = Task_2.centroid_computation("detected_box.png")
divide_image("centeroid_image.png", top, bottom, right, left, cx, cy)
