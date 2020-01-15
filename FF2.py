#https://github.com/aristofun/py-agender
import cv2
import time
from pyagender import PyAgender
cap = cv2.VideoCapture(0)
# параметры могут не применяться к большинству камер
#cap.set(3, 480)  # set width of the frame
#cap.set(4, 640)  # set height of the frame
while True:
    start = time.time()
    ret, image = cap.read()
    faces = PyAgender().detect_genders_ages(image)
    #gender > 0.5 == female
    print(faces)
    for data in faces:
        for key in data:
            if(key=='gender' or key == 'age'):
                if key=='gender':
                    if data[key] <0.5:
                        #print(key)
                        print('Male')
                    else:
                        #print(key)
                        print('Female')
                if key=='age':
                      #print(key)
                      print(data[key])
    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('frame', image)
    print("--- %s seconds ---" % (time.time() - start))
    if cv2.waitKey(1) & 0xFF == ord('q'): # чтобы завершить программу нажать q на ENG раскладке
        break
cap.release()
cv2.destroyAllWindows()
# OUTPUT EXAMPLE:
#[{'left': 65, 'top': 57, 'right': 290, 'bottom': 282, 'width': 225, 'height': 225, 'gender': 0.0150823705, 'age': 19.3277230063934}]
#Male
#19.3277230063934
