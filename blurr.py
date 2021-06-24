import cv2

# Callback function for trackbar
def on_change(self):
    pass

# Reads image with 0 as GRAY and 1 as BGR
img = cv2.imread('test2.jpg', 0)
img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
# Creates window
cv2.namedWindow('Image')

# Creates Trackbar with slider position and callback function
low_k = 1 # slider start position
high_k = 21  # maximal slider position
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