import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {} pixels".format(image.shape[2]))

# display image
cv2.imshow("Image", image)
cv2.waitKey(0)

# write image
cv2.imwrite("newimage.jpg", image)

