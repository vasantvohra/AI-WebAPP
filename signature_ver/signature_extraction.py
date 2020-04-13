import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#----
#CANNY=0
def form1(pg,CANNY=0,Filter=0):
    #pg=int(input("Enter form number from 1-3"))
    try:
        if pg == 1 or pg == 2 or pg == 3:
            print("Input images")
            img1 = cv2.imread("./media/input_forms/{}/1.jpg".format(pg))
            img1 = cv2.resize(img1, (2550, 3508))
            img2 = cv2.imread("./media/input_forms/{}/2.jpg".format(pg))
            img2 = cv2.resize(img2, (2550, 3508))
            img3 = cv2.imread("./media/input_forms/{}/3.jpg".format(pg))
            img3 = cv2.resize(img3, (2550, 3508))
    except:
        print("please enter value 1-3")


    # ----
    def mkdir(pg=1):
        try:
            os.mkdir(r'.\media\output_signext\{}'.format(pg))
        except OSError as error:
            print(error)


    mkdir(pg)


    def show(img1, img2, img3):
        # plt.figure(figsize=(10.0,10.0))
        # plt.imshow(img)
        # plt.axis('off')
        # plt.show()
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
        _, ax3 = plt.subplots(1, figsize=(10, 10))
        ax1.imshow(np.squeeze(img1))
        ax2.imshow(np.squeeze(img2))
        ax3.imshow(np.squeeze(img3))
        ax1.axis('off')
        ax1.set_title("Page 1")
        ax2.axis('off')
        ax2.set_title("Page 2")
        ax2.axis('off')
        ax3.set_title("Page 3")
        ax3.axis("off")
        #plt.show()


    def draw_rectangle(img, r1, r2,f=Filter):
        '''Draw bounding rectangle on image with r1 & r2 bouding box'''
        if not f:
            _, img = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY)
        img = cv2.rectangle(img, (r1[0], r1[1] + r2[3]), (r1[0] + r1[2], r1[1]), (0, 255, 0), 2)
        img = cv2.rectangle(img, (r2[0], r2[1] + r2[3]), (r2[0] + r2[2], r2[1]), (0, 0, 255), 2)
        return img


    def extract(img, i, canny=CANNY):
        '''extract the edges from the img, and i = bounding box tuple'''
        # _,img = cv2.threshold(img,155,255,cv2.THRESH_BINARY)
        imCrop = img[int(i[1]):int(i[1] + i[3]), int(i[0]):int(i[0] + i[2])]
        if canny == True:
            imgGray = cv2.cvtColor(imCrop, cv2.COLOR_BGR2GRAY)
            imgGray = cv2.bilateralFilter(imgGray, 9, 30, 30)
            imgEdge = cv2.Canny(imgGray, 120, 230)  # 120,230)
            return imgEdge
        # imgEdge = cv2.dilate(imgEdge, None, iterations=1)
        # imgEdge = cv2.erode(imgEdge, None,iterations=1)
        # resized = cv2.resize(imgEdge,(250,250),interpolation = cv2.INTER_AREA)
        else:
            return imCrop
            # return imgGray


    def page1(pg=1):
        r1_1 = (154, 552, 750, 150)
        r1_2 = (930, 558, 627, 157)
        img = draw_rectangle(img1, r1_1, r1_2)

        cv2.imwrite(r"./media/output_signext/{}/page1.jpg".format(pg), img)
        plt.figure(figsize=(15.0, 15.0))
        plt.imshow(img)
        plt.axis('off')
        #plt.show()
        l = []
        a = 0
        l.append(r1_1)
        l.append(r1_2)
        for i in l:
            a = extract(img, i)
            cv2.imwrite(r"./media/output_signext/{}/page1_{}.jpg".format(pg, i), a)
            plt.imshow(a)
            plt.axis('off')
            #plt.show()
        print("page 1 extracted signature saved at output folder")


    page1(pg)


    def page2(pg=1):
        r4_1 = (129, 1734, 789, 192)
        r4_2 = (1239, 1735, 775, 182)
        img = draw_rectangle(img2, r4_1, r4_2)
        cv2.imwrite(r"./media/output_signext/{}/page4.jpg".format(pg), img)
        ##plt.figure(figsize=(15.0, 15.0))
        ##plt.imshow(img)
        ##plt.axis('off')
        ##plt.show()
        l = []
        l.append(r4_1)
        l.append(r4_2);
        a = 0
        for i in l:
            a = extract(img, i)

            ##f=detect(a)
            ##print(f)
            ##if f: print("blank")

            cv2.imwrite(r"./media/output_signext/{}/page4_{}.jpg".format(pg, i), a)
            plt.imshow(a);
            plt.axis('off');
            #plt.show()
        print("page 4 extracted signature saved")


    page2(pg)


    def page3(pg=1):
        r5_1 = (115, 2994, 833, 170)
        r5_2 = (1211, 3021, 823, 120)
        # (348, 593, 235, 29)
        ##imgGray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
        ##img = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        img = draw_rectangle(img3, r5_1, r5_2)
        cv2.imwrite(r"./media/output_signext/{}/page5.jpg".format(pg), img)
        ##plt.figure(figsize=(10.0, 10.0))
        ##plt.imshow(img)
        #plt.axis('off')
        ##plt.show()
        l = [];
        l.append(r5_1)
        l.append(r5_2)
        a = 0
        for i in l:
            a = extract(img, i)
            """to detect a blank image"""
            ##f=detect(a)
            ##print(f)
            ##if f: print("blank")
            cv2.imwrite(r"./media/output_signext/{}/page5_{}.jpg".format(pg, i), a)
            # plt.figure(figsize=(4.0,4.0),facecolor=(1, 1, 1))
            # file = mpimg.imread("./output/{}/page5_{}.jpg".format(pg,i))
            plt.imshow(a)
            plt.axis('off')
            plt.figsize = (1, 1)
            # .set_size_inches(2,2)
            #plt.show()
        ##l_0 = extract(img3, l[0], False)
        ##l_1 = extract(img3, l[1], False)
        print("page 5 extracted signature saved")


    page3(pg)
if __name__=="__main__":
    
    form1(2)
