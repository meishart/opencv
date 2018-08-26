import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=400)
cv2.imshow("Original", image)

cropped = image[50:200, 300:400]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
