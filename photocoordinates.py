import os
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import csv

mp_pose = mp.solutions.pose
pose_image = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def detectPose(image_path, pose = pose_image):
    image_pose = cv2.imread(image_path)
    original_image = image_pose.copy()
    image_in_RGB = cv2.cvtColor(image_pose, cv2.COLOR_BGR2RGB)
    resultant = pose.process(image_in_RGB)

    if resultant.pose_landmarks:    

        mp_drawing.draw_landmarks(image=original_image, landmark_list=resultant.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255),
                                                                               thickness=3, circle_radius=3),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(49,125,237),
                                                                               thickness=2, circle_radius=2))
        
    return original_image, resultant.pose_landmarks 
    


# path to needed pose image
# image_path = 'pose_photo/pose3.jpg'
# output = cv2.imread(image_path)
# res, landmarks = detectPose(image_path, pose_image)


# cv2.imshow('Pose with Landmarks', res)
# cv2.waitKey(2000)
# cv2.destroyAllWindows() 

