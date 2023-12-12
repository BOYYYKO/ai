import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Boyko.jpg")
# DISPLAY
cv2.imshow("Boyko", img)
cv2.waitKey(0)