import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=300)
cv2.imshow("Original", image)

# Create a mask of the same size as the image
mask = np.zeros(image.shape[:2], dtype="uint8")

# Center of the image
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)

# Rectangle inside mask filled with white color
cv2.rectangle(mask, (cX - 75, cY -75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked", masked)
cv2.waitKey(0)
