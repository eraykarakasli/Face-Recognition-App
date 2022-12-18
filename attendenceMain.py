import cv2
from simple_facerec import SimpleFacerec
from datetime import datetime
from datetime import date
from openpyxl import Workbook,load_workbook
import pandas as pd
import openpyxl


today = date.today()
day = today.strftime("%b-%d-%Y")
day_str = "attendance-" + day + ".csv"
print(day_str)

folder = open(day_str, "a")
folder.write("Name, Time")
folder.close()




def attendanceWrite(name):
    with open(day_str, 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')



# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        attendanceWrite(name)
        #############
        cvsDataframe = pd.read_csv(day_str)
        resultExcelFile = pd.ExcelWriter('logggin' + day + '.xlsx')
        cvsDataframe.to_excel(resultExcelFile, index=False)
        resultExcelFile.save()
        #############################
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

