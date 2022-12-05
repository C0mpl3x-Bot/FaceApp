#Library sites used:
#https://docs.python.org/3/library/tkinter.html
#https://docs.python.org/3/library/time.html

#Imports necessary libraries
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter import messagebox
import time

#main function that would be ran from UI to allow the notepad function to run properly
def Output(self):
    #intialising global variables
    global window
    global TextBox
    global MenuBar
    global FileMenu
    global EditMenu
    global FileDirectory
    global MuteSaveNotification

    #intialise window for notepad function
    window = Tk()
    window.title("Untitled")
    window.geometry("500x300")

    #Creating MenuBar
    MenuBar = Menu(window)
    window.config(menu=MenuBar)

    #setting some variables to false and none to help with notepad state so the application can perform certain function differently in different states
    Output.FileOpen = False
    Output.MuteSaveNotification = None
    Output.FileDirectory = None

    #TextBox intialising 
    #wrap = word allows the sentences to break into new lines and not go off the textbox window so it fits the text in the width of the text document
    #undo = true allows user to perfrom undo and redo functions on the notepad
    TextBox = Text(window,wrap=WORD,undo=True)
    TextBox.pack()

    #responsiveness by doing 0,weight =1 it allws all extra space to go to row zero and coloumn zero allowing the text editor to be responsive
    window.grid_rowconfigure(0, weight = 1)
    window.grid_columnconfigure(0,weight=1)
    #causes the textbox to fill the entire frame if the frame is made larger or smaller 
    #this is because the N+E+W+S allows the textbox to stick to every side which would be NE,NW,SE and SW making the function responsive
    TextBox.grid(sticky=N+E+W+S)

    #all the functions found within the menubar are setup as lambda for keybidings to be setup 
    #creating a menu item
    FileMenu = Menu(MenuBar)
    #With the menu you use cascade to add the functions to the application instead pack
    #Creating File Menu
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #adds new file to the menubar file section
    FileMenu.add_command(label="New - ⌘N",command=lambda: NewFile(None))
    #adds save to the menubar file section
    FileMenu.add_command(label="Save - ⌘S",command= lambda: SaveFile(None))
    #adds save as to the menubar file section
    FileMenu.add_command(label="Save As - ⌘L",command = lambda: SaveAsFile(None))
    #adds open file to the menubar file section
    FileMenu.add_command(label="Open - ⌘O",command=lambda:OpenFile(None))

    #adds a line between the functions above and the functions below in File Menu causing them to be separated
    FileMenu.add_separator()
    #adds MoveFile file to the menubar file section this does not require a keybind
    FileMenu.add_command(label="Move File Into System",command=MoveFile)
    #adds Mute Save Notification to the menubar file section this does not require a keybind
    FileMenu.add_command(label= "Mute Save Notification",command=MuteNotification)
    #adds Exit to the menubar file section this does not require a keybind
    FileMenu.add_command(label="Exit",command=close_window)

    #Creating an Edit Menu
    EditMenu = Menu(MenuBar)
    #With the menu you use cascade to add the functions to the application instead pack
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    #adds Undo to the menubar edit section
    EditMenu.add_command(label= "Undo - ⌘Z",command=lambda:UndoFile(None))
    #adds redo to the menubar edit section
    EditMenu.add_command(label = "Redo - ⌘Y",command=lambda:RedoFile(None))

    #adds a line between the functions above and the functions below in Edit Menu causing them to be separated
    EditMenu.add_separator()
    #adds cut to the menubar edit section 
    EditMenu.add_command(label= "Cut - ⌘X",command=lambda:CutFile(None))
    #adds copy to the menubar edit section
    EditMenu.add_command(label= "Copy - ⌘C",command=lambda:CopyFile(None))
    #adds paste to the menubar edit section
    EditMenu.add_command(label= "Paste - ⌘V",command=lambda:PasteFile(None))

    #used to handle window close event
    window.protocol("WM_DELETE_WINDOW", close_window)


    #Keybinding function would be run and it checks if a speicifc keybind is used within the notepad frame 
    #and would run the function for that specific keybind preseed
    keybinds(None)
    
    window.mainloop()


#keybinds for important notepad functions (cut,copy,paste have their own keybinds built into them via tkinter event_generate)
def keybinds(event):
    #key binding for NewFile
    for New in ['<Command-Key-N>','<Command-Key-n>']:
        #if any of the key binds above is pressed then it would run NewFile function
        TextBox.bind(New,NewFile)
    #key binding for SaveFile
    for Save in ['<Command-Key-S>','<Command-Key-s>']:
        #if any of the key binds above is pressed then it would run SaveFile function
        TextBox.bind(Save,SaveFile)
    #key binding for Save As 
    for SaveAs in ['<Command-Key-L>','<Command-Key-l>']:
        #if any of the key binds above is pressed then it would run SaveAsFile function
        TextBox.bind(SaveAs,SaveAsFile)
    #key binding for OpenFile
    for openfiles in ['<Command-Key-O>','<Command-Key-o>']:
        #if any of the key binds above is pressed then it would run OpenFile function
        TextBox.bind(openfiles,OpenFile)
    #key binding for undo
    for undo in ['<Command-Key-Z>','<Command-Key-z>']:
        #if any of the key binds above is pressed then it would run UndoFile function
        TextBox.bind(undo,UndoFile)
    #key binding for redo
    for redo in ['<Command-Key-Y>','<Command-Key-y>']:
        #if any of the key binds above is pressed then it would run RedoFile function
        TextBox.bind(redo,RedoFile)
    

#close function which gives the user the warning before they close the window.  
def close_window():
    #if x is pressed then the question is asked if user presses ok then window.destroy() is ran
    if messagebox.askokcancel("Quit",  "Do you want to quit the notepad function?"):
        window.destroy()    

#Create a new file by deleting all the text within the TextBox
def NewFile(event):
    #set the window name to the filename and the mute status if mute was never pressed then the title would not contain the mute status
    if(Output.MuteSaveNotification == None):
        window.title("Untitled")
    elif(Output.MuteSaveNotification == True):
        window.title("Untitled" + " - Save Notification Muted")
    elif(Output.MuteSaveNotification == False):
        window.title("Untitled" + " - Save Notification Unmuted")
    #set file open to false
    Output.FileOpen = False
    #set file directory to none
    Output.FileDirectory = None
    #delete everything within the textbox from the begining till the end
    TextBox.delete('0.0','end')

#allow user to open a specific type of text file cannot open any file using this function
def OpenFile(event):
    #if user attempts to open a file and does not select a file split string would have an error as there is no string to split 
    #this does not break the application so by using try and except it stops the error from coming up in the console 
    #and the block of code would function as intended to if the user selects a file to open
    #since error does not break application in except block just return
    try:
        #let user select a file on their device.
        File = filedialog.askopenfilename(initialdir='UserFiles')
        #save File to fileExtension
        FileExtension = File
        #get the last part of the filename so the part after the . eg the png/jpg
        split_string = FileExtension.split(".", -1)
        #set name to the extension of the filename the user selected
        FileExtension = split_string[1]
        #convert FileExtension to lowercase then check if the extensions are either txt/py/java/cs
        if(FileExtension.lower() == "txt" or FileExtension.lower() == "py" or FileExtension.lower() == "java" or FileExtension.lower() == "cs"):

            #set file directory to the directory of the file the user selected
            Output.FileDirectory = File
            #since a file has been opened by the user set FileOpen to True
            Output.FileOpen = True

            #delete everything in the textbox
            TextBox.delete("1.0",'end')

            #save filename to UserSelectedFilename
            UserSelectedFilename = File
            #gets the file name and split it from the other part 
            split_string =  UserSelectedFilename.split("/", 6)
            #sets the filename back to UserSelectedFilename without the useless text
            UserSelectedFilename = split_string[-1]

            #set the window name to the filename and mute status
            if(Output.MuteSaveNotification == None):
                window.title(UserSelectedFilename)
            elif(Output.MuteSaveNotification == True):
                window.title(UserSelectedFilename + " - Save Notification Muted")
            elif(Output.MuteSaveNotification == False):
                window.title(UserSelectedFilename + " - Save Notification Unmuted")

            #open the file
            text_file = open(File ,'r')

            #write the text from the file to the textbox
            TextBox.insert(END,text_file.read())

            #close the file
            text_file.close()
        else:
            #set message to the error text
            Message = 'Please Input A Text File which is one of the following formats \n txt or py or java or cs'
            #call NotePadOutputFrame with the message as the parameter
            NotePadOutputFrame(Message)
    except:
        return

#Allows user to select a specific type of file to be moved into the folder within the system which stores the files
#if movefile is pressed MoveFileNotePad is imported and then the function within it is ran
def MoveFile():
    import MoveFileNotePad
    MoveFileNotePad.Output(window)

#This function would allow user to mute and unmute the save pop up notifications 
def MuteNotification():
    #check if the MuteSaveNotification is either none or false
    if(Output.MuteSaveNotification == False or Output.MuteSaveNotification == None):
        #set MuteSaveNotification to true
        Output.MuteSaveNotification = True;
        
        #check if a file has been opened by the user by checking if FileOpen is true
        if(Output.FileOpen == True):
            #save filename to UserSelectedFilename
            UserSelectedFilename = Output.FileDirectory
            #gets the file name and split it from the other part 
            split_string =  UserSelectedFilename.split("/", 6)
            #sets the filename back to UserSelectedFilename without the useless text
            UserSelectedFilename = split_string[-1]
            #set title to the file name with the save notification status
            Title = str(UserSelectedFilename) + " - Save Notification Muted"
        #checks if no file has been opened by the user by checking if FileOpen is false
        elif(Output.FileOpen == False):
            #set title to Untitlited which is default with the save notification status
            Title = "Untitled" + " - Save Notification Muted"
        #set the window title to the new title
        window.title(Title)
    #check if MuteSaveNotification is true
    elif(Output.MuteSaveNotification == True):
        #set MuteSaveNotification to false
        Output.MuteSaveNotification = False

        #check if a file has been opened by the user by checking if FileOpen is true
        if(Output.FileOpen == True):
            #save filename to UserSelectedFilename
            UserSelectedFilename = Output.FileDirectory
            #gets the file name and split it from the other part 
            split_string =  UserSelectedFilename.split("/", 6)
            #sets the filename back to UserSelectedFilename without the useless text
            UserSelectedFilename = split_string[-1]
            #set title to the file name with the save notification status
            Title = str(UserSelectedFilename) + " - Save Notification Unmuted"
        #checks if no file has been opened by the user by checking if FileOpen is false
        elif(Output.FileOpen == False):
            #set title to Untitlited which is default with the save notification status
            Title = "Untitled" + " - Save Notification Unmuted"
        #set the window title to the new title
        window.title(Title)


#allows user to update the exisiting file they are working on but if it is a file is not saved then it would ask the user to save as the file. 
def SaveFile(event):
    #try and except implemented because if user wanted to save and cancelled the save then an error would pop in console so to stop the uncessary error use try and except
    #since error does not break application in except block just return
    try:
        #check if a file has not been opened by checking if FileOpen is fasle
        if(Output.FileOpen == False):
            #lets user save the file in the usersfiles folder with the defaultextension of txt
            File = filedialog.asksaveasfilename(initialdir="UserFiles",defaultextension=".txt")
            #opens the file
            text_file  = open(File,'w')
            #writes the changes to the file
            text_file.write(TextBox.get('0.0','end'))
            #closes the file
            text_file.close
            #save filename to UserSelectedFilename
            UserSelectedFilename = File
            #gets the file name and split it from the other part 
            split_string =  UserSelectedFilename.split("/", 6)
            #sets the filename back to UserSelectedFilename without the useless text
            UserSelectedFilename = split_string[-1]

            #sets title of the notepad to be the UserSelectedFilename
            #set the window name to the filename with the save mute status
            if(Output.MuteSaveNotification == None):
                window.title(UserSelectedFilename)
            elif(Output.MuteSaveNotification == True):
                window.title(UserSelectedFilename + " - Save Notification Muted")
            elif(Output.MuteSaveNotification == False):
                window.title(UserSelectedFilename + " - Save Notification Unmuted")

            #gets the time and date the user saved the file
            date = time.strftime("%a, %d %b %Y %H:%M:%S")
            #Changes the output of message for the specific situation
            Message = 'Your file ' + str(UserSelectedFilename) + ' has been successfully saved in our system on \n' + str(date)
            #calls the NotePadOutputFrame function with message as its parameter
            NotePadOutputFrame(Message)
            #sets fileOpen to true as the saved file is now open 
            Output.FileOpen = True
            #sets the fileDriectory to the saved files directory that is now open 
            Output.FileDirectory = File

        #checks if a file has been opened by checking if File opne is true
        elif(Output.FileOpen == True):
            #if file has been opened then it would open that specific file
            text_file = open(Output.FileDirectory,'w')
            #writes the changes to the file
            text_file.write(TextBox.get('0.0','end'))
            #closes the file
            text_file.close
            #check if the MuteSaveNotification is either none or false
            if(Output.MuteSaveNotification == False or Output.MuteSaveNotification == None):
                #save filename to UserSelectedFilename
                UserSelectedFilename = Output.FileDirectory
                #gets the file name and split it from the other part 
                split_string =  UserSelectedFilename.split("/", 6)
                #sets the filename back to UserSelectedFilename without the useless text
                UserSelectedFilename = split_string[-1]
                
                #sets title of the notepad to be the UserSelectedFilename
                #set the window name to the filename with the save mute status
                if(Output.MuteSaveNotification == None):
                    window.title(UserSelectedFilename)
                elif(Output.MuteSaveNotification == True):
                    window.title(UserSelectedFilename + " - Save Notification Muted")
                elif(Output.MuteSaveNotification == False):
                    window.title(UserSelectedFilename + " - Save Notification Unmuted")
                  
                #gets the time and date the user saved the file 
                date = time.strftime("%a, %d %b %Y %H:%M:%S")
                #Changes the output of message for the specific situation
                Message = 'Your file ' + str(UserSelectedFilename) + ' has been successfully updated on \n' + str(date)
                #calls the NotePadOutputFrame function with message as its parameter
                NotePadOutputFrame(Message)
    except:
        return
    
def SaveAsFile(event):
    #try and except implemented because if user wanted to save and cancelled the save then an error would pop in console so to stop the uncessary error use try and except
    #since error does not break application in except block just return
    try:
        #lets user save the file in the usersfiles folder with the defaultextension of txt
        File = filedialog.asksaveasfilename(initialdir="UserFiles",defaultextension=".txt")
        #opens the file
        text_file  = open(File,'w')
        #writes the changes to the file
        text_file.write(TextBox.get('0.0','end'))
        #closes the file
        text_file.close
        #save filename to UserSelectedFilename
        UserSelectedFilename = File
        #gets the file name and split it from the other part 
        split_string =  UserSelectedFilename.split("/", 6)
        #sets the filename back to UserSelectedFilename without the useless text
        UserSelectedFilename = split_string[-1]

        #sets title of the notepad to be the UserSelectedFilename
        #set the window name to the filename and mute status
        if(Output.MuteSaveNotification == None):
            window.title(UserSelectedFilename)
        elif(Output.MuteSaveNotification == True):
            window.title(UserSelectedFilename + " - Save Notification Muted")
        elif(Output.MuteSaveNotification == False):
            window.title(UserSelectedFilename + " - Save Notification Unmuted")

        #gets the time and date the user saved the file 
        date = time.strftime("%a, %d %b %Y %H:%M:%S")
        #Changes the output of message for the specific situation
        Message = 'Your file ' + str(UserSelectedFilename) + ' has been successfully updated on \n' + str(date)
        #calls the NotePadOutputFrame function with message as its parameter
        NotePadOutputFrame(Message)
        #sets fileOpen to true as the saved file is now open 
        Output.FileOpen = True
        #sets the fileDriectory to the saved files directory that is now open 
        Output.FileDirectory = File
    except:
        return

#function would be run if undo keybind is pressed or undo button in menu bar is pressed
def UndoFile(event):
    #if user tried to undo nothing then a warning would pop up in the console the try and except stops the warning from popping up stopping 
    #the console from getting clustered
    #since error does not break application in except block just return
    try:
        TextBox.edit_undo()
    except:
        return

#function would be run if redo keybind is pressed or redo button in menu bar is pressed
def RedoFile(event):
    #if user tried to redo nothing then a warning would pop up in the console the try and except stops the warning from popping up stopping 
    #the console from getting clustered
    #since error does not break application in except block just return
    try:
        TextBox.edit_redo()
    except:
        return

#event_generate generates an event sequence and allows certain functions to be performed such as copy,cut,paste hence does not require manual keybinding

#function would be run if cut keybind is pressed or cut button in menu bar is pressed
def CutFile(event):
    #Move the currently selected widget contents to the clipboard.
    TextBox.event_generate("<<Cut>>")

#function would be run if copy keybind is pressed or copy button in menu bar is pressed
def CopyFile(event):
    #Copy the currently selected widget contents to the clipboard.
    TextBox.event_generate("<<Copy>>")

#function would be run if paste keybind is pressed or paste button in menu bar is pressed
def PasteFile(event):
    #Replace the currently selected widget contents with the contents of the clipboard.
    TextBox.event_generate("<<Paste>>")

#function would be run if NotePadOutPutFrame is called with a string message
def NotePadOutputFrame(Message):
    #intialise new pop up 
    global pop
    pop = Toplevel(window)
    pop.title("Notepad Output") 
    pop.geometry("600x300")        
    pop.config(bg="#A9A9A9")
    
    #create label with new messgae and set its background colour, foreground colour, font and size
    pop_output_label = Label(pop,text=Message, bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_output_label.pack(pady=10)
