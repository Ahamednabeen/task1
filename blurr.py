from function import load_image
import cv2
import argparse
import numpy as np
from function import *
from initialize import initialize


def main():
    initialize()
    path='test2.jpg'
    data=dataloader(path)

    img=load_image(data)

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
    
    