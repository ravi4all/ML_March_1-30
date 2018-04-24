import numpy as np
import cv2

dataset = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

font = cv2.FONT_HERSHEY_SIMPLEX

face_1 = np.load('face_1.npy').reshape(20,50*50*3)
face_2 = np.load('face_1.npy').reshape(20,50*50*3)
face_3 = np.load('face_1.npy').reshape(20,50*50*3)

users = {
    0 : 'user_1',
    1 : 'user_2',
    2 : 'user_3'
}

labels = np.zeros((60,1))
labels[0:20,:] = 0.0
labels[20:40,:] = 1.0
labels[40:,:] = 2.0

data = np.concatenate([face_1,face_2,face_3])
print(data.shape)

def distance(x1,x2):
    return np.sqrt(sum(x1 - x2)**2)

def knn(x,train,k=5):
    m = train.shape[0]
    dist = []

    for i in range(m):
        # print("X is",x)
        # print("Train data is",train[i])
        dist.append(distance(x,train[i]))
        # print("Distance is",dist[i])

    dist = np.asarray(dist)
    # print(dist)
    index = np.argsort(dist)
    # print(index)
    sorted_labels = labels[index][:k]
    # print(sorted_labels)
    count = np.unique(sorted_labels, return_counts=True)
    # print(count)
    # print(count[0][np.argmax(count[1])])
    return count[0][np.argmax(count[1])]



cap = cv2.VideoCapture(0)

while True:

    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(gray, 1.3)

        for x, y, w, h in faces:
            face_comp = img[y:y + h, x:x + w, :]
            face_comp = cv2.resize(face_comp, (50, 50))

            lab = knn(face_comp.flatten(), data)
            text = users[int(lab)]
            # print(text)
            cv2.putText(img,text,(x,y),font,1,(0,0,255),2)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)

        cv2.imshow('img',img)

    else:
        print("Some error")

    k = cv2.waitKey(1) & 0xFF
    if k == 27 or len(data) == 20:
        break


cap.release()
cv2.destroyAllWindows()