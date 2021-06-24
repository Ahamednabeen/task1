from function import load_image
import cv2
import argparse
import numpy as np
from function import *

img=load_image(data)
cv2.namedWindow('Image')
frame = img
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)


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