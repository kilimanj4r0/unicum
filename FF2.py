import cv2
print(cv2.__version__)
#preparing to read images by camera:
#cap = cv2.VideoCapture(0)
#cap.set(3, 480) #set width of the frame
#cap.set(4, 640) #set height of the frame
#ret, image = cap.read()
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
from pyagender import PyAgender
agender = PyAgender()
faces = agender.detect_genders_ages(cv2.imread(r'E:\Desktop\ALL\python_projects\FF\realme.plus.png'))
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