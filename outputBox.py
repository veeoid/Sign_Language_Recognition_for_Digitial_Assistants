import matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy


#img = np.zeros((512,512,3),np.uint8)
img= np.zeros((200,1200,3), np.uint8)
prediction = 'abcdefg ajajajaj'
#x1, y1, x2, y2 = 100, 100, 300, 300
#img = img[y1:y2, x1:x2]
#img[:] = 255, 0, 0
cv2.namedWindow("Output", cv2.WINDOW_FREERATIO)
#cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
cv2.putText(img,'%s' %(prediction), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
#cv2.putText(img, "Draw shapes lalallalal", (0,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
cv2.imshow("Output", img)

cv2.waitKey(0)