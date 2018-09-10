import argparse
import imutils
import cv2
import mahotas


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=300)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# Otsu's threshold value
T = mahotas.thresholding.otsu(blurred)
print("Otsu's thresholding: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0

thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

# Riddler-Calvard threshold value
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard thresholding: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0

thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)

cv2.waitKey(0)