
# import necessary libraries
import cv2

# open the webcam
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (you can change it based on your setup)

# use a face and body detection function
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")


# check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# main loop for capturing and displaying video
while True:
    # capture frame-by-frame
    ret, frame = cap.read()
      
    # convert the frame into the grayscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    
    # draw the faces on the screen
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0,), 3)


    # check if the frame was captured successfully
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # perform any processing on the frame (optional)
    # e.g., add image processing techniques here

    # display the frame
    cv2.imshow('CCTV Feed', frame)

    # break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()






