import numpy as np
import cv2
xml2 = cv2.CascadeClassifier("mapeamento_100.xml")
xml = cv2.CascadeClassifier("mapeamento.xml")
img = cv2.imread("mima.jpg")
height, width, c = img.shape

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
detectar = xml.detectMultiScale(gray, 1.2, 5)
detectar2 = xml2.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in detectar:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
for (x,y,w,h) in detectar2:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('Mima', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
