import argparse
import numpy as np
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help ="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
#cv2.waitKey(0)

# aspect ratio
r = 150.0 / image.shape[1]
new_dimension = (150, int(image.shape[0] * r))

resized = cv2.resize(image, new_dimension, interpolation = cv2.INTER_NEAREST)
cv2.imshow("Resize", resized)
#cv2.waitKey(0)

resized = imutils.resize(image, width = 100)
cv2.imshow("Resized Imutils", resized)
cv2.waitKey(0)



