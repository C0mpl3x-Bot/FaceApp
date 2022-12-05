#Examples used from https://github.com/bradtraversy/face_recognition_examples
#Library sites used:
#https://pypi.org/project/face-recognition/
#https://docs.python.org/3/library/os.html
#https://pypi.org/project/Pillow/
#https://docs.python.org/3/library/tkinter.html
#https://numpy.org/

#Imports necessary libraries
import face_recognition
import os
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
import numpy as np
def Output(self):

    #error would occur if the user does not fully perfrom the function 
    #such as user does not select an image causing there to be an error but error does not break the application so try and except would fix this error,
    #error occurs as there is no file being selected for it to perfrom the function
    #since error does not break application code in except block just returns
    try:
        #finds the files with all the images of the admins. The names of the admins are in the file name
        path,dirs,files = next(os.walk('./img/knownAdmin'))

        #get the number of files within the knownAdmin folder
        Admin_file_count = len(files)

        #empty array/list
        KnownFaceEncodings = []
        KnownFaceNames = []

        #set i to 0
        i = 0
        #goes through the number of files 
        while i is not Admin_file_count:
            #get the name of each file one by one and saves it to name
            name = files[i]
            #skips the file name .DS_Store which is found on macs.
            if(name != ".DS_Store"):
                #loads the specific file it is on and adds the files face encodings to the KnownFaceEncodings array/list
                KnownFaceEncodings.append(face_recognition.face_encodings(face_recognition.load_image_file("./img/knownAdmin/" + name))[0])

            
                #splits the filename to only get the name of the admin in the file and saves that to the KnownFaceNames array/list
                split_string = name.split(".", 1)
                name = split_string[0]
                KnownFaceNames.append(name)


            #increment i to move to the next file
            i += 1

        #finds the files with all the images of the known users. The names of the known users are in the file name
        path,dirs,files = next(os.walk('./img/known'))
        #get the number of files within the known folder
        known_file_count = len(files)
        
        #set i to 0
        i = 0
        while i is not known_file_count:
            #get the name of each file one by one and saves it to name
            name = files[i]
            #skips the file name .DS_Store which is found on macs.
            if(name != ".DS_Store"):
                #loads the specific file it is on and adds the files face encodings to the KnownFaceEncodings array/list
                KnownFaceEncodings.append(face_recognition.face_encodings(face_recognition.load_image_file("./img/known/" + name))[0])

            
                #splits the filename to only get the name of the person in the file and saves that to the KnownFaceNames array/list
                split_string = name.split(".", 1)
                name = split_string[0]
                KnownFaceNames.append(name)

            #increment i to move to the next file
            i += 1

        #let user select an image to uplaod
        filename = filedialog.askopenfilename()

        #loads the file the user uploaded and saves it to UploadedImages
        UploadedImage = face_recognition.load_image_file(filename)

        #Find faces locations and encodings in UploadedImage Image
        FaceLocationsInImage = face_recognition.face_locations(UploadedImage)
        #gets the face encodings of the face in the UploadedImage using FaceLocationsInImage
        FaceEncodingsInImage = face_recognition.face_encodings(UploadedImage, FaceLocationsInImage)

        #Convert to PIL format so u can draw on the image
        PilImage = Image.fromarray(UploadedImage)

        #Creates an imagedraw instance and saves it to PilDraw
        PilDraw = ImageDraw.Draw(PilImage)

        #loop through faces in the Uploaded Image
        for(top, right, bottom, left), FaceEncoding in zip(FaceLocationsInImage,FaceEncodingsInImage):

            #compares the faces econdings in the uploaded image with the known faces encodings (The ones in the folder) which were saved in a list called KnownFaceEncodings
            Compare = face_recognition.compare_faces(KnownFaceEncodings, FaceEncoding)
            #gets all the faces distances by comparing the face encodings in the uploaded image to the known face encodings (The ones in the folder) which were saved in a list called KnownFaceEncodings
            FaceDistances = face_recognition.face_distance(KnownFaceEncodings, FaceEncoding)
            #gets the lowest index of the face between the KnownFaceEncodings and the face in the Uploaded Image
            FaceMatchIndex = np.argmin(FaceDistances)
            #gets the smallest face distance value 
            ClosestFaceMatch = np.amin(FaceDistances)

            #gets the most similar face in the files by using the smallest index
            if Compare[FaceMatchIndex]:
                #checks the face distance value to see if it is lower than 0.45 to guarantee that the person in the image is the same person in the uploaded image
                if(ClosestFaceMatch < 0.45):
                    #gets the name of the person in KnownFaceNames list/array using the FaceMatchIndex 
                    name = KnownFaceNames[FaceMatchIndex]
            else:
                #if there are no matches set name to unknown
                name = "Unknown"

            # Draw Box that would go around the face
            PilDraw.rectangle(((left,top),(right,bottom)),outline = (255,0,0))

            #Draw label and the black box for the name to go inside and place the name inside the box
            text_width, text_height = PilDraw.textsize(name)
            PilDraw.rectangle(((left,bottom - text_height * 2),(right,bottom)),fill=(0,0,0),outline=(0,0,0))

            #set font and size of text
            fontType = ImageFont.truetype('arial.ttf', 20) 
            #place the text which is the name of the user on to the second rectangle with the correct fontType and fill
            PilDraw.text((left + 6,bottom-text_height-8), name, fill=(255,255,255,255),font = fontType)

        del PilDraw

        #Display image
        PilImage.show()

        #saves the image that is saved to PilImage to a specific folder within the system in JPG form with a unique name 
        PilImage.save('img/IdentifyfaceImages/' + f'{top}.jpg', 'JPEG')

    except:
        return