import cv2

def on_change(self):
    pass
def initialize():
    cv2.namedWindow('Image')
    # Creates Trackbar with slider position and callback function
    low_k = 1 # slider start position
    high_k = 31  # maximal slider position
    cv2.createTrackbar('Blur', 'Image', low_k, high_k, on_change)
    """It  creates a opencv window named Image ,lower value,upper value (for the slider which is using for the blurr operation).Then creates a trackbar with the name 'Blur' in the
    Image window
    parameters: Image(opencv window)
                low_k(int)
                high_k(int)
                Trackbar(opencv trackbar)
    return_type: None returns
    reference:  https://stackoverflow.com/questions/53152665/opencv-python-blur-image-using-trackbar              """