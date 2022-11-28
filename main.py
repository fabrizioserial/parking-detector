import pickle

import cv2 as cv
import numpy as np
import cvzone


cap = cv.VideoCapture('resources/topdownparking.mp4')
width, height = 40,20

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

def checkParkingSpace(imgProp):
    for pos in posList:
        x,y = pos

        imgCrop = imgProp[y:y+height, x:x+width]
        cv.imshow(str(x*y),imgCrop)
        count = cv.countNonZero(imgCrop)
        cvzone.putTextRect(img, str(count),(x,y+height-10), scale=1, thickness=1,offset=0)
        #cv.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
        if count < 200:
            color = (0,255,0)
            trickness = 5
        else:
            color = (0,0,255)
            trickness = 2
        cv.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, trickness)


while True:
    if cap.get(cv.CAP_PROP_POS_FRAMES) == cap.get(cv.CAP_PROP_FRAME_COUNT):
        cap.set(cv.CAP_PROP_POS_FRAMES,0)

    success, img = cap.read()

    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (3,3),1)
    imgThreshold = cv.adaptiveThreshold(imgBlur,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv.THRESH_BINARY_INV,25,16)

    imgMedian = cv.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv.dilate(imgMedian,kernel,iterations=1)
    checkParkingSpace(imgDilate)

    cv.imshow("image", img)
    #cv.imshow("imageBlur", imgBlur)
    #cv.imshow("imageBlur", imgThreshold)
    #cv.imshow("imageBlurMedian", imgMedian)
    cv.waitKey(1)