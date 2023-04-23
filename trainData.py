import cv2
import numpy as np
import os
from PIL import Image

#https://github.com/opencv/opencv/issues/13848
#print (dir (cv2.face))
recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataSet'

def getImageWithId(path):
    #truy cập vào đường dẫn của ảnh
    imagePaths= [os.path.join(path,f) for f in os.listdir(path)]
  
    faces=[]
    IDs=[]

    for imagePath in imagePaths:
        faceImg= Image.open(imagePath).convert('L')
        faceNp= np.array(faceImg, 'uint8')
        print(faceNp)
 
        Id= int(imagePath.split('\\')[1].split('.')[1])

        faces.append(faceNp)
        IDs.append(Id)

        cv2.imshow('training', faceNp)
        cv2.waitKey(10)
    return faces, IDs
faces, Ids=getImageWithId(path)

recognizer.train(faces, np.array(Ids))

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()



# quét tất cả các cái ảnh 