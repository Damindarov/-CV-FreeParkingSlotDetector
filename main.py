import cv2
import pickle
import cvzone
import numpy as np

#load video
cap = cv2.VideoCapture('carPark.mp4')

width, height = 107, 48 #size of one parking slot

def checkParkingSlot():
    for slot in slotList:
        x, y = slot

        imgCrop = img[y:y+height, x:x+width]
        cv2.imshow(str(x*y),imgCrop)

try:
    with open("CarParkingSlots", "rb") as f:
        slotList = pickle.load(f)
except:
    slotList = []

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)

    kernel = np.ones((3,3), np.unit8)
    imgDilate = cv2.dilate(imgBlur, kernel, iterations=1)

    checkParkingSlot()
    for slot in slotList:
        cv2.rectangle(img, slot, (slot[0] + width, slot[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.imshow("ImageGray", imgGray)
    cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageThresh", imgThreshold)
    cv2.imshow("ImageThresh", imgMedian)
    cv2.waitKey(10)