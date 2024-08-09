import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
image=cv2.imread("image1.jpg")
image=cv2.resize(image,(1200,600))
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+h,y+h),(0,255,0),2)
    cv2.imshow("Face Cascade",image)
cv2.waitKey(0)
cv2.destroyAllWindows()