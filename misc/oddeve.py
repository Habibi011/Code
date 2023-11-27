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
def chatfunc(me,them):
    ask=input("Achu: ")
    sql="UPDATE chat SET message=\'"+ask+"\',status=False WHERE user=\""+me+"\""
    crsr.execute(sql)
    mydb.commit()
    print("Waiting for Deepu..", end="\r")
    reply(me,them)
def reply(me,them):
    time.sleep(2)
    sql="SELECT status from chat WHERE user=\""+them+"\""
    crsr.execute(sql)
    status=crsr.fetchall()
    while status[0][0]!=0:
        crsr.execute(sql)
        status=crsr.fetchall()
        mydb.commit()
        time.sleep(0.5)
    sql="SELECT message from chat WHERE user=\""+them+"\""
    crsr.execute(sql)
    msg=crsr.fetchall()
    print("Deepu:",msg[0][0])
    playsound(700,500)
    playsound(700,500)
    sql="UPDATE chat SET status=True WHERE user=\""+me+"\""
    crsr.execute(sql)
    mydb.commit()
    chatfunc()
crsr=mydb.cursor()
print(mydb)
print("Server loaded")
crsr.execute("SHOW TABLES LIKE \'chat\'")
tab=crsr.fetchall()
if tab[0][0]=='chat':
    crsr.execute("DROP TABLE chat")
    mydb.commit()
    crsr.execute("CREATE TABLE chat (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), message VARCHAR(255),status boolean)")
    mydb.commit()
time.sleep(2)
cScreen()
print("CHAT ROOM: 19946")
nName=input("Enter your Nickname: ")
print("User Created")
sql = "INSERT INTO chat (user,status) VALUES (%s, %s)"
val = (nName,True)
crsr.execute(sql,val)
sql="SELECT id from chat WHERE user=\""+nName+"\""
crsr.execute(sql)
id=crsr.fetchall()
me=nName
if id[0][0] ==1:
    crsr.execute("SELECT user from chat WHERE id=2")
    x=crsr.fetchall()
    them=x[0][0]
    chatfunc(me,them)
else:
    crsr.execute("SELECT user from chat WHERE id=1")
    x=crsr.fetchall()
    them=x[0][0]
    reply(me,them)