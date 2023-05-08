import Female_Voice as fv
def main_task_list(): 
  try:     
      fv.pyttsx3.speak('I can do below tasks as follow')
      fv.pyttsx3.speak('firstly i can help with windows')
      print()
      print(" * Windows ".center(126))
      print()
      fv.pyttsx3.speak('I can help with Linux')
      print(" * Linux ".center(126))
      print()
      fv.pyttsx3.speak('and also i can help with aws cloud')
      print(" * AWS Cloud ".center(126))
      print()
  except:
      print("windows task error")