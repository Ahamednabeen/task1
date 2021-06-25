import cv2
import argparse
import numpy as np
from function import dataloader,colour_filter,blurr,blurr_image, detect_objects
from initialize import initialize


def main():
    initialize()
    img=dataloader()

    

    result=colour_filter(img)
    contours = detect_objects(result)
    cv2.imshow('filtered', result)
    cv2.waitKey()

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
    cv2.imshow('contours',result)
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
    
    