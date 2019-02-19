import numpy as np
import cv2

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
def backsub(img):
    return fgbg.apply(img)

    