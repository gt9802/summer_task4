import cv2
#read first image
flag = cv2.imread('IN.jpeg')
#read second image
chhetri = cv2.imread('chhetri.jpeg')
#make sizes equal
flag = cv2.resize(flag, (512,512))
chhetri = cv2.resize(chhetri,(512,512))
#add two images to final_img
final_img = cv2.add( flag,chhetri)
#print image
cv2.imshow('final',final_img)
cv2.waitKey()
cv2.destroAllWindow()  
