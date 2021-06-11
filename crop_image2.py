import cv2
img2 = cv2.imread('sun.jpg')
img2 = cv2.resize(img2,(512,512))
crop_img2 = img2[143:255, 325:436]
