import cv2
from simple_facerec import SimpleFacerec


#Encode faced from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")


#Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

#Detect Faces
    face_location, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_location, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (94, 224, 69), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyWindow()
