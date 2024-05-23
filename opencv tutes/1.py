import cv2 as cv
r=cv.imread('psr.jpg',1)
'''to read an image you can use this you can use falgs for your image like to display write 1 anter the name of the image to
display colored image and 0 to gray scale image and -1 to lodds image including such as alpha change'''
cv.imshow("hg",r)
cv.waitKey(0)
cv.destroyAllWindows()