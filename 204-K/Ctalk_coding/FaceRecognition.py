# coding:utf-8
#python 2.7
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import numpy
import cv2
#import matplotlib
#import matplotlib.pyplot as plt

# 待检测的图片路径
def FigureProcess():
    imagepath = r'C:\Users\vioiano\Desktop\persons.jpg'
    f=open("haarcascade_frontalface_default.xml",'r')
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # 读取图片
    image = cv2.imread(imagepath)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # 探测图片中的人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor =1.15,
        minNeighbors = 5,
        minSize = (5,5),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    return image

def VideoProcess(videoPath):
    vc=cv2.VideoCapture(videoPath)
    c=0
    list_rc=[]
    fps_o=vc.get(cv2.cv.CV_CAP_PROP_FPS)
    fourcc=cv2.cv.CV_FOURCC(*"MJPG")
    videoWriter=cv2.VideoWriter("new_"+videoPath+"_.avi",fourcc,fps_o/5,(int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(vc.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))))
    if vc.isOpened():
        rval,frame=vc.read()
    else:
        print("false")
        rval=False
    while rval:
        rval,frame=vc.read()
        #rows, cols, channel = frame.shape
        # frame2=cv2.resize(frame,(cols/3,rows/3),fx=0,fy=0,interpolation=cv2.INTER_AREA)
        if ( c%5 == 0):
            #every 5 fps write frame to img
            print("processing")
            videoWriter.write(FigureProcess(frame))
            # cropped001 = frame2[0:300,300:600]   #y change from 0 to 300 x change from 300 to 600
            # cv2.imwrite('./cropped/'+str(c)+'_001.jpg',cropped001)
        c=c+1
        cv2.waitKey(1)
    vc.release()
    videoWriter.release()
    #list_rc=numpy.array(list_rc)
    #T=numpy.arange(0,len(list_rc.T[1]))*(1.0 /(fps_o/5) )

    #plt.plot(T,list_rc.T[1])
    #plt.xlabel("Time(s)")
    #plt.ylabel("Position_x")
    #plt.title("Single channel wavedata")
    #plt.grid('on')#标尺，on：有，off:无。
    #plt.show()

FigureProcess()
