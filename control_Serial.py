import cv2
import serial

# Initialize the serial connection
ser = serial.Serial('COM13', 9600,timeout=1)

# Load the Haar Cascade classifier
classifier = cv2.CascadeClassifier('object.xml')

# Open a camera
cap = cv2.VideoCapture(1)

org =(50,50)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect objects in the frame
    objects = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the objects
    for (x, y, w, h) in objects:
        img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img,'USB',org,font,1,(255,0,0),2,cv2.LINE_AA)
         # Send a byte to Arduino
        char_data = chr(97)  # 97 is ASCII code of 'a'
        ser.write(char_data.encode())
    # Display the frame with the detected objects
    cv2.imshow('Object Detection',img)

    # Check for user input
    key = cv2.waitKey(1)
    if key == 27: # exit on ESC key
        break

# Release the camera and destroy the windows
ser.close()
cap.release()
cv2.destroyAllWindows()
