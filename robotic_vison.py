import cv2  
import numpy as np
from util import get_spots_boxes,empty_or_not
import matplotlib.pyplot as plt
#import serial
import threading
from flask import Flask, Response, render_template
import time 


app = Flask(__name__)


    
def calc_diff(img1,img2):
    return np.abs(np.mean(img1)-np.mean(img2))


#######################################################
#                                                     #
# Serial part                                         #
#                                                     #
#######################################################

#ser = serial.Serial('COM13', 9600,timeout=1)

mask = 'mask4.png'
cap = cv2.VideoCapture(0)

# cap.set(3, 1280) # Width
# cap.set(4, 720) # Height



mask = cv2.imread(mask,0)


connected_component = cv2.connectedComponentsWithStats(mask,4,cv2.CV_32S)

spots = get_spots_boxes(connected_component)

spots_status = [None for j in spots ]
diffs = [None for j in spots]
print(spots[0])
print(spots[1])
print(spots[2])
print(spots[3])
print(spots[4])
print(spots[5])








def process_():
    step = 10 
    previous_frame = None
    frame_nmr = 0
    ret = True
    while ret : 
        ret,frame = cap.read()
        
        if frame_nmr %step == 0 and previous_frame is not None:     
            for spot_indx, spot in enumerate(spots):
                x1,y1,w,h = spot
                spot_crop = frame[y1:y1+h,x1:x1 +w,:]
                
                diffs[spot_indx] =calc_diff(spot_crop,previous_frame[y1:y1+h,x1:x1+w,:])
                
            print([diffs[j] for j in np.argsort(diffs)][::-1])   
            # plt.figure()
            # plt.hist([diffs[j]/np.amax(diffs) for j in np.argsort(diffs)][::-1])
            # # if frame_nmr ==300:
            # #     plt.show()
                
                
                
        if frame_nmr %step == 0:
            
            for spot_indx, spot in enumerate(spots):
                x1,y1,w,h= spot
        
                spot_crop = frame[y1:y1 +h,x1:x1 +w,:]
                
                spot_status = empty_or_not(spot_crop)
                
                spots_status[spot_indx] = spot_status
        
        if frame_nmr %step ==0:
            previous_frame = frame.copy()
                
        for spot_indx, spot in enumerate(spots): 
                
            spot_status = spots_status[spot_indx]
            x1,y1,w,h = spots[spot_indx]
            
            if spot_status:
                frame =cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0,255,0),2)
            
            else:
                frame =cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(0,0,255),2)
                # if spots[spot_indx]==spots[0]:
                #       frame =cv2.putText(frame, "Vi tri 2", (13,152), cv2.FONT_HERSHEY_SIMPLEX,1,
                #                  (0, 0, 255),2, cv2.LINE_AA, True)

                #       char_data = chr(98)# is ASCII code of 'a'
                #       ser.write(char_data.encode())
                #       time.sleep(0.2)

                #       char_data = chr(103)# is ASCII code of 'a'
                #       ser.write(char_data.encode())
                # elif spots[spot_indx]==spots[1]:
                #       frame =cv2.putText(frame, "Vi tri 3", (207,152), cv2.FONT_HERSHEY_SIMPLEX,1,
                #                  (0, 0, 255),2, cv2.LINE_AA, True)
                #       char_data = chr(99)  # 97 is ASCII code of 'b'
                #       ser.write(char_data.encode())
                #       time.sleep(0.2)

                #       char_data = chr(103)# is ASCII code of 'a'
                #       ser.write(char_data.encode())
                # elif spots[spot_indx]==spots[2]:
                #       frame =cv2.putText(frame, "Vi tri 5", (434,153), cv2.FONT_HERSHEY_SIMPLEX,1,
                #                  (0, 0, 255),2, cv2.LINE_AA, True)
                #       char_data = chr(101)  # 97 is ASCII code of 'c'
                #       ser.write(char_data.encode())
                #       time.sleep(0.2)

                #       char_data = chr(103)# is ASCII code of 'a'
                #       ser.write(char_data.encode())
                # elif spots[spot_indx]==spots[3]:
                #       frame =cv2.putText(frame, "Vi tri 1", (13,170), cv2.FONT_HERSHEY_SIMPLEX,1,
                #                  (0, 0, 255),2, cv2.LINE_AA, True)
                #       char_data = chr(97)#97 is ASCII code of 'd'
                #       ser.write(char_data.encode())
                #       time.sleep(0.2)

                #       char_data = chr(103)# is ASCII code of 'a'
                #       ser.write(char_data.encode())
                # elif spots[spot_indx]==spots[4]:
                #       frame =cv2.putText(frame, "Vi tri 4", (215,170), cv2.FONT_HERSHEY_SIMPLEX,1,
                #                  (0, 0, 255),2, cv2.LINE_AA, True)
                #       char_data = chr(100)  # 97 is ASCII code of 'e'
                #       ser.write(char_data.encode())
                #       time.sleep(0.2)

                #       char_data = chr(103)# is ASCII code of 'a'
                #       ser.write(char_data.encode())
                # elif spots[spot_indx]==spots[5]:
                #       frame =cv2.putText(frame, "Vi tri 6", (433,171), cv2.FONT_HERSHEY_SIMPLEX,1,
                #                  (0, 0, 255),2, cv2.LINE_AA, True)
                #       char_data = chr(102)  # 97 is ASCII code of 'f'
                #       ser.write(char_data.encode())
                #       time.sleep(0.2)
                #       char_data = chr(103)# is ASCII code of 'a'
                #       ser.write(char_data.encode())
        cv2.rectangle(frame,(50,490),(400,400),(0,0,0),-1)
        cv2.putText(frame,'slots:{}/{}'.format(str(sum(spots_status)),str(len(spots_status))),(60,450),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        #cv2.imshow('frame',frame)
           
       
        
        ret,buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

    # Yield the encoded frame as a byte string
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        
        
        if cv2.waitKey(25) & 0xFF ==ord('q'):
            break
        
        frame_nmr+=1


@app.route('/video_feed')
def video_feed():
    # Return a response object that streams the video
    return Response(process_(), mimetype='multipart/x-mixed-replace; boundary=frame')
# Define a Flask route to render the web page that displays the video
@app.route('/')
def main():
    return render_template('index1.html')

if __name__ == '__main__':
     # Start the video stream in a separate thread
    t = threading.Thread(target=process_)
    t.daemon = True
    t.start()

    # Run the Flask app in the main thread
    app.run(debug=True, host='0.0.0.0',port = 80)
    
#ser.close()
cap.release()
cv2.destroyAllWindows()