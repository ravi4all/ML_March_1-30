import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    # ret -> True/False
    # if camera works properly then true will come
    ret, img = capture.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray,1.3)

        for x,y,w,h in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 5)

        cv2.imshow('img',img)
        # print(gray)

    else:
        print("Problem with camera")

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()