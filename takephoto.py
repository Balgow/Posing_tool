import cv2
import time
import mediapipe as mp
import os
import re

TIMER = int(10)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def get_photo_name():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'pose_photo')
    dirs = os.listdir(final_directory)
    number = re.findall(r'\d+', dirs[-1])
    number = int(number[0])
    pose_file_name = 'pose'+str(number+1)+'.jpg'
    return os.path.join(final_directory, pose_file_name)


cap = cv2.VideoCapture(0)
pose = mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5)

while True:

    ret, img = cap.read()
    cv2.imshow('Pose', img)
    prev = time.time()

    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
    image.flags.writeable = False
    results = pose.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color = (245,117,66), thickness = 15, circle_radius = 4),
        mp_drawing.DrawingSpec(color = (245,66,230), thickness = 4, circle_radius = 2))




    while TIMER >= 0:
        ret, img = cap.read()

        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color = (245,117,66), thickness = 15, circle_radius = 4),
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

        photo_name = get_photo_name()
        cv2.imwrite(photo_name, img)

    break

cap.release()
cv2.destroyAllWindows()