from matplotlib import pyplot as plt
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
resized = imutils.resize(image, width=300)

cv2.imshow("Original", resized)

# Split the image into three channels - Blue, Green and Red.
channels = cv2.split(resized)
colors = ('b', 'g', 'r')

plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (channel, color) in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    # Plot histogram in each color
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

# 2D Histograms
figure = plt.figure()
ax = figure.add_subplot(131)
hist = cv2.calcHist([channels[0], channels[1]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B.")
plt.colorbar(p)

ax = figure.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R.")
plt.colorbar(p)

ax = figure.add_subplot(133)
hist = cv2.calcHist([channels[2], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for R and B.")
plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

# 3D Histogram
hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

plt.show()


