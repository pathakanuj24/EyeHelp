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

5. Run the script by executing the following command:

   ```bash
   python main.py 

The application will start and open the webcam feed. Place your face in front of the camera and make sure it is properly detected. You will see a virtual keyboard displayed on the screen. 

### To control the keyboard, follow these instructions:

- You can select the left or right side of the keyboard by gazing at the corresponding side for a few seconds. You will hear a sound left or right depending on the side you select. Once that is selected, it will display the gaze side virtual keyboard. 
- To type a letter, blink your eyes. The active letter on the keyboard will be added to the text input area or frame.
- The text you type will be displayed in the text input area at the top of the screen.


