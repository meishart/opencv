import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
resized = imutils.resize(image, width = 300)
cv2.imshow("Original", resized)

# flipped = cv2.flip(resized, 1)
# cv2.imshow("Flipped Horizontally", flipped)
#
# flipped = cv2.flip(resized, 0)
# cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(resized, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)

cv2.waitKey(0)
