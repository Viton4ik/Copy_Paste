<<<<<<< HEAD
# Code to download "Ctrl-C" data to a file "copy_paste_buffer.txt" in a directory we need
# Victor Vetoshkin
# August 2022

# Connect the module for working with the clipboard
import pyperclip
# Connect the module to work with system time
import time
#Add module for buttons searching
import keyboard

# import only datetime class
from datetime import datetime
from datetime import date
import os
# Returns the path to the current working folder
pth = os.getcwd()
print(pth)

## Kindly ask to put a path to the directory - what we wanna save files in
#pth = input('Insert a directory:')
pth = 'C:\\Program Files'
#d=input()

## Go to the directory that has been written down
print(os.chdir(pth))
# create an empty folder there, but remember another 'mkdir' with the same name will set 'FileExistsError',
# to avoid this:
if not os.path.isdir("Copy_Paste_log"):
     os.mkdir("Copy_Paste_log")
pth = 'C:\\Program Files\Copy_Paste_log'
print(os.chdir(pth))

# Set a variable 'old' and put an empty string there
old = ''
# find the current datetime
now = datetime.now()
current_date = now.date()
current_time = now.time()
# Watch the buffer
while True:
    # Put a data in our buffer
    s = pyperclip.paste()
    # Define a "stop" button - 'esc'
    k = keyboard.is_pressed('esc')
    # Check if "stop" button pressed
    if k:
        # Open or create a new file in this directory.
        file = open('copy_paste_buffer.txt', 'a', encoding='UTF-8')
        #put the date info in our file.
        file.write(str(current_date) + '  ' +  str(current_time) + '\n')
        #Write a message about stopped proccess
        file.write('Recording has been stopped by user\n')
        #Add a spacebar
        file.write('  \n')
        #Close the file
        file.close()
        #Print a message here to be sure
        print('You Pressed A Key!')
        #clean the buffer up
        pyperclip.copy(' ')
        #Stop the proccess
        break
    #Check the buffer
    if(s != old):
        #Open or create a new file in this directory.
        file = open('copy_paste_buffer.txt', 'a', encoding='UTF-8')
        #ut the date info in our file.
        file.write(str(current_date) + '  ' +  str(current_time) + '\n')
        #put copied info from the buffer in our file.
        file.write('  ' + str(s) + '\n')
        #create a spacebar and slide to the next string
        file.write('  \n')
        file.close()
        #to check the copied info - if needed
        #print(s)
        # put the data in old to avoid printing the previous info
        old = s
    # delay
    time.sleep(0.1)
=======
# Code to download "Ctrl-C" data to a file "copy_paste_buffer.txt" in a directory we need
# Victor Vetoshkin
# August 2022

# Connect the module for working with the clipboard
import pyperclip
# Connect the module to work with system time
import time
#Add module for buttons searching
import keyboard

# import only datetime class
from datetime import datetime
from datetime import date
import os
# Returns the path to the current working folder
pth = os.getcwd()
print(pth)

## Kindly ask to put a path to the directory - what we wanna save files in
#pth = input('Insert a directory:')
pth = 'C:\\Program Files'
#d=input()

## Go to the directory that has been written down
print(os.chdir(pth))
# create an empty folder there, but remember another 'mkdir' with the same name will set 'FileExistsError',
# to avoid this:
if not os.path.isdir("Copy_Paste_log"):
     os.mkdir("Copy_Paste_log")
pth = 'C:\\Program Files\Copy_Paste_log'
print(os.chdir(pth))

# Set a variable 'old' and put an empty string there
old = ''
# find the current datetime
now = datetime.now()
current_date = now.date()
current_time = now.time()
# Watch the buffer
while True:
    # Put a data in our buffer
    s = pyperclip.paste()
    # Define a "stop" button - 'esc'
    k = keyboard.is_pressed('esc')
    # Check if "stop" button pressed
    if k:
        # Open or create a new file in this directory.
        file = open('copy_paste_buffer.txt', 'a', encoding='UTF-8')
        #put the date info in our file.
        file.write(str(current_date) + '  ' +  str(current_time) + '\n')
        #Write a message about stopped proccess
        file.write('Recording has been stopped by user\n')
        #Add a spacebar
        file.write('  \n')
        #Close the file
        file.close()
        #Print a message here to be sure
        print('You Pressed A Key!')
        #clean the buffer up
        pyperclip.copy(' ')
        #Stop the proccess
        break
    #Check the buffer
    if(s != old):
        #Open or create a new file in this directory.
        file = open('copy_paste_buffer.txt', 'a', encoding='UTF-8')
        #ut the date info in our file.
        file.write(str(current_date) + '  ' +  str(current_time) + '\n')
        #put copied info from the buffer in our file.
        file.write('  ' + str(s) + '\n')
        #create a spacebar and slide to the next string
        file.write('  \n')
        file.close()
        #to check the copied info - if needed
        #print(s)
        # put the data in old to avoid printing the previous info
        old = s
    # delay
    time.sleep(0.1)
>>>>>>> 1449daad103cafbb57ca8bc63ed96f038b867336
