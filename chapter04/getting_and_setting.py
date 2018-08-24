import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Paint the pixel RED
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Slicing
corner = image[0:450, 0:450]
cv2.imshow("Corner", corner)

image[0:450, 0:450] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)

