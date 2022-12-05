#Library sites used:
#https://docs.python.org/3/library/tkinter.html
#https://docs.python.org/3/library/random.html

#Imports necessary libraries
from tkinter import *
from tkinter import messagebox
import random

def Password(self,win):

    global pop
    global pop2
    #intialise popup window for password generator
    pop = Toplevel(win)
    pop.title("Password Gen") 
    pop.geometry("400x600")        
    pop.config(bg="#A9A9A9")

    #intialise global variables
    global pop_label
    global pop_label1
    global pop_label2
    global pop_label3
    global pop_entryLength
    global pop_entryDigits
    global pop_entrySymbols
    global pop_button


    #create a label with text that is going to be placed on the pop up
    pop_label = Label(pop,text='Please Follow The Following Steps To generate A Random Password', bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_label.pack(pady=10)

    #create a label with text that is going to be placed on the pop up
    pop_label1 = Label(pop,text='Please Enter The Length You Want The Password To Be:', bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_label1.pack(pady=10)

    #create input/spinbox box to allow user to input length data
    pop_entryLength = Spinbox(pop,from_= 0,to=100)
    pop_entryLength.pack(pady=10)

    #create a label1 with text that is going to be placed on the pop up
    pop_label2 = Label(pop,text='Please Enter The Number Of Symbols You Want The Password To Contain:', bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_label2.pack(pady=15)

    #create input box to allow user to input symbol data
    pop_entrySymbols= Spinbox(pop,from_= 0,to=100)
    pop_entrySymbols.pack(pady=10)

    #create a label1 with text that is going to be placed on the pop up
    pop_label3 = Label(pop,text='Please Enter The Number Of Digits You Want The Password To Contain:', bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_label3.pack(pady=15)

    #create input box to allow user to input digit data
    pop_entryDigits= Spinbox(pop,from_= 0,to=100)
    pop_entryDigits.pack(pady=10)

    #create button so user can submit all the data they inputted and generate a password
    pop_button = Button(pop, text ="Generate", fg="black", highlightbackground= '#A9A9A9', bg='#A9A9A9',  command = Generate)
    pop_button.pack(pady=10)
    
    #used to handle window close event
    pop.protocol("WM_DELETE_WINDOW", close_pop)


def Generate():

    #intialise window for new pop up
    global pop2
    pop2 = Toplevel()
    pop2.title("Password Gen ouput") 
    pop2.geometry("500x300")        
    pop2.config(bg="#A9A9A9")

    global pop_output_label
    global pop_copy_button

    #used to handle window close event
    pop2.protocol("WM_DELETE_WINDOW", close_pop)

    #variable of all possible digits, symbols and characters intialised
    stringDigits = "0123456789"
    stringSymbols = "!@£€#$%^&()_-+=[]{};:|<>/?~"
    stringCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    msg = ''

    try:
        #get user input and save them according to their variable
        input_length=pop_entryLength.get()
        symbol = pop_entrySymbols.get()
        digits = pop_entryDigits.get()
        RequirementPassword  = ''
        #checks if the sum of digits length and symbols length is greater than password length
        if((int(digits) + int(symbol)) > int(input_length)):
            #checks if length of digits is greater than password length
            if(int(digits)>int(input_length)):
                #change the output of msg
                msg = 'Inputted number for digits is too large make sure it is less than input number for length.'"\n"' Please change your digits input'
            #checks if length of symbol is greater than password length 
            elif(int(symbol) > int(input_length)):
                #change the output of msg
                msg = 'Inputted number for symbols is too large make sure it is less than input number for length.'"\n" 'Please change your symbols input'
            #if nither are true then runs code in else statement
            else:
                #change the output of msg
                msg = 'The sum of the numbers inputted for digits and symbols are larger than the input number for length.' "\n" 'Please change your inputted values'
        #if the if statement is false then run code in else statement
        else:
            #calculate string length for number of characters
            StringLength = int(input_length) - (int(digits)+ (int(symbol)))

            #for loop that loops up to user input for digits
            for i in range(int(digits)):
                #randomly selects index from the variable stringDigits
                digit_index = (random.randrange(0, len(stringDigits)))
                #gets the ditgit from that index and adds it to requirement password
                RequirementPassword += stringDigits[digit_index:digit_index+1]

            #for loop that loops up to user input for symbol
            for k in range(int(symbol)):
                #randomly selects index from the variable stringSymbol
                symbol_index = (random.randrange(0, len(stringSymbols)))
                #gets the symbol from that index and adds it to requirement password
                RequirementPassword += stringSymbols[symbol_index:symbol_index+1]

            #for loop that loops up to String legnth value
            for j in range(int(StringLength)):
                #randomly selects index from the variable stringCharacters
                character_index = (random.randrange(0, len(stringCharacters)))   
                #gets the character from that index and adds it to requirement password
                RequirementPassword += stringCharacters[character_index:character_index+1]

            #new empty string created
            global RandomPassword
            RandomPassword = ''
            #for loop that loops up to input length value
            for l in range(int(input_length)):
                #selects random index from requirement password
                length_index = (random.randrange(0, len(RequirementPassword)))  
                #gets the data at that index and saves it to random password 
                RandomPassword +=  RequirementPassword[length_index:length_index+1]
                #remove the data that you got from requirement password so it does not repeat 
                RequirementPassword = RequirementPassword[0:length_index] + RequirementPassword[length_index+1:len(RequirementPassword)]


            #label with text that contains the randomly generated password using user input is displayed on the new pop up
            pop_output_label = Label(pop2,text=' Generated Password For The Input Given Is: ' + RandomPassword + ' \n To Copy The Password Press The Button Below', bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
            pop_output_label.pack(pady=10)

            #button to allow user to copy the random password generated to their clipboard
            pop_copy_button = Button(pop2, text = "Copy To Clipboard", fg="black", highlightbackground= '#A9A9A9', bg='#A9A9A9',  command = copy)
            pop_copy_button.pack(pady=10)

    #if something other than a number is inputted into the box then a pop up which states the user needs to input a valid number is displayed
    except ValueError:
        msg = 'Please Input A Valid Number'
    #label with text that contains the randomly generated password on the new pop up
    pop_output_label = Label(pop2,text=msg, bg = "#A9A9A9" , fg = "black", font=("helvetica",12))
    pop_output_label.pack(pady=10)
        

#copy to clipboard function does not pop up as it gets destoyed instantly but saves the password to clipboard  
def copy():
    global pop3
    pop3 = Toplevel()
    pop3.title("Copied To ClipBoard") 
    pop3.geometry("500x300")        
    pop3.config(bg="#A9A9A9")
    pop3.withdraw()
    #clear clipboard
    pop3.clipboard_clear()
    #save random password to users clipboard 
    pop3.clipboard_append(RandomPassword)
    # now it stays on the clipboard after the window is closed
    pop3.update()
    #close pop3
    pop3.destroy()
    
#close function which gives the user the warning before they close the pop up window.
def close_pop():
    #if x is pressed then the question is asked if user presses ok then destroy for both pop ups are is ran
    if messagebox.askokcancel("Quit", "Do you want to quit Password Generator?"):
        #if user did not use the function and generate a password then pop2 is not initalised which caused there to be a warning in the console
        #warning did not break the code so by using a try and except block it stops the unncessary error from poping up
        #since error does not break application code in except block just returns
        try:
            pop.destroy()    
            pop2.destroy()  
        except:
            return
        
