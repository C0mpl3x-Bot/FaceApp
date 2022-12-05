#Library sites used:
#https://docs.python.org/3/library/tkinter.html

#Imports necessary libraries
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
def Check(self,win):

    global pop
    #intialise popup window for password checker
    pop = Toplevel(win)
    pop.title("Password Check") 
    pop.geometry("700x600")        
    pop.config(bg="#A9A9A9")

    #intialise global variables
    global pop_label
    global pop_entryPassword
    global pop_button
    global pop_label2

    #create a label with text that is going to be placed on the pop up
    pop_label = Label(pop,text='Please Enter The Password You Want To Check Below', bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_label.pack(pady=10)

    #create a label1 with text that is going to be placed on the pop up
    pop_label2 = Label(pop,text='The Checker Would Determine How Good Your Password Is \n \n Horrible Password: Length -> 0 Or More, Symbols = 0 , Digits = 0 \n \n Poor Password: Length -> 4 Or More, Symbols -> 1 Or More , Digits -> 1 Or More \n \n Ok Password: Length -> 8 Or More, Symbols -> 2 Or More , Digits -> 2 Or More \n \n Good Password: Length -> 12 Or More, Symbols -> 3 Or More , Digits -> 3 Or More, Both Uppercase And Lowercase Letters Used \n \n Excellent Password: Length -> 16 Or More, Symbols -> 4 Or More , Digits -> 4 Or More, Both Uppercase And Lowercase Letters Used \n \n If None Of These Are Met Then The Password Would Be Determined As Invalid', bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_label2.pack(pady=10)

    #create input box to allow user to input password they want to check
    pop_entryPassword = Entry(pop)
    pop_entryPassword.pack(pady=10)

    #create button so user can submit all the data they inputted and have the password to be checked
    pop_button = Button(pop, text ="Check", fg="black", highlightbackground= '#A9A9A9', bg='#A9A9A9',  command = Checker)
    pop_button.pack(pady=10)

    #used to handle window close event
    pop.protocol("WM_DELETE_WINDOW", close_pop)


def Checker():
    #minmise the first pop up
    pop.withdraw()

    #all possible inputs in a password 
    stringDigits = "0123456789"
    stringSymbols = "!@£€#$%^&()_-+=[]{};:|<>/?~"
    stringCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    upperCaseCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerCaseCharacters = "abcdefghijklmnopqrstuvwxyz"

    #get user input
    input_length=pop_entryPassword.get()
    Output  = ''
    symbolCount = 0 
    digitCount = 0
    UpperCaseFound = False
    LowerCaseFound = False

    #loop up to the length of the input
    for j in range(int(len(input_length))):
        #k is equal to each character in the inputted password 
        k = input_length[j:j+1]  

        #check if k is a symbol, digit,upper case character or lower case character
        if k in stringSymbols:
            #increment symbol count by 1
            symbolCount += 1
        if  k in stringDigits:
            #increment digit count by 1
            digitCount += 1
        if k in upperCaseCharacters:
            #return true for upper case
            UpperCaseFound = True
        if k in lowerCaseCharacters:
            #return true for lower case
            LowerCaseFound = True    

    #compare the results to the systems criteria and update the output variable so it returns the criteria the password met
    if(len(input_length) >= 16 and symbolCount >= 4 and digitCount >= 4 and UpperCaseFound == True and LowerCaseFound == True):
        Output = "Your Password Is Excellent And Your password is " + input_length
    elif(len(input_length) >= 12 and symbolCount >= 3 and digitCount >= 3 and UpperCaseFound == True and LowerCaseFound == True): 
        Output = "Your Password Is Good and Your password is " + input_length
    elif(len(input_length) >=8 and symbolCount >=2 and digitCount >=2):    
        Output = "Your Password Is Ok and Your password is " + input_length   
    elif(len(input_length) >= 4 and symbolCount >= 1 and digitCount >= 1): 
        Output = "Your Password Is Poor and Your password is " + input_length
    elif(len(input_length) > 0 and symbolCount == 0 and digitCount == 0):
        Output = "Your Password Is Horrible and Your password is " + input_length
    else:
        Output = "Your Password Does Not Meet Any Of Our Requirements. Hence Your Password Is Invalid"   
  
    #initalise new popup window
    global pop2
    pop2 = Toplevel()
    pop2.title("Open File Error Output") 
    pop2.geometry("500x300")        
    pop2.config(bg="#A9A9A9")

    global pop_output_label
    global pop_copy_button

    #label that has output as the text so it would ouput the users inputted password strength
    pop_output_label = Label(pop2,text=Output, bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_output_label.pack(pady=10)

    #used to handle window close event
    pop2.protocol("WM_DELETE_WINDOW", close_pop)

#close function which gives the user the warning before they close the pop up window.
def close_pop():
    #if x is pressed then the question is asked if user presses ok then destroy for both pop ups are is ran
    if messagebox.askokcancel("Quit", "Do you want to quit Password Checker?"):
        #if user did not use the function to check a password then pop2 is not initalised which caused there to be a warning in the console
        #warning did not break the code so by using a try and except block it stops the unncessary error from poping up
        #since error does not break application code in except block just returns
        try:
            pop.destroy()    
            pop2.destroy()  
        except:
            return