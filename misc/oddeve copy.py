import subprocess
import sys
import os
import math
import random
import base64
import time
def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
def cScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
def cLine():
    sys.stdout.write('\x1b[2K') 
try:
    import mysql.connector
except:
    print("Connector Not found! Installing Connector...")
    install("mysql-connector-python")
    cScreen()
    print("Connector Installed")
    import mysql.connector
try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)
print("Loading Server..")
mydb = mysql.connector.connect(
  host="sql12.freesqldatabase.com",
  user="sql12665125",
  password=str(base64.b64decode('djV4V2FONmJZdQ=='))[2:-1],
  database="sql12665125"
)
crsr=mydb.cursor()
print(mydb)
time.sleep(2)
cScreen()
print("CHAT ROOM: 19946")
print("Wating for message...", end="\r")
# nName=input("Enter your Nickname: ")
# ask=input("Start Chat?(y/n)")
# if ask=='y':
#      print("User Created")
#      sql = "INSERT INTO chat (user, message,status) VALUES (%s, %s, %s)"
#      val = (nName, (str(nName)+" entered the chat room"),True)
#      crsr.execute(sql,val)
# else:
#     print("Exiting...")
sql1="UPDATE chat SET status=True WHERE user=\"achu\""
sql2="UPDATE chat SET status=True WHERE user=\"deepu\""
crsr.execute(sql1)
crsr.execute(sql2)
mydb.commit()
def chatfunc():
    ask=input("Deepu: ")
    sql="UPDATE chat SET message=\'"+ask+"\',status=False WHERE user=\"deepu\""
    crsr.execute(sql)
    mydb.commit()
    print("Waiting for Achu..",end='\r')
    reply()
def reply():
    time.sleep(2)
    sql="SELECT status from chat WHERE user=\"achu\""
    crsr.execute(sql)
    status=crsr.fetchall()
    while status[0][0]!=0:
        crsr.execute(sql)
        status=crsr.fetchall()
        mydb.commit()
        time.sleep(0.5)
    sql="SELECT message from chat WHERE user=\"achu\""
    crsr.execute(sql)
    msg=crsr.fetchall()
    print("Achu:",msg[0][0])
    playsound(700,500)
    playsound(700,500)
    sql="UPDATE chat SET status=True WHERE user=\"deepu\""
    crsr.execute(sql)
    mydb.commit()
    chatfunc()
reply()

