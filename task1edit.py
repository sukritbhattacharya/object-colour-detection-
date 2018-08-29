import cv2
import numpy as np

img = cv2.imread('taskimg.png', cv2.IMREAD_COLOR)

img_height, img_widhth, img_channel = img.shape

#print(img_height, img_widhth, img_channel)

img_height_y = img_height // 2
img_width_x = img_widhth // 2

cv2.circle(img,(img_width_x, img_height_y), 5, (0,255,0), -1)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

red_lower=np.array([136,87,111],np.uint8)
red_upper=np.array([180,255,255],np.uint8)

blue_lower=np.array([0, 249, 206],np.uint8)
blue_upper=np.array([110,255,255],np.uint8)

yellow_lower=np.array([22,30,150],np.uint8)
yellow_upper=np.array([60,255,255],np.uint8)


red=cv2.inRange(hsv, red_lower, red_upper)
blue=cv2.inRange(hsv,blue_lower,blue_upper)
yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)







kernal = np.ones((5 ,5), "uint8")
res=cv2.bitwise_and(img, img, mask = red)
    #blue=cv2.dilate(blue,kernal)
res1=cv2.bitwise_and(img, img, mask = blue)
    #yellow=cv2.dilate(yellow,kernal)
res2=cv2.bitwise_and(img, img, mask = yellow)

(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):

    area = cv2.contourArea(contour)

    if(area>300):


        x,y,w,h = cv2.boundingRect(contour)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.line(img,((x+w//2),(y+h//2)) ,(img_width_x, img_height_y),(255,0,0),5)
        cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))


    (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.line(img,((x+w//2),(y+h//2)) ,(img_width_x, img_height_y),(255,0,0),5)
            cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

    (_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.line(img,((x+w//2),(y+h//2)) ,(img_width_x, img_height_y),(255,0,0),5)
            cv2.putText(img,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))




    cv2.imshow('webcam', img)
    if cv2.waitKey(0)&0xFF == ord('q'):
        break


cv2.destroyAllWindows()