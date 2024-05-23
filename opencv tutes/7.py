import cv2 as cv
import numpy as np


# event = [i for i in dir(cv) if 'EVENT' in i]
# print(event)

def cleak_event(event, x,y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv.circle(img,(x,y),2,(0,255,255),-1)
        mycol = np.zeros((450,450,3),np.uint8)
        mycol[:]=(blue,green,red)

        cv.imshow('colour', mycol)


img = cv.imread("psr.jpg")
cv.imshow("image",img)
point = []
cv.setMouseCallback('image',cleak_event)
cv.waitKey(0)
cv.destroyAllWindows()