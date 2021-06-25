import cv2

def on_change(self):
    pass
def initialize():
    cv2.namedWindow('Image')
    # Creates Trackbar with slider position and callback function
    low_k = 1 # slider start position
    high_k = 31  # maximal slider position
    cv2.createTrackbar('Blur', 'Image', low_k, high_k, on_change)