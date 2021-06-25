import cv2
import argparse
import numpy as np
from function import dataloader,colour_filter,blurr,blurr_image
from initialize import initialize


def main():
    initialize()
    img=dataloader()

    

    result=colour_filter(img)
    cv2.imshow('filtered', result)
    cv2.waitKey()

    
    # Infinite loop
    while(True):
        median=blurr_image(img,blurr())
        cv2.imshow('Image', median)  # displays image 'median' in window
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":

    main()
    
    