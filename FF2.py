import os
import time

import cv2
from pyagender import PyAgender

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# параметры могут не применяться к большинству камер
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap.set(3, 480)  # set width of the frame
#cap.set(4, 640)  # set height of the frame

def detect(image):
    agenda = PyAgender()
    ans = agenda.detect_genders_ages(image)
    return ans

def memory():
    import os
    import psutil
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
    print('memory use:', memoryUse)

def mainf():
    while True:
        start = time.time()
        ret, image = cap.read()
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ans = detect(image)
        #agenda = PyAgender()
        #ans = agenda.detect_genders_ages(image)
        #gender > 0.5 == female
        print(ans)
        for data in ans:
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
        print("--- %s seconds ---" % (time.time() - start))
        cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('frame', image)
        memory()
        #tensorflow.contrib.keras.backend.clear_session()
        if cv2.waitKey(1) & 0xFF == ord('q'): # чтобы завершить программу нажать q на ENG раскладке
            cap.release()
            cv2.destroyAllWindows()
            break
if __name__ == "__main__":
    mainf()
# OUTPUT EXAMPLE:
#[{'left': 65, 'top': 57, 'right': 290, 'bottom': 282, 'width': 225, 'height': 225, 'gender': 0.0150823705, 'age': 19.3277230063934}]
#Male
#19.3277230063934
