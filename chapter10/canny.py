import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=300)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", blurred)

canny = cv2.Canny(image, 60, 196)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
