import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# opencv performs clipping and ensure result is always between (0, 255)
result = cv2.add(np.uint8([200]), np.uint8([100]))
print("max of 255: {}".format(result))

result = cv2.subtract(np.uint8([50]), np.uint8([100]))
print("min of 255: {}".format(result))

# numpy performs modulo arithmetic and wrap around
result = np.uint8([200]) + np.uint8([100])
print("wrap around: {}".format(result))

result = np.uint8([50]) - np.uint8([100])
print("wrap around: {}".format(result))

# load image
image = cv2.imread(args["image"])
image = imutils.resize(image, width=400)
cv2.imshow("Original", image)

M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtract", subtracted)
cv2.waitKey(0)