from vosk import Model, KaldiRecognizer
import pyaudio as pa
import sys, signal
import os

model = Model(r'/Users/anandsinha/Documents/TATA-Final-Clean/model-small-en-in-0.4') # model path here and r is for windows compatibility of /. instead of //

recognizer = KaldiRecognizer(model, 16000)

mic = pa.PyAudio()
stream = mic.open(format=pa.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        if 'start all programs' in text:
            print(text[14:-3])
            print('Starting all Applications...')
            ## ADD THE PROGRAM DEF TO STOP LIKE IN EXAMPLE.
            #EXAMPLE - os.system(r'start cmd /k "python C:\Users\******\********\Automated_Switcher\task_1.py"' )
        
        elif 'start human in range' in text:
            print(text[14:-3])
            print('Activating program human in vicinity...')
            ## ADD THE PROGRAM DEF TO STOP LIKE IN EXAMPLE.
            #EXAMPLE - os.system(r'start cmd /k "python C:\Users\******\********\Automated_Switcher\task_1.py"' )
            
        elif 'start empty running' in text:
            print(text[14:-3])
            print('Activating program Idle Running...')
            ## ADD THE PROGRAM DEF TO STOP LIKE IN EXAMPLE.
            #EXAMPLE - os.system(r'start cmd /k "python C:\Users\******\********\Automated_Switcher\task_1.py"' )
        
        elif 'start belt alignment' in text:
            print(text[14:-3])
            print('Activating program Belt Alignment...')
            ## ADD THE PROGRAM DEF TO STOP LIKE IN EXAMPLE.
            #EXAMPLE - os.system(r'start cmd /k "python C:\Users\******\********\Automated_Switcher\task_1.py"' )
            
        elif 'stop human in range' in text:
            print(text[14:-3])
            print('Deactivating program human in vicinity...')
            ## ADD THE PROGRAM DEF TO STOP LIKE IN EXAMPLE.
            #os.system(r'taskkill /im "C:\Windows\system32\cmd.exe - python C:\Users\gdgis\Documents\Automated_Switcher\task_1.py"')
        
        elif 'stop empty running' in text:
            print(text[14:-3])
            print('Deactivating program Idle Running...')
            ## ADD THE PROGRAM DEF TO STOP LIKE IN EXAMPLE.
            #os.system(r'taskkill /im "C:\Windows\system32\cmd.exe - python C:\Users\gdgis\Documents\Automated_Switcher\task_1.py"')
        
        elif 'stop belt alignment' in text:
            print(text[14:-3])
            print('Deactivating program Belt Alignment...')
            ## ADD THE PROGRAM DEF TO STOP LIKE IN EXAMPLE.
            #os.system(r'taskkill /im "C:\Windows\system32\cmd.exe - python C:\Users\gdgis\Documents\Automated_Switcher\task_1.py"')
        
        elif 'stop all program' in text:
            print(text[14:-3])
            print('Stopping All Programs...')
            ## ADD THE PROGRAM DEF TO STOP ALL THE APPLICATIONS BY PRIORITY ORDER LIKE IN EXAMPLE.
            #os.system(r'taskkill /im "C:\Windows\system32\cmd.exe - python C:\Users\gdgis\Documents\Automated_Switcher\task_1.py"')
        #__________________________________________Stoping the program_________________________________________________________________________
        elif 'stop listening' in text:
            print(text[14:-3])
            print('Ending As Per Instruction.')
            sys.exit(0)
            signal.signal(signal.SIGINT, sigint_handler)
        else:
            print(text[14:-3])
            print(False)

 