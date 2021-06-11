import cv2
img1 = cv2.imread('starts.jpg')
img1 = cv2.resize(img1,(512,512))
crop_img1 = img1[143:255 , 325:436]
