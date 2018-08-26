import numpy as np
import cv2

canvas1 = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(canvas1, (25,25), (275, 275), 255, -1)
cv2.imshow("Rectangle", canvas1)

canvas2 = np.zeros((300, 300), dtype="uint8")
center = (150, 150)
cv2.circle(canvas2, center, 150, 255, -1)
cv2.imshow("Circle", canvas2)



# bitwise operations
bitwise_and = cv2.bitwise_and(canvas1, canvas2)
cv2.imshow("And", bitwise_and)

bitwise_or = cv2.bitwise_or(canvas1, canvas2)
cv2.imshow("Or", bitwise_or)

bitwise_xor = cv2.bitwise_xor(canvas1, canvas2)
cv2.imshow("Xor", bitwise_xor)

bitwise_not = cv2.bitwise_not(canvas2)
cv2.imshow("Not", bitwise_not)
cv2.waitKey(0)
