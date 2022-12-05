# Examples used from https://github.com/bradtraversy/face_recognition_examples
#Library sites used:
#https://docs.python.org/3/library/tkinter.html
#https://docs.python.org/3/library/os.html
#https://pypi.org/project/face-recognition/
#https://numpy.org/

#Imports necessary libraries
from tkinter import *
from tkinter import filedialog
import os
import face_recognition
from tkinter import messagebox
import numpy as np

def Output(self, win):
    #error would occur if the user does not fully perfrom the function 
    #such as does not select an image causing there to be an error but error does not break the application so try and except would fix this error,
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
            i+=1

        #set i to 0
        i = 0
        #finds the files with all the images of the known users. The names of the known users are in the file name
        path,dirs,files = next(os.walk('./img/known'))
        #get the number of files within the known folder
        known_file_count = len(files)
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
            i+=1
        
        #allows user to select the file they want to use
        filename = filedialog.askopenfilename()

        #empty string which would be replaced with the results of the users input so the results can be displayed to the user
        msg = " "
        #image uploaded by user
        UnknownImage = face_recognition.load_image_file(filename)
        #gets number of faces within the image
        numberOfFaces = len(face_recognition.face_encodings(UnknownImage))

        #intialise NumberOfUnknownFaces as 0
        NumberOfUnknownFaces = 0;

        #intialise NumberOfKnownFaces as 0
        NumberOfKnownFaces = 0;
        
        #iterate over number of faces within the image
        for j in range(numberOfFaces):
            #gets the face encodings of the speicific face in the image and saves it to UnknownFaceEncoding
            UnknownFaceEncoding = face_recognition.face_encodings(UnknownImage)[j]
            
            
            #compares the faces econdings in the uploaded image with the known faces encodings (The ones in the folders) which were saved in a list called KnownFaceEncodings
            Compare = face_recognition.compare_faces(KnownFaceEncodings, UnknownFaceEncoding)
            #gets all the faces distances by comparing the face encodings in the uploaded image to the known face encodings (The ones in the folders) which were saved in a list called KnownFaceEncodings
            FaceDistances = face_recognition.face_distance(KnownFaceEncodings, UnknownFaceEncoding)
            #gets the lowest index of the face distance between the KnownFaceEncodings and the face in the uploaded image
            FaceMatchIndex = np.argmin(FaceDistances)
            #gets the smallest face distance value 
            ClosestFaceMatch = np.amin(FaceDistances)

            #gets the most similar face in the files by using the smallest index
            if Compare[FaceMatchIndex]:
                #checks the face distance value to see if it is lower than 0.45 to guarantee that the person in the known images folder is the same person in the uploaded image and checks if NumberOfKnownFaces is less than 1
                if(ClosestFaceMatch < 0.45 and NumberOfKnownFaces < 1):
                    #add the following result to msg
                    msg += f'In the image there is ' + KnownFaceNames[FaceMatchIndex]
                    #increment NumberOfKnownFace
                    NumberOfKnownFaces += 1
                #check if ClosestFaceMatch is less than 0.45 and NumberOfKnownFaces is greater than or equal to 1
                elif(ClosestFaceMatch < 0.45 and NumberOfKnownFaces >= 1):
                    #add the following result to msg
                    msg += f' and ' + KnownFaceNames[FaceMatchIndex]
                    #increment NumberOfKnownFace
                    NumberOfKnownFaces += 1
                #check if numberOfFaces is less than or equal to 1 and closest facematch is greater than 1 meaning that the person is not in the database
                elif(ClosestFaceMatch >= 0.45 and numberOfFaces <= 1):
                    #increment NumberOfKnownFace               
                    NumberOfUnknownFaces += 1
            else:
                #check if closestFaceMatch is greater than 0.45 and that numberOfFaces  is greater than 1
                if((ClosestFaceMatch >= 0.45 and numberOfFaces > 1) or (ClosestFaceMatch >= 0.45 and numberOfFaces <= 1)):
                    #increment NumberOfKnownFace  
                    NumberOfUnknownFaces += 1
                #check if no one in the photo is recognised by the system by checking if NumberOfUnknownFaces is equal to numberOfFaces
                if(ClosestFaceMatch >= 0.45 and NumberOfUnknownFaces == numberOfFaces):
                    #if NumberOfUnknownFacess is equal to number of faces then set msg to the following
                    msg= f'We are unable to identify anyone in the image'
            
        
        #checks NumberOfUnknownFace is equal to 1 and that numberOfFaces is greater than 1
        if(NumberOfUnknownFaces == 1 and numberOfFaces > 1):
            #add the following result to msg
            msg += f" and we were unable to identify " + str(NumberOfUnknownFaces) + " person"
        #If the statement above is not ture then it would check if NumberOfUnkownFaces is greater than 1 and that NumberOfUnkown faces is less than NumberOfFaces
        elif(NumberOfUnknownFaces > 1 and NumberOfUnknownFaces < numberOfFaces):
            #add the following result to msg
            msg += f" and we were unable to identify " + str(NumberOfUnknownFaces) + " people"

        #intialise global variables
        global pop
        global pop_label
        global pop_button

        #intialise popup window for the FaceMatch result to be displayed on
        pop = Toplevel(win)
        pop.title("Face Match Result") 
        pop.geometry("500x250")        
        pop.config(bg="#A9A9A9")

        #create a label which would be displayed on the pop up screen which would contain the result of the users uploaded image by displaying what is saved to msg
        pop_label = Label(pop,text=msg, bg = '#A9A9A9' , fg = "black", font=("helvetica",12))
        pop_label.pack(pady=10)    

        #used to handle pop up window close event
        pop.protocol("WM_DELETE_WINDOW", close_pop)
    except:
        return

#close function which gives the user the warning before they close the pop up window.
def close_pop():
    #if x button is pressed then the question is asked if user presses ok then pop.destroy() is ran
    if messagebox.askokcancel("Quit", "Do you want to quit Face Match?"):
        pop.destroy()      
