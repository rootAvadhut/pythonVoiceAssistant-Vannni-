import Female_Voice as fv
import time
import Recognizers as re
import webbrowser as wb
import subprocess as sp
def cloud_tasks():
    
    try: 
        print()
        print("Welcome To AWS Cloud Menu ".center(125))
        fv.pyttsx3.speak('Welcome To AWS cloud Menu')
        fv.engine.runAndWait()
        print()
        while True: 
           #calling recognizer function from Recognizer module 
            re.recognize()
            
            #ask--> list cloud task
            if((("list" in re.ch) or ("task" in re.ch)) or (("what" in re.ch) and ("can" in re.ch)) or ("do" in re.ch)):
                cloud_task_list()
            #create key pair   
            elif(("create" in re.ch) and ("key" in re.ch) or ("pair" in re.ch)):
               key=input("Enter your key-name:")
               sp.getoutput("aws ec2 create-key-pair --key-name {0}".format(key))
               fv.pyttsx3.speak("Creating a new key pair for you")
               wb.open("https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#KeyPairs:")
               fv.pyttsx3.speak("key pair created successfully")
               print(">>Key-Pair created successfully<<".center(125))
               time.sleep(7)
               #configure security group
            elif(("configure" in re.ch) or ("security" in re.ch) or ("group" in re.ch)):
                sg=input("Enter your security group name :")
                sp.getoutput("aws ec2 create-security-group  --group-name {0} --description project".format(sg))
                fv.pyttsx3.speak("Configuring your aws security group")
                wb.open("https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#SecurityGroups:")
                fv.pyttsx3.speak("security group is configured")
                print(">>Security Group configured<<".center(125))
                time.sleep(7)
                #launch ec2 instance
            elif(("ec2" in re.ch) or ("instance" in re.ch)and ("launch" in re.ch)):
                sp.getoutput("aws ec2 run-instances --image-id ami-0c768662cc797cd75 --count 1 --instance-type t2.micro --key-name MyProjectKey --security-group-ids sg-000088eaabe5ed0b5")
                fv.pyttsx3.speak("Launching a new ec2 instance for you")
                wb.open("https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:v=3;$case=tags:true%5C,client:false;$regex=tags:false%5C,client:false")
                fv.pyttsx3.speak("EC2 Instance is launched")
                print(">>EC2 Instance is launched<<".center(125))
                time.sleep(10)
                #launch ebs volume
            elif(("launch" in re.ch) and ("ebs" in re.ch) or ("volume" in re.ch)):
                sp.getoutput("aws ec2 create-volume --volume-type gp2 --size 1 -    -availability-zone ap-south-1b")
                fv.pyttsx3.speak("Launching an ebs volume of 1GiB in mumbai region")
                wb.open("https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Volumes:")
                fv.pyttsx3.speak("EBS  volume of 1GiB is launched")
                print(">>EBS Volume is launched<<".center(125))
                time.sleep(10)
            #start instance
            elif(("start" in re.ch) and ("instance" in re.ch) or ("existing" in re.ch)):
                sp.getoutput("aws ec2 start-instances --instance-ids i-0b5ba266f2a83c415")
                fv.pyttsx3.speak("starting existing ec2 instance for you")
                wb.open("https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:v=3;$case=tags:true%5C,client:false;$regex=tags:false%5C,client:false")
                time.sleep(5)
                fv.pyttsx3.speak("ec2 instance is started")
                print(">>EC2 Instance is Started<<".center(125))
                time.sleep(10)
            #stop instance
            elif(("top" in re.ch)or ("stop" in re.ch) and ("instance" in re.ch)):
                sp.getoutput("aws ec2 stop-instances --instance-ids i-0b5ba266f2a83c415")
                fv.pyttsx3.speak("stoping existing ec2 instance for you")
                wb.open("https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:v=3;$case=tags:true%5C,client:false;$regex=tags:false%5C,client:false")
                time.sleep(5)
                fv.pyttsx3.speak("ec2 instance is stoped")
                print(">>EC2 Instance is Stoped<<".center(125))
                time.sleep(10)
            #attach storage 
            elif ("attach" in re.ch) and ("storage" in re.ch) or ("memory" in re.ch):
                sp.getoutput("aws ec2 attach-volume --volume-id vol-02b239aaf050881d3 --instance-id i-0b5ba266f2a83c415 --device /dev/sdf")
                fv.pyttsx3.speak("Your EBS volume is  attaching to your launched instance")
                wb.open("https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Volumes:")
                time.sleep(3)
                fv.pyttsx3.speak("EBS volume is attached")
                print(">>EBS volume is attached<<".center(125))
                time.sleep(7)
            #remove storage
            elif ("remove" in re.ch) and ("storage" in re.ch) or ("memory" in re.ch):
                sp.getoutput("aws ec2 detach-volume --volume-id vol-02b239aaf050881d3")
                fv.pyttsx3.speak("Your EBS volume is  detaching from your launched instance")
                wb.open("https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Volumes:")
                time.sleep(3)
                fv.pyttsx3.speak("EBS volume is detached")
                print(">>EBS volume is deteched<<".center(125))
                time.sleep(7)
            elif ("s3" in re.ch) or ("bucket" in re.ch) and ("create" in re.ch):
                s3()                
                status= b[0]
                if status == 0:
                    pass
                else:
                    print("already name exist".center(125))
                    fv.pyttsx3.speak("already name exist, please enter unique a bucket name ")
                    s3()
                fv.pyttsx3.speak("Creating a S3 bucket")
                wb.open("https://s3.console.aws.amazon.com/s3/buckets?region=ap-south-1")
                time.sleep(5)
                fv.pyttsx3.speak("s3 bucket created successfully")
                print(">>S3 Bucket Created<<".center(125))
                time.sleep(7)

            #go back to main menu
            elif (("go" in re.ch) or ("back" in re.ch) or ("main" in re.ch)):
                fv.pyttsx3.speak("Going back to main menu")
                fv.pyttsx3.speak("Thank you!")
                print("Thank you!".center(125))
                break
            else:
                print("Don't understand".center(125))            
            
    except:
        print("windows eroor")
        re.recognize()
        
#cloud task list  
def cloud_task_list(): 
            try:     
                fv.pyttsx3.speak('I can do below tasks as follow')
                fv.pyttsx3.speak("As per your choice,now i will automate aws cloud")
                fv.pyttsx3.speak("Creating a new key pair")
                print()
                print(">>Creating a new key pair<<".center(125))
                fv.pyttsx3.speak("Creating a security group")
                
                print()
                print(">>Creating a security group<<".center(125))
                fv.pyttsx3.speak("Launching a new ec2-instance")
                
                print()
                print(">>Launching a new ec2-instance<<".center(125))
                fv.pyttsx3.speak("Launching a ebs volume")
                
                print()
                print(">>Launching a EBS volume<<".center(125))
                fv.pyttsx3.speak("Attaching your EBS volume to your launched instance")

                print()
                print(">>Start Instance<<".center(125))
                fv.pyttsx3.speak("i can help with Starting existing  Instance")

                print()
                print(">>Stop Instance<<".center(125))
                fv.pyttsx3.speak("i can help with Stopping existing Instance")
 
                print()
                print(">>Creation of S3 bucket<<".center(125))
                fv.pyttsx3.speak("Creation of S3 bucket")
                
                # print()
                # print(">>Creation of S3 bucket<<".center(125))
                # fv.pyttsx3.speak("Copying file from local pc to AWS S3 bucket")
            except:
                print("cloud task error")
def s3():
    fv.pyttsx3.speak("S3 bucket is object storage and make sure the bucket name must be unique")
    bk=input("Enter a name creating bucket : ")
    global b
    b=sp.getstatusoutput("aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1 --acl bucket-owner-full-control".format(bk))