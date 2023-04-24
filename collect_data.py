import cv2
import os
import time

#######################################################

myPath = "C:/Users/taikh/Desktop/robotic/data_craw" #Rasbperry Pi 

cameraBrightness = 190
moduleVal = 10 #Save every Ith frame avoid repetition

minBlur = 0 # smaller value means more blurriness present 
grayImage =False    #image saved color gray 
saveData = True #save data flag 
showImages = True #Image display flag 
imgWidth =180
imgHeight =120

######################################################

global countFolder 
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,cameraBrightness)

count = 0
countSave =0

def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(myPath+ str(countFolder)):
        countFolder = countFolder+1
    os.makedirs(myPath+str(countFolder))
    
if saveData:saveDataFunc()


while True:
    success,img = cap.read()
    img = cv2.resize(img,(imgWidth,imgHeight))
    if grayImage:img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    if saveData:
        blur =cv2.Laplacian(img,cv2.CV_64F).var()
        if count % moduleVal == 0 and blur >minBlur:
            nowTime = time.time()
            cv2.imwrite(myPath + str(countFolder)+
                        '/'+str(countSave)+" " +str(int(blur))+" "+str(nowTime)+".png",img)
            countSave+=1
        count+=1
    if showImages:
        cv2.imshow("Image",img)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cap.destroyAllWindow()
    
    



