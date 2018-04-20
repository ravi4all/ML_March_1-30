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

labels = np.zeros((60,0))
labels[0:20,:] = 0.0
labels[20:40,:] = 1.0
labels[40:,:] = 2.0

data = np.concatenate([face_1,face_2,face_3])
print(data.shape)

def distance(x1,x2):
    return np.sqrt(sum((x1 - x2)**2))

def knn(x,train,target,k):
    m = train.shape[0]
    dist = []

    for i in range(m):
        dist.append(distance(x,train[i]))

    dist = np.asarray(dist)
    index = np.argsort(dist)

    lab = labels(index)[:k]
    count = np.unique(lab, return_counts=True)
    return count[0][np.argmax(count)]