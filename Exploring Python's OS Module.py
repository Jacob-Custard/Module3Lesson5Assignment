# Task 1 Directory Inspector: Create a Python script that lists all files and subdirectories in a given
#directory. Your script should prompt the user for the directory path and then display the contents.

import os                                                                                                                             #importing the os module

def list_directory_contents(path):                                                                                                    #defining a function to list all the files and subdirectories in a directory
    try:                                                                                                                              #try block to handle errors
        for directory, subdirectories, files in os.walk(path):                                                                        #'for' loop to cycle through a directory using the os module 'walk' function
           
            for subdirectory in subdirectories:                                                                                       #'for' loop to cycle through the 'subdirectories'
                print(f"Subdirectory: {subdirectory}")                                                                                #'print' statement to print off the 'subdirectories' as they are looped through

            for file in files:                                                                                                        #'for' loop cycling through 'files'
                print(f"File: {file}")                                                                                                #'print' statement to print off the files as they are looped through

    except FileNotFoundError:                                                                                                         #'except' statement for file not found error
        print("File not found.")                                                                                                      #'print' statement telling the user the file couldnt be located

    except OSError:                                                                                                                   #'except' statement for the more general OSError error
        print("General error, look at an invalid path or permission issues to start with.")                                           #'print' statement telling the user a general error has occured and telling them to check the most common causes of this type of error

user_path = input("Please enter a directory path: ")                                                                                  #'input' statement to prompt the user to input the directory path they would like displayed
                                                                                                
list_directory_contents(user_path)                                                                                                    #calling the function with the user input



