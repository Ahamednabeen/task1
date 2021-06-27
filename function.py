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




def detect_objects(result):
        """this function accepts filtered image(result of filter operation) as input and detect the objects in it.First it converts the image (bgr)into gray scale
        .Then it performs canny edge detection in it .Then it creates a mask with that image (gray varriable) with cv2.adaptivethreshold method.Then it find the 
        contour coordinates from the mask by cv2.findcontours method and the coordinate values will be stored in the varriable contours.Then it initializes a empty
        list (objects_contours) to store the coordinate values after sorting and neglecting small contours .It creates a loop that loops in contours .In that loop 
        first it finds the area of the current contour and store it in area Then check if area is greater than a threshold value.If only yes it appends that contour 
        the object_contour list.And finally when the loop is over it returns that list(object contours)
        Parameters: gray(mat)::input image
                    mask(mat)::binary image
                    contours(numpy array)::contours with coordinates
                    object_contours(list)::listt of final contours
                    area(float)::area of respective contour
        return type:  object_contours(list)::listt of final contours
        reference  :https://pysource.com/2021/05/28/measure-size-of-an-object-with-opencv-aruco-marker-and-python/          
                    """
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
    """ This function is to draw polylines on the contours.It takes contours(list containing contours) and result(image with colour filtered output) .It creates a for loop to loop in the contours.Fisrt it creats a rectangle with minimum possible size
    and store the paramters in rect(varriable).Then it extracts the paramters(axis coordinates,height,width,angle) and store it in rect .It creates a bounding box 
    with the paramters in the rect and to convert those into integers(cv2 only supports integers for drawing).Then using cv2.polylines function it draws the box coordinates
     and displays the result at end of loop
     parameters:contours(listt)::list of contours
                result(mat) :: input image
                rect(list)::rectangle paramters
                box(list):: box coordinatets
    return_type:none
    reference:https://pysource.com/2021/05/28/measure-size-of-an-object-with-opencv-aruco-marker-and-python/ """
    for cnt in contours:

    # Get rect
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect


    # Display rectangle
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # cv2.circle(result, (int(x), int(y)), 5, (255, 255, 255), 3)
        cv2.polylines(result, [box], True, (255, 255, 255), 2)
        # cv2.drawContours(result, [box.astype("int")], -1, (0, 255, 0), 2)
    cv2.imshow('contours',result)    #         