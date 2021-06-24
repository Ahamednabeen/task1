from function import load_image
import cv2
import argparse
import numpy as np
from function import *

img=load_image(data)
cv2.namedWindow('Image')
result = img.copy()
frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([155,25,0])
upper = np.array([179,255,255])
mask = cv2.inRange(frame, lower, upper)
result = cv2.bitwise_and(result, result, mask=mask)

cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()

# Creates Trackbar with slider position and callback function
low_k = 1 # slider start position
high_k = 31  # maximal slider position
cv2.createTrackbar('Blur', 'Image', low_k, high_k, on_change)

# Infinite loop
while(True):
    ksize = cv2.getTrackbarPos('Blur', 'Image')  # returns trackbar position
    ksize = 2*ksize-1  # medianBlur allows only odd ksize values

    # Blures input image
    median = cv2.medianBlur(img, ksize)  # source, kernel size

    cv2.imshow('Image', median)  # displays image 'median' in window
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()