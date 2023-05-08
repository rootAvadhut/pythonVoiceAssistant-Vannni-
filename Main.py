import Recognizers as re
import Cloud_Tasks as ct
import Female_Voice as fv
import Windows_Tasks as wt
import Linux_Tasks as lt
import Main_Task_List as mtl
import Intro

Intro.intro()
try:
        while True:
            print()
            print("\t \t \t Tell me your requirement... i am listening : ", end='')
            re.recognize()

            #greeting to team and introduction
            if("hello" in re.ch) or ("hi" in re.ch) and ("heya" in re.ch) or ("hey" in re.ch):
                fv.pyttsx3.speak("hello guys , how are you ...?")
            elif("fine" in re.ch) or ("what" in re.ch) and ("about" in re.ch):
                fv.pyttsx3.speak("i am good too")
            elif("tell" in re.ch) or ("about" in re.ch) and ("yourself" in re.ch):
                fv.pyttsx3.speak("i am your voice assistant vaani, i am very intelligent , and i can control your desktop and linux server for you")
            
            #what can you do for me
            elif("what" in re.ch) and ("can" in re.ch) and ("do" in re.ch):
                mtl.main_task_list()
        
            #windows/window menu or start windows/window 
            elif ((("start" in re.ch) and ("windows" in re.ch) or ("window" in re.ch)) or( ("go" in re.ch) and ("to" in re.ch) and ("windows" in re.ch) or ("window" in re.ch))):
                fv.pyttsx3.speak("okay")
                wt.windows_tasks()
            #start linux menu / goto linux
            elif ((("start" in re.ch) and ("linux" in re.ch)) or( ("go" in re.ch) or ("to" in re.ch) and ("linux" in re.ch))):
                fv.pyttsx3.speak("okay")
                lt.linux_tasks()
            #start cloud 
            elif ((("start" in re.ch) and ("cloud" in re.ch) or ("cloud" in re.ch)) or( ("go" in re.ch) or ("to" in re.ch) and ("cloud" in re.ch))):
                fv.pyttsx3.speak("okay")
                ct.cloud_tasks()
            elif ("exit" in re.ch) or ("stop" in re.ch) or ("bye" in re.ch):
                fv.pyttsx3.speak("see you soon,, have a nice day...!!!")
                print()
                print("See You Soon, Have a nice day...!!!".center(125))
                break
            else:
                print("not understand".center(125)) 
except:
    re.recognize()
    print('main error')


