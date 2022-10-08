import os
import cv2
import time
import re
import mediapipe as mp


mp_pose = mp.solutions.pose
pose_image = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils


def detectPose(image_pose, pose, image2):
    
    original_image = image_pose.copy()
    image_in_RGB = cv2.cvtColor(image_pose, cv2.COLOR_BGR2RGB)
    resultant = pose.process(image_in_RGB)

    if resultant.pose_landmarks:    

        mp_drawing.draw_landmarks(image=image2, landmark_list=resultant.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255),
                                                                               thickness=3, circle_radius=3),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(49,125,237),
                                                                               thickness=2, circle_radius=2))
        
    return image2, resultant.pose_landmarks 
    


# path to needed pose image
image_path = 'pose_photo/pose3.jpg'
image2 = cv2.imread('pose_photo/pose1.jpg')

output = cv2.imread(image_path)
res, landmarks = detectPose(output, pose_image, image2)





# with open('pose_landmarks.csv', 'w') as file:
#     writer = csv.writer(file)
#     for data_point in landmarks.landmark:
#         writer.writerow((data_point.x, data_point.y,data_point.z,data_point.visibility))
    
  

cv2.imshow('Pose with Landmarks', res)
cv2.waitKey(2000)
cv2.destroyAllWindows() 








# current_directory = os.getcwd()
# final_directory = os.path.join(current_directory, r'pose_photo')
# if not os.path.exists(final_directory):
#    os.makedirs(final_directory)


# import re
# current_dir = os.path.join(os.getcwd(), r'pose_photo')


# print(current_dir)

# current_directory = os.getcwd()
# final_directory = os.path.join(current_directory, r'pose_photo')
# dirs = os.listdir(final_directory)
# number = re.findall(r'\d+', dirs[-1])
# number = int(number[0])
# pose_file_name = 'pose'+str(number+1)+'.jpg'


