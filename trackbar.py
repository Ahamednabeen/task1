import cv2
import sys
import numpy as np
from function import dataloader
from funtion2 import *
def main():
    initialize_for_filter()
    image = dataloader()

    # Initialize to check if HSV min/max value changes
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    output = image
    wait_time = 33

    while(1):
        hMin,sMin,vMin,hMax,sMax,vMax=get_pos()
        # Set minimum and max HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])
        output=operation(image,lower,upper)
        print_results(hMin,sMin,vMin,hMax,sMax,vMax)
        # Display output image
        cv2.imshow('image',output)
        # Wait longer to prevent freeze for videos.
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
