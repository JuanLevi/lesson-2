import cv2
import numpy


star=cv2.imread('images\star.jpg')
dot=cv2.imread('images\dot.jpg')
texture=cv2.imread('images\Texture.jpg')
pika=cv2.imread('images\pikachu.png')

# sum = addtion of 2 pictures
add=cv2.addWeighted(src1=star, alpha=0.5, src2=dot, beta=0.3, gamma=1)

cv2.imshow('adition',add)
cv2.waitKey(100)


#subtraction of 2 pictures
sub=cv2.subtract(src1=star, src2=dot)
cv2.imshow('Subtraction',sub)
cv2.waitKey(100)


#image resizing
res=cv2.resize(star,dsize=(300,300))
cv2.imshow('Resizing',res)
cv2.waitKey(100)


#erosion
matrix=numpy.ones((15,5), numpy.uint8)
errosion=cv2.erode(pika, matrix)
cv2.imshow('Erosion', errosion)
cv2.waitKey(100)


#blurring


# gaussian ---> normal blur
gaussian=cv2.GaussianBlur(texture,(11,11),0,0)
cv2.imshow('Gaussian Blur', gaussian)
cv2.waitKey(100)


# median ---> preserve some edges 
median=cv2.medianBlur(texture,11)
cv2.imshow('Median Blur', median)
cv2.waitKey(100)


# bilaterla --> sharp edges are preserved
bilateral=cv2.bilateralFilter(texture,11,79,sigmaSpace=83)
cv2.imshow('Bilateral Blur', bilateral)
cv2.waitKey(100)


#borders 
border=cv2.copyMakeBorder(pika,100,100,100,100,cv2.BORDER_REFLECT)
cv2.imshow('Reflect Border',border)
cv2.waitKey(10000)





























































