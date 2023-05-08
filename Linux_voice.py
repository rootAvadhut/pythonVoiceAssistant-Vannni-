import Female_Voice as fv
import Recognizers as re
import subprocess as sp
from os import system


def linux_voice():
        try:
            fv.pyttsx3.speak("Now you can control linux command from voice")
            print("* start Voice Command".center(125))
            while True:
                re.recognize()
                if("date" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=date")
                    fv.pyttsx3.speak("showing date")
                elif("calendar" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=cal")
                    fv.pyttsx3.speak("showing calendar")
                elif("IP" in re.ch )or ("ip address" in re.ch) or ("address" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=ifconfig")
                    fv.pyttsx3.speak("showing IP address")
                elif("active ports" in re.ch) or ("ports" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=netstat%20-tnlp")
                    fv.pyttsx3.speak("showing active ports")
                elif("amount" in re.ch) or ("disc" in re.ch) and ("space" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=df%20-h")
                    fv.pyttsx3.speak("showing amount of disc space")
                elif("status" in re.ch) or ("webserver" in re.ch) and ("apache" in re.ch) or ("httpd" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=systemctl%20status%20httpd")
                    fv.pyttsx3.speak("apache webserver is running")
                elif("state of selinux" in re.ch) or ("selinux" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=getenforce")
                    fv.pyttsx3.speak("SElinux is permissive")
                elif("yum" in re.ch) or ("module" in re.ch) and ("list" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=yum%20module%20list")
                    fv.pyttsx3.speak("Here is the long list of modules")
                elif("package" in re.ch) or ("firefox" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=yum%20whatprovides%20firefox")
                    fv.pyttsx3.speak("Here is the package name of firefox")
                elif("ping" in re.ch) or ("google" in re.ch) and ("server" in re.ch):
                    system("curl http://192.168.1.104/cgi-bin/local.py?x=ping%20-c%205%208.8.8.8")
                    fv.pyttsx3.speak("Server is Ping able")
                elif (("go" in re.ch) or ("back" in re.ch) or ("main" in re.ch)):
                    fv.pyttsx3.speak("Going back to main menu")
                    fv.pyttsx3.speak("Thank you!")
                    print("Thank you!".center(125))
                    break
                else:
                    print("Don't understand".center(125))
        except:
            print("voice Error ")

  
  



