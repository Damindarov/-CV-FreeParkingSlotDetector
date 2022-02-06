import cv2
import pickle


width, height = 107, 48 #size of one parking slot
try:
    with open("CarParkingSlots", "rb") as f:
        slotList = pickle.load(f)
except:
    slotList = []

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        slotList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, slot in enumerate(slotList):
            x1, y1 = slot
            if x1<x<x1+width and y1<y<y1+height:
                slotList.pop(i)
    with open("CarParkingSlots", "wb") as f:
        pickle.dump(slotList,f)
while True:
    img = cv2.imread("carParkImg.png")
    for slot in slotList:
        cv2.rectangle(img, slot, (slot[0] + width, slot[1] + height), (255, 0, 255), 2)
    cv2.imshow("Test Image", img)
    cv2.setMouseCallback("Test Image", mouseClick)
    cv2.waitKey(1)