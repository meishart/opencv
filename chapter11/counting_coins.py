import argparse
import imutils
import cv2
import numpy as np

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

for (i, c) in enumerate(counts):
    (x, y, w, h) = cv2.boundingRect(c)

    print("Coins #{}".format(i + 1))
    coin = image[y:y+h, x:x+w]
    cv2.imshow("Coin", coin)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y+h, x:x+w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))

cv2.waitKey(0)