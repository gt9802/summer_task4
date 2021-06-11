import cv2, numpy
#To create an empty color image we create a 3D array of zeroes:
canvas = numpy.zeros((400,400,3), dtype='uint8')
cv2.circle(canvas,(76,56),50,(0,0,255),-1)
cv2.rectangle(canvas, (277,40), (381,115), (255,0,0), 2)
cv2.ellipse(canvas, (200,50), (50,30), 15, 0, 360, (0,255,0), 2)
cv2.line(canvas, (9,198), (356,373), (0,0,255), 2)
cv2.imshow('img', canvas)
cv2.waitKey()
cv2.destroyAllWindows()
