import Female_Voice as fv
import Recognizers as re
import subprocess as sp
import Linux_voice as lv
from os import system
def linux_tasks():
    
    try: 
        print()
        print("Welcome To Linux Menu ".center(125))
        fv.pyttsx3.speak('Welcome To Linux Menu')
        fv.engine.runAndWait()
        print()
        while True: 
           #calling recognizer function from Recognizer module 
            re.recognize()
            
            #ask--> what can do for me
            if(( ("task" in re.ch)) or (("what" in re.ch) and ("can" in re.ch)) or ("do" in re.ch)):
                linux_task_list()
            # provice linux cli/terminal
            elif (('provide' in re.ch) and ('linux' in re.ch) or ('cli' in re.ch)or ('terminal' in re.ch)):
                linux_cli()
            
            #control linux from voice / start voice command    
            elif ((('control' in re.ch) and ('linux' in re.ch) and ('voice' in re.ch))or ('start' in re.ch) and ('voice' in re.ch) or('command' in re.ch)):
                lv.linux_voice()

            #go back to main menu
            elif (("go" in re.ch) or ("back" in re.ch) or ("main" in re.ch)):
                fv.pyttsx3.speak("Going back to main menu")
                fv.pyttsx3.speak("Thank you!")
                print("Thank you!".center(125))
                break
            else:
                print("Don't understand".center(125))            
            
    except:
        print("linux eroor")
        re.recognize()
        
  
def linux_task_list(): 
            try:     
                fv.pyttsx3.speak('I can do below tasks as follow')
                print(" * Linux and It's Tools".center(126))
                print()
                fv.pyttsx3.speak('linux cli')
                fv.pyttsx3.speak('where you can access linux and its tool directly on windows prompt')
                
                print(" * Linux Commands from Voice".center(126))
                print()
                fv.pyttsx3.speak('Linux Commands from Voice')
                fv.pyttsx3.speak('In this feature you can monitor linux')
                fv.pyttsx3.speak('and run commands such as date, checking webserver service running and many more from just voice command')
                
            except:
                print("windows task error")
#start linux cli function
def linux_cli(): 
    fv.pyttsx3.speak("you can control linux from CLI")
    fv.pyttsx3.speak("In which you can use linux from your windows prompt and control all linux such as commands and tools")
    system("ssh root@192.168.1.104")  