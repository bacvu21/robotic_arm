import cv2
import os

# Set up camera object
cap = cv2.VideoCapture(0)

# Set capture resolution
cap.set(3, 64) # Width
cap.set(4, 64) # Height

# Create folder to store captured images
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

# Function to capture images from webcam
def capture_images(num_images):
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if ret:
            img_name = os.path.join("captured_images", f"image_{count}.png")
            cv2.imwrite(img_name, frame)
            count += 1
            print(f"Image {count} captured")
            cv2.imshow('frame',frame)
    cap.release()
    cv2.destroyAllWindows()

# Capture 10 images and save them in 64x64 resolution
capture_images(10)
