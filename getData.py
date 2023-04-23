
#from cv2 import idct
#import numpy as np
import cv2
import sqlite3
import os  # truy cập vào hệ thống



#kết nối tới database
def insertOrUpdate(id, name, lop):
    conn = sqlite3.connect('C:/Users/DELL/Desktop/20212/ĐA1/database/DATA.db')
    query = "SELECT * FROM people WHERE ID=" + str(id)
    cusror = conn.execute(query) # thực thi câu lệnh 
    
    isRecordExist =0  # biến để ktra xem đã có ID chưa để update or insert
    for row in cusror:
        isRecordExist=1  # duyệt từng hàng trên bản ghi nếu đã tồn tại sẽ bằng 1
    if(isRecordExist==0):  # chưa có bản ghi nào 
        query= "INSERT INTO people(ID, NAME, LOP) VALUES("+ str(id)+",'"+str(name)+"','"+str(lop)+"')"
    else:
        query = "UPDATE people SET NAME='"+str(name)+"', LOP='"+str(lop)+"' WHERE ID=" +str(id)
    conn.execute(query)
    conn.commit()
    conn.close()
# nhận  diện mặt trên webcam :

faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml" )
 #truy cập vào webcam
cap = cv2.VideoCapture(0)

#inser database
id = input("Nhập id:")
name= input("Nhập tên: ")
lop=input("Nhập tên lớp học:")
insertOrUpdate(id, name,lop)

sampleNum=0  #chỉ số ảnh

while(True):
    #lấy dữ liệu từ cam
    ret, frame = cap.read()
    #chuyển ảnh về màu xám để train
    gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3,5)
    #vẽ hình vuông
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0),2)  #(0,255,0): màu xanh

        if not os.path.exists('dataSet'):
            os.makedirs('dataSet')

        sampleNum+=1

        cv2.imwrite('dataSet/User.'+str(id)+'.'+str(sampleNum)+'.jpg', gray[y:y+h, x:x+w])
       
    cv2.imshow('frame',frame)
    cv2.waitKey(1)

    if sampleNum>100 :
        break
   
cap.release()  # giải phóng
cv2.destroyAllWindows() # hủy 


# nhập Id tên, lớp
# cam hiện lên và lấy ảnh của mk 200 