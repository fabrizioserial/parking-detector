import pickle

import cv2 as cv
import numpy as np
from PIL import ImageColor

width, height = 40,20

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

img = cv.imread('resources/parking.png')
# cap = cv.VideoCapture('resources/topdownparking.mp4')


def mouseClick(events, x,y,flags, params):
    if events == cv.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            x1,y1 = pos
            if x1 < x <x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList,f)

while True:
    # success, img = cap.read()

    for pos in posList:
        cv.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255,0,255),2)

    cv.imshow("image", img)
    cv.setMouseCallback("image", mouseClick)
    cv.waitKey(1)
