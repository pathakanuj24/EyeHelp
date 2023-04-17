import cv2
import numpy as np
import dlib



from math import hypot


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 10)
fps = int(cap.get(10))
print("fps:", fps)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# keyboard settings 
keyboard = np.zeros((600,1000,3), np.uint8)

keys_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T",
              5: "A", 6: "S", 7: "D", 8: "F", 9: "G",
              10: "Z", 11: "X", 12: "C", 13: "V", 14: "B"}

def letter(letter_index,text , letter_light):

    # Keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 200
        y = 0
    elif letter_index == 2:
        x = 400
        y = 0
    elif letter_index == 3:
        x = 600
        y = 0
    elif letter_index == 4:
        x = 800
        y = 0
    elif letter_index == 5:
        x = 0
        y = 200
    elif letter_index == 6:
        x = 200
        y = 200
    elif letter_index == 7:
        x = 400
        y = 200
    elif letter_index == 8:
        x = 600
        y = 200
    elif letter_index == 9:
        x = 800
        y = 200
    elif letter_index == 10:
        x = 0
        y = 400
    elif letter_index == 11:
        x = 200
        y = 400
    elif letter_index == 12:
        x = 400
        y = 400
    elif letter_index == 13:
        x = 600
        y = 400
    elif letter_index == 14:
        x = 800
        y = 400
        
        
        
    width = 200
    height = 200
    th = 3
    if letter_light == True:
        cv2.rectangle(keyboard,(x+th , y+th),(x+width-th, y+height-th),(255,255,255),-1)
    else:
        cv2.rectangle(keyboard,(x+th , y+th),(x+width-th, y+height-th),(255,0,0),3)

    # text settings
    # Text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 10
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 0, 0), font_th)
    font_letter = cv2.FONT_HERSHEY_PLAIN

        
    

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)


font  = cv2.FONT_HERSHEY_DUPLEX

def get_blinking_ratio(eye_points, facial_landmarks):
    # coordinates of left and right part of eye
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y) 
    
    # center
    # coordinates of center top and bottom of eye
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(landmarks.part(eye_points[5]), landmarks.part(eye_points[4]))

    horizontal_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    vertical_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)
    
    Length_of_horizontal_line = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    length_of_vertical_line = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
    
    ratio =  Length_of_horizontal_line/length_of_vertical_line
    return ratio
def get_gaze_ratio(eye_points, facial_landmarks):
    left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                                (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                                (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                                (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                                (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                                (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)
    cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)

    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    # cv2.polylines(mask, [left_eye_region], True, 255, 2)
    cv2.fillPoly(mask, [left_eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)

    min_x = np.min(left_eye_region[:, 0])
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])
    max_y = np.max(left_eye_region[:, 1])
    
    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
    height, width = threshold_eye.shape
    left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
    left_side_white = cv2.countNonZero(left_side_threshold)
    right_side_threshold = threshold_eye[0: height, int(width / 2): width]
    right_side_white = cv2.countNonZero(right_side_threshold)

    if left_side_white == 0:
        gaze_ratio = 1
    elif right_side_white == 0:
        gaze_ratio = 5
    else:
        gaze_ratio = left_side_white / right_side_white
    return gaze_ratio
    



frames = 0
letter_index = 0
while(cap.isOpened()):

    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    new_frame = cv2.resize(frame, (500, 500))
    
    
    frames += 1
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    keyboard[:] = (0, 0, 0)
    new_frame = np.zeros((500, 500, 3), np.uint8)
    faces = detector(gray)
    for face in faces:
        # x,y = face.left(), face.top()
        # x1,y1 = face.right(), face.bottom()
        # cv2.rectangle(frame, (x,y), (x1,y1), (0,255,0), 2)
        
        
        landmarks = predictor(gray, face)
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        
      
        
        
        average_blinking_ratio = (left_eye_ratio + right_eye_ratio)/2
        # print(average_blinking_ratio)
        
        
        if average_blinking_ratio > 3.7:
            cv2.putText(frame, "Blinking", (50, 150), font, 3, (255,0,0))
            
        
        # Gaze detection
        
        left_eye_region = np.array([(landmarks.part(36).x, landmarks.part(36).y),
                                    (landmarks.part(37).x, landmarks.part(37).y),
                                    (landmarks.part(38).x, landmarks.part(38).y),
                                    (landmarks.part(39).x, landmarks.part(39).y),
                                    (landmarks.part(40).x, landmarks.part(40).y),
                                    (landmarks.part(41).x, landmarks.part(41).y)], np.int32)
        
        cv2.polylines(frame, [left_eye_region], True, (0,0,255), 2)
        height, width, _ = frame.shape
        
        # mask to Sepearate the left eye from the rest of the image
        mask = np.zeros((height, width), np.uint8)
        cv2.polylines(mask, [left_eye_region], True, 255, 2)
        cv2.fillPoly(mask, [left_eye_region], 255)
        
        
        left_eye = cv2.bitwise_and(gray, gray, mask=mask)
        
        
        min_x = np.min(left_eye_region[:, 0])
        max_x = np.max(left_eye_region[:, 0])
        min_y = np.min(left_eye_region[:, 1])
        max_y = np.max(left_eye_region[:, 1])
        
        gray_eye = left_eye[min_y: max_y, min_x: max_x]
        _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
        height, width = threshold_eye.shape
        
        left_side_threshold = threshold_eye[0: height, 0: int(width/2)]
        left_Side_White = cv2.countNonZero(left_side_threshold)
        
        
        
        right_side_threshold = threshold_eye[0: height, int(width/2): width]
        right_Side_White = cv2.countNonZero(right_side_threshold)
        
       
        
        
        gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
        gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2
        
        print(gaze_ratio)
        
        if gaze_ratio <1.2:
            cv2.putText(frame, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)
            new_frame[:] = (0, 0, 255)
        elif 3 <= gaze_ratio <= 3.4:
            cv2.putText(frame, "CENTER", (50, 100), font, 2, (0, 0, 255), 3)
        else:
            new_frame[:] = (255, 0, 0)
            cv2.putText(frame, "LEFT", (50, 100), font, 2, (0, 0, 255), 3)

        
        
        cv2.putText(frame, str(left_Side_White), (50, 100), font, 2, (0,0,255), 3)
        cv2.putText(frame, str(right_Side_White), (50, 150), font, 2, (0,0,255), 3)
        threshold_eye = cv2.resize(threshold_eye, None, fx=5, fy=5)
        eye = cv2.resize(gray_eye, None, fx=5, fy=5)
        
        
        
        if frames == 10:
            letter_index += 1
            frames = 0
        if letter_index == 15:
            letter_index = 0
            
        for i in range(15):
            if i == letter_index:
                light = True
            else:
                light = False
            letter(i, keys_set_1[i], light)
        
        
    



        
        
    cv2.imshow('Frame', frame)
    cv2.imshow("New frame", new_frame)
    cv2.imshow("Virtual Keyboard", keyboard)
  

    key = cv2.waitKey(1)
    if key == 27:
        break
        
        
cap.release()
cv2.destroyAllWindows()
