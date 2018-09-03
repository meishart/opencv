from matplotlib import pyplot as plt
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width = 300)
cv2.imshow("Original", image)

# obtain a grayscale image
grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayed", grayed)

# compute the histogram
histogram = cv2.calcHist([grayed], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(histogram)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
