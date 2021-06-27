import cv2
import argparse
import numpy as np
from function import dataloader,colour_filter,blurr,blurr_image, detect_objects, draw_countours
from initialize import initialize,init_trackbar_filter



def main():
    img=dataloader()   

    result=colour_filter(img)
    contours = detect_objects(result)
    # cv2.imshow('filtered', result)
    cv2.waitKey()
    initialize() 
    draw_countours(contours,result)
    # Infinite loop
    while(True):
        median=blurr_image(img,blurr())
        cv2.imshow('Image', median)  # displays image 'median' in window
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

    init_trackbar_filter()
if __name__ == "__main__":

    main()
    
    