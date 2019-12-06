import cv2
import numpy as np
from imutils.perspective import four_point_transform

# Read image
im_in_rgb = cv2.imread("images/hell1.png", cv2.IMREAD_COLOR)
im_in = cv2.imread("images/hell1.png", 0)

# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
lYellow = np.array([20,100,100])
uYellow = np.array([30,255,255])
th, im_th = cv2.threshold(im_in, 50, 255, cv2.THRESH_BINARY)

hsv = cv2.cvtColor(im_in_rgb, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, lYellow, uYellow)
kernel = np.array([10,10])
dilation = cv2.dilate(mask, kernel, iterations = 10)
mask = dilation
mask = 255 - mask
mask1 = mask & im_th
res = cv2.bitwise_and(im_in_rgb, im_in_rgb, mask = mask1)
# Display images.
# cv2.imshow("Thresholded Image", res)

pts_1 = np.array([(151, 373), (750, 268), (1693, 531), (1368, 1078)])
pts_2 = np.array([(336, 148), (790, 72), (1513, 277), (936, 1075)])
pts_3 = np.array([(72, 145), (730, 34), (1766, 332), (968, 1078)])
pts_5 = np.array([(494, 228), (848, 168), (1462, 346), (946, 1074)])

pts_11 = np.array([(138, 178), (770, 76), (1820, 380), (1008, 1074)])
pts_12 = np.array([(472, 228), (836, 168), (1432, 340), (932, 1078)])

pts_hough1 = np.array([(93, 165), (777, 69), (1885, 389), (957, 1917)])
pts_hell = np.array([(97, 169), (769, 61), (1893, 385), (953, 1937)])
# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(im_in_rgb, pts_hell)
# show the original and warped images
cv2.imshow("Original", im_in_rgb)
cv2.imshow("Warped", warped)
cv2.imwrite("images/test.png", warped)
cv2.waitKey(0)