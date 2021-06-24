import cv2
def on_change(self):
    pass
def load_image(data):
    """image data is value and it converts image into another size given """
    img = data.copy()
    img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
    return img