import cv2 as cv
import numpy as np


# event = [i for i in dir(cv) if 'EVENT' in i]
# print(event)

def cleak_event(event, x,y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        circle = cv.circle(img,(x,y),4,(0,0,255),-1)
        point.append((x,y))
        if len(point) >=2:
            cv.line(img,point[-1],point[-2],(255,0,0),5)
        cv.imshow('image', img)


img = np.zeros((512,512,3),np.uint8)
cv.imshow("image",img)
point = []
cv.setMouseCallback('image',cleak_event)
cv.waitKey(0)
cv.destroyAllWindows()