import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
centre = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(centre, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated 45", rotated)
#cv2.waitKey(0)

M = cv2.getRotationMatrix2D(centre, -90, .5)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated 90", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180", rotated)
cv2.waitKey(0)


