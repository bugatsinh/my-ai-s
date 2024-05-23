import cv2 as cv
import numpy as np


# event = [i for i in dir(cv) if 'EVENT' in i]
# print(event)

def cleak_event(event, x,y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        
        print(x,', ',y)
        fount = cv.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ', ' +str(y)        
        cv.putText(img, strxy, (x, y),fount,1,(255,255,0),2)
        cv.imshow('gjjjg',img)
    if event==cv.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        fount = cv.FONT_HERSHEY_SIMPLEX
        strbgr = str(blue) + ', ' +str(green) + ', ' +str(red)        
        cv.putText(img, strbgr, (x, y),fount,1,(0,255,255),2)
        cv.imshow('gjjjg',img)


# img = np.zeros((512,512,3),np.uint8)
img = cv.imread("psr.jpg")
cv.imshow("gjjjg",img)
cv.setMouseCallback('gjjjg',cleak_event)
cv.waitKey(0)
cv.destroyAllWindows()