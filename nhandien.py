

import cv2
from openpyxl import Workbook
import xlsxwriter
import datetime
import numpy as np
import os
import pandas as pd
from PIL import Image
import sqlite3


#training hình ảnh nhận diện và thư viện nhận diện khuôn mặt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml" )
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('recognizer/trainingData.yml')


#lấy thông tin người dùng
def getProfile(id):
    conn = sqlite3.connect('C:/Users/DELL/Desktop/20212/ĐA1/database/DATA.db')
    query = "SELECT * FROM people WHERE ID =" + str(id)
    cursor = conn.execute(query)

    profile = None

    for row in cursor:
        profile = row
    conn.close()
    return profile

cap= cv2.VideoCapture(0)
fontface=cv2.FONT_HERSHEY_SIMPLEX

ID=[]
NAME=[]
LOP=[]

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,225,0) ,2)
       
        #cắt ảnh người trong camera
        roi_gray = gray[y:y+h, x:x+w]
        id, confidence = recognizer.predict(roi_gray)

        if confidence < 40 :
            profile= getProfile(id)
            if(profile != None):
                cv2.putText(frame, ""+str(profile[1]), (x+10,y+30), fontface,1, (0,255,0),2)

                #lưu vào file exel
                ID.append(str(profile[0]))
                NAME.append(str(profile[1]))
                LOP.append(str(profile[2]))
                if(os.path.exists("du_lieu.xlsx")):
                    os.remove("du_lieu.xlsx")
                    workbook=xlsxwriter.Workbook('du_lieu.xlsx')
                    worksheet= workbook.add_worksheet()
                    worksheet.write('A1', 'ID')
                    worksheet.write('B1', 'NAME')
                    worksheet.write('C1', 'LOP')
                    for item in range(len(ID)):
                        worksheet.write(item+1,0,ID[item])
                        worksheet.write(item+1,1,NAME[item])
                        worksheet.write(item+1,2,LOP[item])
                    
                    
                   
                else:
                    workbook=xlsxwriter.Workbook('du_lieu.xlsx')
                    worksheet= workbook.add_worksheet()
                    worksheet.write('A1', 'ID')
                    worksheet.write('B1', 'NAME')
                    worksheet.write('C1', 'LOP')
                    workbook.close()
                    for item in range(len(ID)):
                        worksheet.write(item+1,0,ID[item])
                        worksheet.write(item+1,1,NAME[item])  
                        worksheet.write(item+1,2,LOP[item])
                 
        else:
            cv2.putText(frame, "Unknow", (x+10,y+30), fontface,1, (0,0,255),2)
    
    
    
    cv2.imshow('image', frame)
    if(cv2.waitKey(1)==ord('q')):
        workbook.close()
        break
    

cap.release()
cv2.destroyAllWindows()


