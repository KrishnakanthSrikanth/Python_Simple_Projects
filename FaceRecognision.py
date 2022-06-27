import numpy as np
import cv2

read=cv2.imread('image/Group.jpg', 0)
print("Read:",read)

read = np.full((100,80,3), 12, np.uint8)
print("Read1:",read)

gray = cv2.cvtColor(read,cv2.COLOR_BGR2GRAY)
print("Gray:",gray)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("face_cascade:",face_cascade)

#face_cascade.load('image/haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.10, 5)
print(len(faces))

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
cv2.imshow("Image",read)
cv2.waitKey(0)
cv2.destroyAllWindows()

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# path = "haarcascade_frontalface_default.xml"
#
# face_cascade = cv2.CascadeClassifier(path)
#
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
# print(len(faces))
#
# for (x, y, w, h) in faces:
# 	cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()