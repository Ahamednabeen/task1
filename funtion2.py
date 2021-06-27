import cv2
import numpy as np
def nothing(x):
    pass

# Create a window
def initialize_for_filter():
    """ This funtion initialises the parameters for the working of trackbar including a window named image,creates Six trackbars (hmin,smin,vmin,hmax,smax,vmax)
    and set the track bar positions of Hmax,smax,vmax at its maximum position
    parameters: image (window) :: window to display the trackbar
                                  hmin(trackbar)
                                  smin("")
                                  vmin("")
                                  hmax("")
                                  smax("")
                                  vmax("")
                                  return type:none
                                  reference:https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv
    """
    cv2.namedWindow('image')
    # create trackbars for color change
    cv2.createTrackbar('HMin','image',0,179,nothing) # Hue is from 0-179 for Opencv
    cv2.createTrackbar('SMin','image',0,255,nothing)
    cv2.createTrackbar('VMin','image',0,255,nothing)
    cv2.createTrackbar('HMax','image',0,179,nothing)
    cv2.createTrackbar('SMax','image',0,255,nothing)
    cv2.createTrackbar('VMax','image',0,255,nothing)
    # Set default value for MAX HSV trackbars.
    cv2.setTrackbarPos('HMax', 'image', 179)
    cv2.setTrackbarPos('SMax', 'image', 255)
    cv2.setTrackbarPos('VMax', 'image', 255)



def get_pos():
    """This funtion is to get the current position of the trackbars that we have created
    parameter:hmin(trackbar):
              smin(trackbar)
              vmin(trackbar)
              hmax(trackbar)
              smax(trackbar)
              vmax(trackbar)
    returntype:hmin(trackbar)
              smin(trackbar)
              vmin(trackbar)
              hmax(trackbar)
              smax(trackbar)
              vmax("trackbar)     
    reference: https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv """    
    hMin = cv2.getTrackbarPos('HMin','image')
    sMin = cv2.getTrackbarPos('SMin','image')
    vMin = cv2.getTrackbarPos('VMin','image')

    hMax = cv2.getTrackbarPos('HMax','image')
    sMax = cv2.getTrackbarPos('SMax','image')
    vMax = cv2.getTrackbarPos('VMax','image')
    return hMin,sMin,vMin,hMax,sMax,vMax 

def operation(image,lower,upper):
    """"This function takes image,lower(numpy array of current hmin,vmin,smin positions),upper(numpy array of current hmax,vmax,smax positions)
    as input .Then it creates hsv version of input image (bgr to hsv conversion).Then creates a mask using  hsv with upper and lower as paramters
    then creates output by performing bitwise_and operation in that image with masking and returns that output
    parameter:  image(mat):: input image
                lower(numpy array)::array of hmin,smin,vmin positions                   
                upper(numpy array)::array of hmax,vmax,smax positions
                hsv(mat)::hsv version of input image
                output(mat)::output image  
    return Type:output (mat)
    reference:https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv             """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image,image, mask= mask)
    return output

def print_results(hMin,sMin,vMin,hMax,sMax,vMax):
    """function to print the current values of trackbars .It checks (not equal)the values of the trackbars with some values which are initialised as zero .Then
    print the current values of parameters
    parameters:hMin (Trackbar)
               Smin(Trackbar)
               Vmin(Tracbar)
               hMax(Trackbar)
               sMax(Trackbar)
               Vmax(Trackbar)
    return: None
    reference:https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv              """
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0
    # Print if there is a change in HSV value
    if( (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax        
def arrays(hMin,sMin,vMin,hMax,sMax,vMax):
    """This function is to create arrays for creating mask.It takes current hMin,sMin,vMin,hMax,sMax,vMax(Trackbar values)as input for function
    and create two numpy array with these values
    Paramters:  hMin (Trackbar) :current trackbar position
               Smin(Trackbar):current trackbar position
               Vmin(Tracbar):current trackbar position
               hMax(Trackbar):current trackbar position
               sMax(Trackbar):current trackbar position
               Vmax(Trackbar):current trackbar position
               lower(numpy array)
               upper(numpy array)
    ReturnType:lower(numpy array) ::array created with min values
               Upper(numpy array) ::array created with max values         
                
                """
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    return lower,upper
