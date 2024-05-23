import cv2 as cv
"""in this tutoril we learned how to axis our camera"""
fdd=cv.VideoCapture(0);
fourcc=cv.VideoWriter_fourcc(*'XVID')
'''FourCC is a 4-byte code used to specify the video codec. List of codes can be obtained at Video Codecs by FourCC. The codecs for Windows is DIVX and for OSX is avc1, h263. FourCC code is passed as cv2'''
out = cv.VideoWriter("output.mp4", fourcc, 20.0,(640,480))#it will store the output taken from the camera
print(fdd.isOpened())#it will tell us that the vedio or image is opened or not


while True:
    red, frame=fdd.read()
    if red == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)#to clonvert any image into gray scale image
        cv.imshow('frame',gray)
        print(fdd.get(cv.CAP_PROP_FRAME_WIDTH))
        print(fdd.get(cv.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)

        if cv.waitKey(0) & 0xFF==ord('p'):
            break
    else:
        break
fdd.release()
out.release()
cv.destroyAllWindows()