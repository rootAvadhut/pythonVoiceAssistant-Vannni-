import Female_Voice as fv
import Recognizers as re
import subprocess as sp
import time
def windows_tasks():
    
    try: 
        print()
        print("Welcome To Windows Menu ".center(125))
        fv.pyttsx3.speak('Welcome To Windows Menu')
        fv.engine.runAndWait()
        print()
        while True: 
           #calling recognizer function from Recognizer module 
            re.recognize()
            
            #ask--> list windows task
            if((("list" in re.ch) or ("task" in re.ch)) or (("what" in re.ch) and ("can" in re.ch)) or ("do" in re.ch)):
                windows_task_list()
                
            
            #ask-> open/launch/ notepad plus
            elif ("editplus" in re.ch) or ("plus" in re.ch) and ("launch" in re.ch):
                fv.pyttsx3.speak("you have launched editplus")
                sp.Popen(['editplus'])
                time.sleep(5)
            elif ("open" in re.ch) and ("notepad" in re.ch) or ("pad" in re.ch):
                # using sp.Popen for  output or sp.getstatusoutput is for checking status code
                fv.pyttsx3.speak("you have opening notepad")
                sp.Popen(['notepad'])
                time.sleep(5)
                #show time/clock /what is time
            elif ("show" in re.ch) or ("clock" in re.ch) or ("time" in re.ch) or ("what" in re.ch) and ("is" in re.ch):
                fv.pyttsx3.speak("Showing time")
                sp.getoutput('timedate.cpl')
                time.sleep(5)
                #paint start /i want draw something
            elif ("paint" in re.ch) or ("start" in re.ch) or ("draw" in re.ch) or ("something" in re.ch):
                fv.pyttsx3.speak("Starting paint")
                sp.Popen(['mspaint'])
                time.sleep(5)
                #vlc player start/ run
            elif (("vlc" in re.ch) or ("player" in re.ch) and ("open" in re.ch)) or ("start" in re.ch):
                fv.pyttsx3.speak("Starting vlc player")
                sp.Popen(['vlc'])
                time.sleep(5)
                #open chrome browser
            elif (("chrome" in re.ch) or ("browser" in re.ch) and ("open" in re.ch)) or ("start" in re.ch):
                fv.pyttsx3.speak("Starting chrome")
                sp.Popen(['chrome'])
                time.sleep(5)
                #create folder or directory
            elif ('create' in re.ch and 'folder' in re.ch or 'directory' in re.ch):
                fv.pyttsx3.speak("Enter path where you want to create directory")
                d = input("Enter path: ").center(126)
                sp.getstatusoutput('mkdir {}'.format(d))
                # os.system('mkdir {}'.format(d))
                input()
                fv.pyttsx3.speak("directory has beeen created")
            #go back to main menu
            elif (("go" in re.ch) or ("back" in re.ch) or ("main" in re.ch)):
                fv.pyttsx3.speak("Going back to main menu")
                fv.pyttsx3.speak("Thank you!")
                print("Thank you!".center(125))
                break
            else:
                print("Don't understand".center(125))
                fv.pyttsx3.speak("Don't understand")            
            
    except:
        print("windows eroor")
        windows_tasks()
        
  
def windows_task_list(): 
            try:     
                fv.pyttsx3.speak('I can do below tasks as follow')
                fv.pyttsx3.speak('I can help with opening browser, such chrome and edge')
                print(" * Browsers".center(126))
                print()
                fv.pyttsx3.speak('I can help with opening Media player, such as vlc')
                print(" * Media player".center(126))
                print()
                fv.pyttsx3.speak('I can help with opening Editor, such as notepad, notepad+')
                print(" * Editor".center(126))
                print()
                fv.pyttsx3.speak('I can help with opening Accessories, such as paint, clock')
                print(" * Accessories".center(126))
                print()
                fv.pyttsx3.speak('Last but not least,I can help with creating Directory/folder')
                print(" * Create Directory/folder".center(126))
                print()                
            except:
                print("windows task error")
