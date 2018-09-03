import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# Read the image from disk
image = cv2.imread(args["image"])
resized = imutils.resize(image, width=300)
cv2.imshow("Original", resized)

# Grayscale
grayed = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayed", grayed)

# Equalize
eq = cv2.equalizeHist(grayed)

cv2.imshow("Histogram Equalized", np.hstack([grayed, eq]))
cv2.waitKey(0)