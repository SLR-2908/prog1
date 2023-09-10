#Histogram Code 9B :
'''
import cv2
from matplotlib import pyplot as pyplot

img = cv2.imread('Photos/cat.jpg')
histr = cv2.calcHist([img,[0],none,[256],[0,256]])

plt = plot(histr)
plt = show ()

#reading an image Code 9B :
import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow("cats",img)
#cv.waitKey(0)

import cv2 as cv
capture = cv.videocapture("Videos/kitten.mp4")
'''

#while true :
#    is true , frame = capture.read()
#    cv.imshow("video",frame)
#    if waitKey(20)&0*FF==ord(d):
#        break
#capture.release()
#cv.destroyAllWindows()

#image reflection Code 9B:
#import numpy as np
#import cv2 as cv
#img = cv2.imread('Photos/cat.jpg')
#       rows,cols=img.shape
#M=float32([1,0,0]
#             [0,-1,rows]
#             [0,0,1])
#reflected_img=cv.warpPerspective(img,M,(int(cols),int(rows)))
#cv.imshow ("img",reflected_img)
#cv.imwrite('reflected_out.jpg'reflected_img)

#cv.waitKey(0)
#cv.destroyAllWindows()

#image scaling Code 9B:
#import numpy as np
#import cv2 as cv 
#img = cv.imread("Photos/cat.jpg")
#rows,cols=img.shape
#      img_shrinked=cv.resize(img,(250,200),interpolation=cv.INTER_AREA)
#cv.imshow("img",img_shrinked)
#      img.enlarge=cv.resize(img_shrinked,None,fx=1.5,fy=1.5,interpolation=cv.INTER_CUBIC)
#cv.imshow("img",img.enlarge)
#cv.waitKey(0)
#cv.destroyAllWindows()

# colour spaces Code 9B:
'''
import cv2 
img = cv2.imread("Photos/cat.jpg")
B,G,R = cv2.split(img)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.imshow("Blue",B)
cv2.waitKey(0)
cv2.imshow("Red",R)
cv2.waitKey(0)
cv2.imshow("Green",G)
cv2.waitKey(0)

cv2.destroyAllWindows()
'''
#Method 2 of Blurring Code :
#average blurring Code 9B :

import numpy as np
import cv2  
img = cv2.imread("Photos/cat.jpg")
averageBlur= cv2.blur(img,(5,5))
cv2.imshow('original',img)
cv2.imshow("average blurring",averageBlur)
cv2.waitKey(0)

cv2.destroyAllWindows()

#gaussian blurring Code 9B:
import numpy as np
import cv2  
img = cv2.imread("Photos/cat.jpg")
gaussianBlur= cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('original',img)
cv2.imshow("gausian blur",gaussianBlur)
cv2.waitKey(0)

cv2.destroyAllWindows()

#resizeing image Code 9B:

import cv2 as cv
img = cv.imread("Photos/cat.jpg")
cv.imshow('cat',img)
def rescaleframe(frame,scale=0.5)
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return=cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_img=rescaleframe(img)
cv.imshow('image',resized_img)
cv.waitKey(0)




        