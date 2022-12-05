#Library sites used:
#https://docs.python.org/3/library/tkinter.html
#https://docs.python.org/3/library/os.html
#https://numpy.org/

#Imports necessary libraries
from tkinter import *
import tkinter
# import face_recognition
import os
# import cv2
import numpy as np
from tkinter import messagebox

#import login_facerecognition file
import Login_FaceRecognition

class MyWindow1:
    
    def __init__(self, win):
        #finds the files with all the images of the admins. The names of the admins are in the file name
        path,dirs,files = next(os.walk('./img/knownAdmin'))
        #get the number of files within the knownAdmin folder
        Admin_file_count = len(files)

        #initialise i as 0
        i = 0
        while i is not Admin_file_count:
            #get the name of each file one by one and saves it to name
            name = files[i]
            #skips the file name .DS_Store which is found on macs.
            if(name == ".DS_Store" and Admin_file_count > 0):
                #subtract one from Admin file count as .DS_STORE is a file that is found on macs
                Admin_file_count -= 1
                #checks if Admin_file_count is equal to 0 if it is then it would stop the while loop from running
                if(Admin_file_count == 0):
                    break;
            i+=1

        #checks if there is an admin within the system if there is it would have the following output on the login/signup window
        if(Admin_file_count > 0):
            #Creates label on the window with text
            self.label = Label(window,bg = '#A9A9A9',fg = "black", text ="Welcome to the login to login press the button below")
            #places the label on the window
            self.label.pack(pady = 10)

            #creates the button for login
            #button btn
            self.btn = Button(window, text ="Login", fg="black", highlightbackground= '#A9A9A9', bg='#A9A9A9',  command = self.LoginOrSignup)
            self.btn.pack(pady = 10)

        #if there are no admins then it would have the following output on the login/signup window
        else:
            #Creates label on the window with text
            self.label = Label(window,bg = '#A9A9A9',fg = "black", text ='Welcome to the Signup Frame to Signup press the button below.' "\n" 'Once you press the button please select an image of your face so you can login.')
            #places the label on the window
            self.label.pack(pady = 10)

            #creates the button for Signup
            #button btn
            self.btn = Button(window, text ="Sign up", fg="black", highlightbackground= '#A9A9A9', bg='#A9A9A9',  command = self.LoginOrSignup)
            self.btn.pack(pady = 10)


        #used to handle window close event
        window.protocol("WM_DELETE_WINDOW",  self.CloseApp) 


    #if the login or signup button is pressed then this function would be called
    def LoginOrSignup(self):

        #finds the files with all the images of the admins. The names of the admins are in the file name
        path,dirs,files = next(os.walk('./img/knownAdmin'))
        #get the number of files within the knownAdmin folder
        Admin_file_count = len(files)

        #initialise i as 0
        i = 0
        #loop over the number of admin files
        while i is not Admin_file_count:
            #get the name of each file one by one and saves it to name
            name = files[i]
            #skips the file name .DS_Store which is found on macs.
            if(name == ".DS_Store" and Admin_file_count > 0):
                #subtract one from Admin file count as .DS_STORE is a file that is found on macs
                Admin_file_count -= 1
                #checks if Admin_file_count is equal to 0 if it is then it would stop the while loop from running
                if(Admin_file_count == 0):
                    break;
            #increment i to move to the next file
            i+=1
        #check if Admin file count is greater than 0
        if(Admin_file_count > 0):
            #minimise the SignUp/Login Window
            window.withdraw()
            #call the face recognition login function
            Login_FaceRecognition.LoginFace_recogntion(self)

        #if admin file count is less than or equal to 0 then the following would run
        else:
            #minise the SignUp/Login Window
            window.withdraw()
            #import AdminUploadImage file to allow users to signup
            import AdminUploadImage
            #call output function from Admin Upload Image to allow users to signup as admins
            AdminUploadImage.Output(self,window)
            #Once that is done run LoginWindow again to allow user to now login to the system as an admin exists allowing login to be possible
            import LoginWindow
            
    #close function which gives the user the warning before they close the pop up window.  
    def CloseApp(self):
        #if x is pressed then the question is asked if user presses ok then exit() is ran
        if messagebox.askokcancel("Quit",  "Do you want to exit from the application?"):
            exit()     

#intialise tk window
#create instance of tk
window=tkinter.Tk()
#sets the frames title
window.title('Secure Face Recognition App')
mywin=MyWindow1(window)
#sets the size of the frame
window.geometry("600x500+10+10")
#sets background colour of the frame
window.configure(bg='#A9A9A9')
#runs the tkinter event loop and listens for button events eg button clicks
window.mainloop()
