import os
import cv2
import mediapipe as mp
import csv
from photocoordinates import detectPose
import time


TIMER = int(20)
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose




photo, poselandmarks = detectPose('pose_photo/pose8.jpg')




cv2.imshow('Pose with Landmarks', photo)
cv2.waitKey(2000)
cv2.destroyAllWindows() 


cap = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:

    while cap.isOpened():
        ret, image = cap.read()
        prev = time.time()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(image, poselandmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color = (200,17,166), thickness = 8, circle_radius = 4),
            mp_drawing.DrawingSpec(color = (145,166,20), thickness = 4, circle_radius = 2))


        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color = (245,117,66), thickness = 8, circle_radius = 4),
            mp_drawing.DrawingSpec(color = (245,66,230), thickness = 4, circle_radius = 2))


        while TIMER >= 0:
            ret, image = cap.read()

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            mp_drawing.draw_landmarks(image, poselandmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color = (200,17,166), thickness = 8, circle_radius = 4),
                mp_drawing.DrawingSpec(color = (145,166,20), thickness = 4, circle_radius = 2))


            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color = (245,117,66), thickness = 8, circle_radius = 4),
                mp_drawing.DrawingSpec(color = (245,66,230), thickness = 4, circle_radius = 2))
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, str(TIMER),
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)
            cv2.imshow('Pose', image)
            cv2.waitKey(10)

            cur = time.time()

            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1

        else:
            ret, img = cap.read()

            cv2.imshow('Pose', img)
            cv2.waitKey(2000)

            photo_name = 'result_photo/result.jpg'
            cv2.imwrite(photo_name, img)

        break

cap.release()
cv2.destroyAllWindows()