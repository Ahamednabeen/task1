from function import load_image
import cv2
import argparse
from function import *

img=load_image(data)
cv2.namedWindow('Image')

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