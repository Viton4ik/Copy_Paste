# Подключим модуль для работы с буфером обмена
import pyperclip
# Подключим модуль для работы с системным временем
import time
#Add module for buttons searching
import keyboard

# import only datetime class
from datetime import datetime
from datetime import date

# Задаем переменную old и присваиваем ей пустую строку
old = ''
# find the current datetime
now = datetime.now()
current_date = now.date()
current_time = now.time()
# Начнем бесконечный цикл слежения за буфером обмена
while True:
    # Кладем в переменную s содержимое буфера обмена
    s = pyperclip.paste()
    # Define a "stop" button - 'esc'
    k = keyboard.is_pressed('esc')
    # Check if "stop" button pressed
    #if (k == True):
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
        # печатаем его (to check the copied info)
        print(s)
        # в переменную old записываем текущее пойманное значение
        # чтобы в следующий виток цикла не повторяться и не печатать то, что уже поймано
        old = s
    # В конце витка цикла делаем паузу в одну секунду, чтобы содержимое буфера обмена успело прогрузиться
    time.sleep(0.1)



