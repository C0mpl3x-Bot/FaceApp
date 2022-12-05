#Library sites used:
#https://pypi.org/project/face-recognition/
#https://opencv.org/ 
#https://numpy.org/

#Imports necessary libraries
import face_recognition
import cv2
import os
import numpy as np

def Face_recogntion(self):
    
    #Opens a video file or a capturing device or an IP video stream for video capturing with API Preference. 
    #0 is used as a parameter to return the first webcam on your device.
    WebCam = cv2.VideoCapture(0)

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
    #Initialise new variables
    FaceLocationsInCam = []
    FaceEncodingsInCam = []
    RunFrame = True
    Running = True;
    color = (0,0,255)
    Access = "Processing"
    name = "Processing"

    #runs until running is false
    while Running:
        #ret returns true if frame is available
        #Frame will get the next frame in the web cam
        ret,frame = WebCam.read()

        #scales down the frame to 1/10 for faster processing
        new_frame = cv2.resize(frame, (0, 0), fx=0.1, fy=0.1)
        #convert BGR to RGB colour because opencv orders colors as blue green red whilst the traditional way is rgb
        rgb_frame = new_frame[:, :, [2, 1, 0]]

        #runs every other frame since it becomes true then false stopping it from constantly running making 
        #the app run smoother.
        if RunFrame:
            #gets the face locations in the frame and saves it to FaceLocationsInCam 
            FaceLocationsInCam  = face_recognition.face_locations(rgb_frame)
            #gets the face encodings of the face in the web cam
            FaceEncodingsInCam = face_recognition.face_encodings(rgb_frame,FaceLocationsInCam)

            #See if the face in the webcam is a match with any of the known faces
            for x in FaceEncodingsInCam:

                #compares the faces econdings in the frame with the known faces encodings (The ones in the folder) which were saved in a list called KnownFaceEncodings
                Compare = face_recognition.compare_faces(KnownFaceEncodings, x)

                #gets all the faces distances by comparing the face encodings in the frame to the known face encodings (The ones in the folder) which were saved in a list called KnownFaceEncodings
                FaceDistances = face_recognition.face_distance(KnownFaceEncodings, x)
                #gets the lowest index of the face between the KnownFaceEncodings and the face in the webcam
                FaceMatchIndex = np.argmin(FaceDistances)
                #gets the smallest face distance value 
                ClosestFaceMatch = np.amin(FaceDistances)

                #gets the most similar face in the files by using the smallest index
                if Compare[FaceMatchIndex]:
                    #checks the face distance value to see if it is lower than 0.45 to guarantee that the person in the image is the same person in the webcam
                    if(ClosestFaceMatch < 0.45):
                        #gets the name of the person in KnownFaceNames list/array using the FaceMatchIndex 
                        name = KnownFaceNames[FaceMatchIndex]
                        #sets access to access granted
                        Access = "ACCESS GRANTED"
                        #color changes to green
                        color = (0,255,0)
                else:
                    #if there are no matches
                    name = "Unknown"
                    #sets access to access denied
                    Access = "ACCESS DENIED"
                    #color changes to red
                    color = (0,0,255)
                


        #allows the box to move with the face since you are setting RunFrame to not RunFrame
        #allowing it to update the frame since it is setting run frame to false and true so it would update the information being outputted
        #every frame allowing the box to move with the face in the webcam
        RunFrame = not RunFrame
        
        #displays result on the screen where the app is detecting the faces
        for(top,right,bottom,left), x in zip(FaceLocationsInCam ,FaceEncodingsInCam):
            #resizes face locations to 10 times its size since the face detected was in 1/10 size
            top *= 10
            right *= 10
            bottom *= 10
            left *= 10

            #draws a box around the face. if user is recognised the color is green if user is not recognised the color is red
            cv2.rectangle(frame,(left,top),(right,bottom),color,2)

            #draws a rectangle underneath the other rectangle which displays the detected users name
            cv2.rectangle(frame, (left, bottom - 45), (right, bottom), color, cv2.FILLED)

            #sets the font for the text that will be displayed on the webcam output
            TextFont = cv2.FONT_HERSHEY_TRIPLEX
            #puts the name inside the second rectangle.
            cv2.putText(frame, name, (left + 6, bottom - 6), TextFont, 1.0, (255, 255, 255), 1)

            #another rectangle is created to display whether the user has access or not so if user 
            #is recognised by the face app then the user would have access granted other wise it will be 
            #access denied
            cv2.rectangle(frame, (left-1, bottom+40), (right+1, bottom), color ,cv2.FILLED)
            cv2.putText(frame, Access, (left + 6, bottom + 30), TextFont, 1.0, (255,255,255), 1)

        #display the video frame by frame
        cv2.imshow('Video',frame)

        #Face Cam will keep being used until escape is pressed on the keyboard which would quit it.
        if cv2.waitKey(1) == 27:
            Running = False
            break
            
    #stops app from running and closes all the windows open and stops using the webcam.
    WebCam.release()
    cv2.destroyAllWindows()