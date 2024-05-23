import cv2 as cv
import numpy as np

img = np.zeros((500,620,3),np.uint8())

# img = cv.imread('psr.jpg')
img = cv.line(img,(640,480),(255,255),(255,0,0))
img = cv.arrowedLine(img,(640,0),(255,255),(255,0,0))
img = cv.rectangle(img, (255,0),(0,650),(255,255,255),-2)
img = cv.circle(img, (255,455),56,(0,255,255),-1)
fount = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, 'who are you', (10,200), fount,4,(255,156,95))
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()