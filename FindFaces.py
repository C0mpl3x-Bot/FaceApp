#Examples used from https://github.com/bradtraversy/face_recognition_examples
#Library sites used:
#https://docs.python.org/3/library/tkinter.html
#https://pypi.org/project/face-recognition/

#Imports necessary libraries
from tkinter import * 
from tkinter import filedialog
import face_recognition
from tkinter import messagebox

def Output(self,win):
    #error would occur if the user does not fully perfrom the function 
    #such as user does not select an image causing there to be an error but error does not break the application so try and except would fix this error,
    #error occurs as there is no file being selected for it to perfrom the function
    #since error does not break application code in except block just returns
    try:
        #allows user to select the file they want to use
        filename = filedialog.askopenfilename()
        
        #loads the file the user uploaded and saves it to UnknownImages
        UnkownImage = face_recognition.load_image_file(filename)


        #gets the face location in the image that the user uploaded and returns a list of tuples of found face loactions in css(top,right,bottom,left) order and saves it to the function FaceLocation
        FaceLocation = face_recognition.face_locations(UnkownImage)

        #intialise window for new pop up
        global pop
        pop = Toplevel(win)
        pop.title("Faces Found")
        pop.geometry("250x150")
        pop.config(bg="#A9A9A9")

        #global variables intialised
        global pop_label
        global pop_button
        
        #empty string which would be replaced with the results of the users input so the results can be displayed to the user
        msg = ''
        #checks if the number of faces equals to 1
        if(len(FaceLocation) == 1):
            #if there is 1 face in the image the result for msg would be the one below
            msg = f'There is {len(FaceLocation)} person in this image'
        else:
            #if there are more than 1 face in the image the result for msg would be the one below
            msg = f'There are {len(FaceLocation)} people in this image'

        #label with text that contains the number of faces the app was able to locate within the image the user uploaded
        pop_label = Label(pop, text= msg, bg ="#A9A9A9", fg= "black", font=("helvetica",12))
        pop_label.pack(pady=10)

        #used to handle pop up window close event
        pop.protocol("WM_DELETE_WINDOW", close_pop)
    except:
        return

#close_pop function which gives the user the warning before they close the pop up window.
def close_pop():
    #if x is pressed then the question is asked if user presses ok then pop.destroy is ran
    if messagebox.askokcancel("Quit", "Do you want to quit Find Faces?"):
        pop.destroy()  
