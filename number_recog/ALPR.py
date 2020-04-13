import numpy as np
import cv2
import sys
import pytesseract
import pandas as pd
import datetime
import matplotlib.pyplot as plt

font = cv2.FONT_HERSHEY_SIMPLEX

Haar_cascade = cv2.CascadeClassifier('./number_recog/india_license_plate.xml')
txt=''
roi_=0

def ocr(img):
     text = pytesseract.image_to_string(img)
     return text

def date_time():
     dt_date = datetime.datetime.now()
     date = dt_date.strftime("%A, %d %b %Y")
     time = dt_date.strftime("%I:%M %S %p")
     return date,time
#cv2.putText(
#            frame, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, size, color, thickness)

def detect(img):
     #img = cv2.resize(img,(480,360))
     #img = cv2.resize(img,(352,240))
     global txt
     global roi_
     detected = img.copy()
     roi = img.copy()
     plate_rect = Haar_cascade.detectMultiScale(detected, scaleFactor = 1.3, minNeighbors = 7)
     #print(plate_rect)
     for (x,y,w,h) in plate_rect:
          roi_ = roi[y:y+h, x:x+w, :]
          #cv2.imshow('roi before',roi_)
          #_,roi_ = cv2.threshold(roi_,100,200,cv2.THRESH_BINARY) # try adding threshold otsu - Done
          roi_ = cv2.cvtColor(roi_, cv2.COLOR_BGR2GRAY)
          roi_ =  cv2.bilateralFilter(roi_, 11, 17, 17)
          ret3,roi_ = cv2.threshold(roi_,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
          ##roi_ = cv2.adaptiveThreshold(roi_,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            ##cv2.THRESH_BINARY,11,4)
          
          txt = ocr(roi_)
          cv2.rectangle(detected,(x,y),(x+w,y+h),(51,51,255),3)
          cv2.putText(detected, txt, (x, y - 10), font, 1, (0, 0, 255), 2)
     d,t=date_time()
     cv2.putText(detected,d, (10, 30), font, 0.7, (255, 255, 255), 2)
     cv2.putText(detected,t, (10, 70), font, 0.7, (255, 255, 255), 2)
     return roi_,detected,txt



def show(img1,img2,number):
     fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (20,20))
     ax1.imshow(np.squeeze(img1), cmap='gray')
     ax2.imshow(np.squeeze(img2), cmap='gray')
     ax1.axis('off')
     ax1.set_title("Input")
     ax2.axis('off')
     ax2.set_title("Output")
     plt.xlabel(number)
     plt.show()

def video():
     cam = cv2.VideoCapture('car.mp4') # reading the video file.
     fourcc = cv2.VideoWriter_fourcc(*'mp4V')
     out = cv2.VideoWriter('car_output.mp4',fourcc, 20.0, (640,480),True)
     
     while cam.isOpened():
          ret, frame = cam.read() # reading the file frame by frame.
          if ret == True:
               _,fr,_ = detect(frame)
               cv2.imshow('car_output',fr)
               out.write(fr)
               if(cv2.waitKey(1) & 0xFF == 27): # press 'Esc' key to exit anytime.
                    break
          else:
               break
     cam.release()
     out.release()
     cv2.destroyAllWindows()

def videocam():
     cam = cv2.VideoCapture(0)
     while True:
          ret, frame = cam.read(0)
          _,fr,_ = detect(frame) 
          cv2.imshow('video', fr)
          if(cv2.waitKey(1) & 0xFF == 27):
              break
def result(img):
     print(img)
     image = cv2.imread(img)
     roi_,output,txt = detect(image)
     cv2.imwrite('./media/detected_plates/roi.jpg',roi_)
     cv2.imwrite('./media/detected_plates/output.jpg',output)
     return txt

if __name__ == "__main__":
     #image = cv2.imread('truck4.png') #1 #3 #truck2.png
     #image = cv2.resize(image,(480,360))
     #image = cv2.resize(image,(1280,720))
     image = cv2.imread(r'../media/cars/car1.jpeg')
     roi_,output,txt = detect(image)
     cv2.imshow("ROI",roi_)
     #cv2.imwrite("roi.jpg",roi_)
     #cv2.imshow('input',image)
     #cv2.imshow('output',output)
     print(txt)
     show(image,output,txt)
     ##videocam()
     ##video()
