import time
def load():
   loadText="loading"
   for x in range(1,5):
      time.sleep(0.2)
      print(loadText, end="\r")
      loadText+="."
load()