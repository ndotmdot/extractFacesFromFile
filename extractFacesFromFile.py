import cv2
# import sys
import glob
# import datetime as dt
# from time import sleep
# import numpy as np
import os
import shutil

moveInputFiles = True
dontExportFaces = False
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


fileNames = []
imageList = []
for filename in glob.glob('images/input/*.jpg'):
    fileNames.append(filename.split('/')[2])
    img = cv2.imread(filename)
    imageList.append(img)

i = 0
for image in imageList:
    image = imageList[i]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    f = 1
    for (x, y, w, h) in faces:
        if dontExportFaces:
            # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if dontExportFaces:
                imgCrop = image[y:y+h,x:x+w]
                cv2.imshow( fileNames[i].split('.')[0] + '-face-' + str(f), imgCrop)
        else:
            imgCrop = image[y:y+h,x:x+w]
            cv2.imwrite('images/output/' + fileNames[i].split('.')[0] + '-face-' + str(f) + '.jpg', imgCrop)
        
        f += 1

    if moveInputFiles:
        if faces.size > 0:
            shutil.move('images/input/' + fileNames[i], 'images/input/processed/found-face/' + fileNames[i])
        else:
            shutil.move('images/input/' + fileNames[i], 'images/input/processed/found-no-face/' + fileNames[i])

    print('processed file: ' + fileNames[i])
    i += 1


    if dontExportFaces:
        cv2.waitKey(0)
        cv2.destroyAllWindows()

