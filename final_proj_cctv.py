
# import necessary libraries
import cv2
import time
import datetime 
import winsound 

# open the webcam
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (you can change it based on your setup)

# use a face and body detection function
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

# initial variable for recording logic
detection = False
detection_stopped_time = None
timer_started = False
RECORD_DURATION_DETECTION = 5

# set the file directory of the video after recording
save_directory = "C:/Users/Mykha/PLD-PROGRAMS-FILES-PY/PLD-PROGRAMS-CPE1-5/FinalProject/video_recordings"

# setup the frame size that is need for recording
frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

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
    bodies = face_cascade.detectMultiScale(gray, 1.2, 5)


    # draw the faces on the screen
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0,), 3)


    # find the different images within the area of the camera using the threshholding
    _,thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    # create the algorithm/logic for the recording and saving of the detection video with specific time
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
            # start the beeping sound when there is a detection within the area of the draw
            for c in contours:
                if cv2.contourArea(c) < 5000 :
                    continue
            winsound.Beep(500, 100)
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            video_filename = f"{current_time}.mp4"
            video_path = f"{save_directory}/{video_filename}"
            out = cv2.VideoWriter(video_path, fourcc, 9, frame_size)
            print("Started Recording!")
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time > RECORD_DURATION_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stop Recording!")

        else:
            timer_started = True
            detection_stopped_time = time.time()
            
    if detection:
        out.write(frame)


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
out.release()
cap.release()
cv2.destroyAllWindows()






