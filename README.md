# Problem:- 

Eye movement disorder is a medical condition characterized by abnormalities in the movement of the eyes, which can affect an individual's ability to track moving objects, read, and perform daily activities that require visual attention. This disorder can manifest in various ways, including involuntary eye movements, difficulty focusing on objects, or problems with eye coordination. 

# Solution:- 
# Virtual Keyboard with Eye Tracking
This is a virtual keyboard application that utilizes eye tracking to enable typing without physical input devices. It allows users to control the keyboard and type by blinking their eyes.In this project, users can able to type just by blinking their eyes.
## SetUp and Installation
To run this application, you need to have Python and the following libraries installed:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   
2. Install the following dependencies.
  - OpenCV (cv2)
  - NumPy (numpy)
  - Dlib (dlib)
  - Pyglet (pyglet)
  
3. You can install these dependencies using the following command:

   ```bash
   pip install requirements.txt

4. Download the pre-trained facial landmarks model file from here:
   [Link](https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat)

Usage
Run the script by executing the following command:

Copy code
python virtual_keyboard.py
The application will start and open the webcam feed. Place your face in front of the camera and make sure it is properly detected. You will see a virtual keyboard displayed on the screen. To control the keyboard, follow these instructions:

To select the left or right side of the keyboard, gaze at the corresponding side for a few seconds. The selected side will be highlighted, and the keyboard will play a sound to indicate the selection.
To type a letter, blink your eyes. The active letter on the keyboard will be added to the text input area.
To type a space, blink when the "_" (underscore) key is active.
To delete a character, use the backspace key on your physical keyboard.
The text you type will be displayed in the text input area at the top of the screen.

Acknowledgements
This application utilizes the following libraries and resources:

OpenCV - an open-source computer vision library
Dlib - a toolkit for creating machine learning and computer vision applications
Pyglet - a cross-platform windowing and multimedia library for Python
The facial landmarks model used in this application is the "shape_predictor_68_face_landmarks" model provided by the dlib library.
