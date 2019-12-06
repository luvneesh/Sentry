# import the necessary packages
from imutils.perspective import four_point_transform
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image file")
ap.add_argument("-c", "--coords",
                help="comma seperated list of source points")
args = vars(ap.parse_args())
# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
image = cv2.imread('images/example2.png')
pts_1 = np.array([(151, 373), (750, 268), (1693, 531), (1368, 1078)])
pts_2 = np.array([(336, 148), (790, 72), (1513, 277), (936, 1075)])
pts_3 = np.array([(72, 145), (730, 34), (1766, 332), (968, 1078)])
# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts_2)
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.imwrite("images/test.png", warped)
cv2.waitKey(0)