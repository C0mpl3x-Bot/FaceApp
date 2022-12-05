#Library sites used:
#https://docs.python.org/3/library/tkinter.html

#Imports necessary libraries
import tkinter
from tkinter import *
from tkinter import messagebox

class MyWindow:
    def __init__(self, win):

        #Creates label on the window with text
        self.label = Label(window,bg = '#A9A9A9',fg = "black", text='Select the function you would like to perform by clicking the one of the buttons below.'  "\n"  'If you select face recognition to quit press esc'
        "\n" 'The upload image function would move the image you have slected into our system.' "\n" 'The image name needs to end with either jpg or png or jpeg.' "\n" 'Please set the name of the file to the person in the image eg username.jpg or username.png')
        #puts the label in the speicifed location on the window
        self.label.place(x = 30, y = 30)
        
        #creates the button for logout
        #button ButtonLogout
        self.ButtonLogout = Button(win, text = 'Logout', fg="black", highlightbackground= '#A9A9A9', bg='#A9A9A9',  command = self.Logout)
        #puts the Button in the speicifed location on the window
        self.ButtonLogout.place(x=0,y = 0)

        #creates the button for Face recognition
        #button 1
        self.b1=Button(win, text='1. Face recognition', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9', command=self.Face_recognition)
        #puts the Button in the speicifed location on the window
        self.b1.place(x=150, y=150)

        #creates the button for button2
        #button 2
        self.b2=Button(win, text='2. Pull Faces', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9',command= self.PullFace)
        #puts the Button in the speicifed location on the window
        self.b2.place(x=350, y=150)

        #creates the button for button3
        #button 3
        self.b3=Button(win, text='3. Face Match', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9',command= self.FaceMatch)
        #puts the Button in the speicifed location on the window
        self.b3.place(x=150, y=175)

        #creates the button for button4
        #button 4
        self.b4=Button(win, text='4. Identify Faces', fg="black", highlightbackground = '#A9A9A9',bg='#A9A9A9',command = self.IdentifyFaces)
        #puts the Button in the speicifed location on the window
        self.b4.place(x=350, y=175)
        
        #creates the button for button5        
        #button 5
        self.b5=Button(win, text='5. Password Generator', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9',command=self.PasswordGenerator)
        #puts the Button in the speicifed location on the window
        self.b5.place(x=150, y=200)

        #creates the button for button6
        #button 6
        self.b6=Button(win, text='6. Find Faces', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9',command= self.FindFaces)
        #puts the Button in the speicifed location on the window
        self.b6.place(x=350, y=200)

        #creates the button for button7
        #button 7
        self.b7=Button(win, text='7. Password Checker', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9',command=self.PasswordChecker)
        #puts the Button in the speicifed location on the window
        self.b7.place(x=150, y=225)

        #creates the button for button8
        #button 8
        self.b8=Button(win, text='8. Notepad', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9',command= self.Notepad)
        #puts the Button in the speicifed location on the window
        self.b8.place(x=350, y=225)

        #creates the button for button9
        #button 9
        self.b9=Button(win, text='9. General Upload Images', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9',command=self.Upload_Image)
        #puts the Button in the speicifed location on the window
        self.b9.place(x=150, y=250)

        #creates the button for button10
        #button 10
        self.b10=Button(win, text='10. Login Upload Images', fg="black", highlightbackground= '#A9A9A9',bg='#A9A9A9',command=self.Admin_Upload_Image)
        #puts the Button in the speicifed location on the window
        self.b10.place(x=350, y=250)

        #used to handle window close event
        window.protocol("WM_DELETE_WINDOW",  self.Logout) 

    #if the logout button is pressed then this function would be called
    def Logout(self):
        #if x or the logout button is pressed then the question is asked if user presses ok then exit() is ran
        if messagebox.askokcancel("Quit", "Do you want to exit from the application?"):
            exit()
    
    #if the face recognition is pressed then FaceRecognition is imported and the function within FaceRecognition is ran
    def Face_recognition(self):
        import FaceRecognition
        FaceRecognition.Face_recogntion(self)

    #if the upload image is pressed then UploadImage is imported and the function within UploadImage is ran
    def Upload_Image(self):
        import UploadImage
        UploadImage.Output(self,window)

     #if the admin upload image is pressed then AdminUploadImage is imported and the function within AdminUploadImage is ran
    def Admin_Upload_Image(self):
        import AdminUploadImage
        AdminUploadImage.Output(self,window)

    #if Password Generator is pressed then PasswordGenerator is imported and the function within PasswordGenerator is ran
    def PasswordGenerator(self):
        import PasswordGen
        PasswordGen.Password(self,window)
    
    #if Password Checker is pressed then PasswordChecker is imported and the function within PasswordChecker is ran
    def PasswordChecker(self):
        import PasswordCheck
        PasswordCheck.Check(self,window)

    #if Face Match is pressed then FaceMatch is imported and the function within FaceMatch is ran
    def FaceMatch(self):
        import FaceMatch
        FaceMatch.Output(self,window)
    
    #if Pull Face is pressed then PullFace is imported and the function within PullFace is ran
    def PullFace(self):
        import PullFace
        PullFace.Output(self)

    #if Find Faces is pressed then FindFaces is imported and the function within FindFaces is ran
    def FindFaces(self):
        import FindFaces
        FindFaces.Output(self,window)

    #if Identify Faces is pressed then IdentifyFaces is imported and the function within IdentifyFaces is ran
    def IdentifyFaces(self):
        import IdentifyFaces
        IdentifyFaces.Output(self)

    #if NotePad is pressed then NotePad is imported and the function within NotePad is ran
    def Notepad(self):
        import Notepad
        Notepad.Output(self)


#intialise tk window
#create instance of tk
window=Tk()
#sets the frames title
window.title('Secure Face Recogniton App - Main Frame ')
mywin=MyWindow(window)
#sets the size of the frame
window.geometry("600x500+10+10")
#sets background colour of the frame
window.configure(bg='#A9A9A9')
#runs the tkinter event loop and listens for button events eg button clicks
window.mainloop()