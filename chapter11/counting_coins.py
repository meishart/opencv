import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=300)
grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(grayed, (11, 11), 0)
cv2.imshow("Image", image)

edged = cv2.Canny(blurred, 80, 196)
cv2.imshow("Edges", edged)

(_, counts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("I count {} coins in this image.".format(len(counts)))

coins = image.copy()
cv2.drawContours(coins, counts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)

cv2.waitKey(0)