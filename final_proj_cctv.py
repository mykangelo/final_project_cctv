
# import necessary libraries
import cv2

# open the webcam
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (you can change it based on your setup)

# check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# main loop for capturing and displaying video
while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    # check if the frame was captured successfully
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # cerform any processing on the frame (optional)
    # e.g., you can add image processing techniques here

    # display the frame
    cv2.imshow('CCTV Feed', frame)

    # break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()






