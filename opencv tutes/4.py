import cv2 as cv

fdd=cv.VideoCapture(0);

print(fdd.get(cv.CAP_PROP_FRAME_WIDTH))
print(fdd.get(cv.CAP_PROP_FRAME_HEIGHT))
fdd.set(3,3000)# three is use on the place of cv.CAP_PROP_FRAME_WIDTH
fdd.set(4,3000)#four is use on the place of cv.CAP_PROP_FRAME_HEIGHT
print(fdd.get(3))
print(fdd.get(4))

while True:
    red, frame=fdd.read()
    if red == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)#to clonvert any image into gray scale image
        cv.imshow('frame',gray)
        if cv.waitKey(0) & 0xFF==ord('p'):
            break
    else:
        break
fdd.release()

cv.destroyAllWindows()