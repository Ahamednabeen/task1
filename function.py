import cv2
import argparse
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input file")
args = vars(ap.parse_args())
data = cv2.imread(args["image"])


def on_change(self):
    pass
def load_image(data):
    """image data is value and it converts image into another size given """
    img = data.copy()
    img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
    return img