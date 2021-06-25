import cv2
import argparse
import numpy as np
import argparse
import imutils
from imutils import contours
from imutils import perspective

# construct the argument parser and parse the arguments

def dataloader():
    """this function is to load the image from the path given as the arguiment in launch.json file and return the image with a resized size
    parameters:image(mat)::input image
    return_type: image(mat) in decreased size from its original
    reference:none"""

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help = "path to the image file")
    args = vars(ap.parse_args())
    data = cv2.imread(args["image"])
    img = data.copy()
    img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
    return img
    
    
def colour_filter(img):
    """it accepts img(image file) then this function is create a filter function for the image that been read  .It reads a image copy that into result varriable Then it converts result into hsv format from bgr format
    .Then it creates two numpy arrays lower and upper containing pixel values of red .Then it creates a mask with these values .Then with that mask we apply bitwise and
    operation on the result(image) varriable and return that varriable 
    parameters: img (mat) in bgr format ::input image
                frame(mat) in hsv format ::hsvv image
                lower(numpy array) ::
                upper(numy array) ::
                mask(numpy array) :: masked i
                result(mat) :: output image
    return_type: result(mat)   
    reference:https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv"""
    result=img.copy()
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([153,25,0])
    upper = np.array([177,255,255])
    mask = cv2.inRange(frame, lower, upper)
    result = cv2.bitwise_and(result, result, mask=mask)
    return result
    

def blurr(): 
    """this function takes position of trackbar (Blur) as input (from Image wiindow) and store that valuue in varriable k size and returns the ksize
    paramters:ksize(int)
    return_type: ksize(int)
    reference:https://stackoverflow.com/questions/53152665/opencv-python-blur-image-using-trackbar"""   
    ksize = cv2.getTrackbarPos('Blur', 'Image')  # returns trackbar position
    return ksize
    


def blurr_image(img,i):
        """this funtions takes img(image file),an integer (k size from blurr() function in this case) as input.Store that integer into the varriable ksize
        .Then it make sure that ksize is odd number by performing a operation.Then it performs a median blurr with the img and ksize
        parameters: img(mat)
                    ksize(int)
                    median(mat)
        return_type: median(mat)    
        reference:  https://stackoverflow.com/questions/53152665/opencv-python-blur-image-using-trackbar"""
        
        ksize=i
        ksize = 2*ksize-1  # medianBlur allows only odd ksize values
        # Blures input image
        median = cv2.medianBlur(img, ksize)  # source, kernel size
        return median

# def find_contours(result):
#         image =result
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         edged = cv2.dilate(image, None, iterations=1)
#         edged = cv2.erode(edged, None, iterations=1)
#         cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         cnts = imutils.grab_contours(cnts)
#         # sort the contours from left-to-right and initialize the
#         # 'pixels per metric' calibration variable
#         (cnts, _) = contours.sort_contours(cnts)
#         pixelsPerMetric = None
#         # loop over the contours individually
#         for c in cnts:
#             # if the contour is not sufficiently large, ignore it
#             if cv2.contourArea(c) < 100:
#                 continue
#             # compute the rotated bounding box of the contour
#             orig = image.copy()
#             box = cv2.minAreaRect(c)
#             box = cv2.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
#             box = np.array(box, dtype="int")
#             # order the points in the contour such that they appear
#             # in top-left, top-right, bottom-right, and bottom-left
#             # order, then draw the outline of the rotated bounding
#             # box
#             box = perspective.order_points(box)
#             cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)



def detect_objects(result):
        # Convert Image to grayscale
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        gray = cv2.Canny(gray, 30, 200)
        # Create a Mask with adaptive threshold
        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #cv2.imshow("mask", mask)
        objects_contours = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 2000:
                #cnt = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
                objects_contours.append(cnt)

        return objects_contours
def draw_countours(contours,result):
    for cnt in contours:

    # Get rect
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect
#

    # Display rectangle
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # cv2.circle(result, (int(x), int(y)), 5, (255, 255, 255), 3)
        cv2.polylines(result, [box], True, (255, 255, 255), 2)
        # cv2.drawContours(result, [box.astype("int")], -1, (0, 255, 0), 2)
    cv2.imshow('contours',result)    #         