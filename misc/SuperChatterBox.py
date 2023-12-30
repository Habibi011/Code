import subprocess
import sys
import os
import random
import base64
import time
print("importing packages..",end="\r")
time.sleep(0.5)
def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
def cScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
def cLine():
     sys.stdout.write('\x1b[1A')
     sys.stdout.write('\x1b[2K')
try:
    import mysql.connector
    print("importing \"mysql-connector\"",end="\r")
except:
    print("\"mysql-connector\" Not found! Installing Connector...")
    install("mysql-connector-python")
    cScreen()
    print("Connector Installed")
    import mysql.connector
try:
    import winsound
except ImportError:
    def playsound(frequency,duration):
        pass
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)
time.sleep(0.5)
firstTime=True
def chatfunc(us1,us2):
    global firstTime
    if firstTime==True:
        print(us2,"entered the chat")
        firstTime=False
    ask=input(nName+" : ")
    sql="UPDATE chat SET message=\'"+ask+"\',status=False WHERE user=\""+us1+"\""
    crsr.execute(sql)
    mydb.commit()
    if ask=="/endchat":
        print(nName+" left the chat")
        print("Thanks for using Super ChatterBox!")
        input("Press any key to end: ")
        return None
    else:
        print(us2," is typing.....")
        reply(us1,us2)
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
    cLine()
    sql="SELECT message from chat WHERE user=\""+them+"\""
    crsr.execute(sql)
    msg=crsr.fetchall()
    if msg[0][0]=="/endchat":
        print(them+" left the chat.")
        print("Thanks for using Super ChatterBox")
        input("Press any key to end: ")
        return None
    print(them+" :",msg[0][0])
    playsound(700,500)
    sql="UPDATE chat SET status=True WHERE user=\""+me+"\""
    crsr.execute(sql)
    mydb.commit()
    chatfunc(me,them)
#>>>main
cScreen()
mydb=None
print("Loading Super ChatterBox Server..")
def loadServer():
    global mydb
    try:
        mydb = mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12665125",
        password=str(base64.b64decode('djV4V2FONmJZdQ=='))[2:-1],
        database="sql12665125"
        )
    except:
        loadServer()
loadServer()
crsr=mydb.cursor(buffered=True)
crsr.execute("SHOW TABLES LIKE \'chat\'")
tab=crsr.fetchall()
def checkTab():
    try:
        try:
            if tab[0][0]=='chat':
                crsr.execute("SELECT*FROM chat")
                res=crsr.fetchall()
                if len(res)==0:
                    pass
                else:
                    crsr.execute("DROP TABLE chat")
                    mydb.commit()
                    crsr.execute("CREATE TABLE chat (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), message VARCHAR(255),status boolean)")
                    mydb.commit()
        except:
            crsr.execute("CREATE TABLE chat (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), message VARCHAR(255),status boolean)")
            mydb.commit()
    except:
        checkTab()
checkTab()
print(mydb)
print("Server loaded!")
time.sleep(2)
cScreen()
print("           ~~~  SUPER CHATTERBOX  ~~~")
print("1)Two-User Buddy Chat in python (doesnt run on idle, Run the run.bat file for best experience))")
print("2)Enter Nickname to Start Chatting with your buddy")
print("3)Enter /endchat to quit chat")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
nName=input("Enter your Nickname: ")
print("Creating user..", end="\r")
time.sleep(2)
print("Finding room....", end="\r")
sql = "INSERT INTO chat (user,status) VALUES (%s, %s)"
val = (nName,True)
crsr.execute(sql,val)
mydb.commit()
cLine()
print("SUPERCHAT ROOM: "+(''.join(["{}".format(random.randint(0, 9)) for num in range(0, 6)])))
print()
print(nName,"entered the chat")
print("Finding your buddy...", end="\r")
time.sleep(2)
sql="SELECT id from chat WHERE user=\""+nName+"\""
crsr.execute(sql)
id=crsr.fetchall()
time.sleep(2)
if id[0][0] ==1:
    def findSecond():
        try:
            crsr.execute("SELECT user from chat WHERE id <> 1")
            x=crsr.fetchall()
            mydb.commit()
            chatfunc(nName,x[0][0])
        except:
            findSecond()
    findSecond()
else:
    crsr.execute("SELECT user from chat WHERE id=1")
    x=crsr.fetchall()
    print(x[0][0],"entered the chat")
    firstTime=False
    print(x[0][0],"is typing...")
    reply(nName,x[0][0])