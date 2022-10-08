import cv2 as cv
import mediapipe as mp
import numpy as np
import os



def create_dir():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'pose_photo')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)






create_dir()

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:

    while cap.isOpened():
        ret, image = cap.read()

        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color = (245,117,66), thickness = 15, circle_radius = 4),
            mp_drawing.DrawingSpec(color = (245,66,230), thickness = 4, circle_radius = 2))



        cv.imshow("Posing Webcam", image)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv.destroyAllWindows()
