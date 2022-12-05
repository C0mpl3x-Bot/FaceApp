#Library sites used:
#https://docs.python.org/3/library/tkinter.html
#https://docs.python.org/3/library/shutil.html

#Imports necessary libraries
from tkinter import *
from tkinter import filedialog
import shutil
from tkinter import messagebox

def Output(self,win):
    #error would occur if the user does not fully perfrom the function 
    #such as user does not select an image causing there to be an error but error does not break the application so try and catch would fix this error,
    #error occurs as there is no file being selected for it to perfrom the function
    #since error does not break application code in except block just returns
    try:
        #let user select a file on their device.
        filename = filedialog.askopenfilename()
        #save filename to name
        name = filename
        #get the last part of the filename so the part after the . eg the png/jpg
        split_string = name.split(".", -1)
        #set name to the extension of the filename the user selected
        name = split_string[1]

        #initalise global variables
        global pop_label
        global pop

        #intialise pop window
        pop = Toplevel(win)
        #sets the pop frames title
        pop.title("Upload Image Results") 
        #set the pop frame size
        pop.geometry("450x250")        
        #sets background colour of the pop frame
        pop.config(bg="#A9A9A9")

        #initalise message with invalid output
        message = f"The file you have selected has not been moved into our system." "\n" " Your File needs to be end with .jpg or .png"

        #conver name to lowercase then check if the extensions are either png/jpg
        if(name.lower()  == "png" or name.lower() == "jpg"):
            #set message to new output.(Successful output)
            message = "The file you have selected has been moved into our general system"
            #moves the file that the user selected to the img/known folder
            shutil.move(filename, './img/known')
            #create label with new msg and set its background colour, foreground colour, font and size
            pop_label = Label(pop,text=message, bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
            pop_label.pack(pady=10)
            
            #used to handle pop up window close event
            pop.protocol("WM_DELETE_WINDOW", close_pop)

        #if the if statement is not true then it will run the code in the else statement
        else:
            #creates label with the unsuccessful message and set its background colour, foreground colour, font and size
            pop_label = Label(pop,text=message, bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
            pop_label.pack(pady=10)

            #used to handle pop up window close event
            pop.protocol("WM_DELETE_WINDOW", close_pop)
    except:
        return

#close function which gives the user the warning before they close the pop up window.
def close_pop():
    #if x button is pressed then the question is asked if user presses ok then pop.destroy() is ran
    if messagebox.askokcancel("Quit", "Do you want to quit General Upload Images?"):
        pop.destroy() 