# Examples used from https://github.com/bradtraversy/face_recognition_examples
#Library sites used:
#https://pypi.org/project/face-recognition/
#https://docs.python.org/3/library/tkinter.html
#https://pypi.org/project/Pillow/

#Imports necessary libraries
import face_recognition
from tkinter import filedialog
from PIL import Image
import os


def Output(self):
    #error would occur if the user does not fully perfrom the function 
    #such as user does not select an image causing there to be an error but error does not break the application so try and except would fix this error,
    #error occurs as there is no file being selected for it to perfrom the function
    #since error does not break application code in except block just returns
    try:

        #ask user to select the image they want to use and save the file path to Filename
        FileName = filedialog.askopenfilename()

        #using face recongition libraries load image file function you can load the image the user selected and save it to UploadedImage
        UploadedImage = face_recognition.load_image_file(FileName)

        #gets the face loaction in the image that the user uploaded and returns a list of tuples of found face loactions in css(top,right,bottom,left) order and saves it to the function FaceLocation
        FaceLocations = face_recognition.face_locations(UploadedImage)

        #for loop that loops over number of face locations found within the image
        for face_location in FaceLocations:
            top, right, bottom, left = face_location

            #gets the faces in the uploaded image
            FaceImage = UploadedImage[top:bottom, left:right]

            #converts the FaceImage to a pil image and saves it to the variable PilImage
            PilImage = Image.fromarray(FaceImage)

            #displays the image that is saved to pil_image
            PilImage.show()

            #saves the image that is saved to PilImage to a specific folder within the system in JPG form with a unique name 
            PilImage.save('img/pullfaceimages/' + f'{top}.jpg', 'JPEG')
    except:
        return

