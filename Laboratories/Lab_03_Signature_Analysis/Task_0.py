import cv2 
import numpy as np 

"""
  Reading image, and converting to black and white. 
  We use OTSU binarization for the task.
"""
def binarization(img_file):
	img = cv2.imread(img_file, 0)
	retval, binarized_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
	cv2.imwrite("bin_sig.png", binarized_img)

binarization("test_image1.jpg")
