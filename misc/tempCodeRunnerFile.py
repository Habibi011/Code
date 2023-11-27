sql1="UPDATE chat SET status=True WHERE user=\"achu\""
sql2="UPDATE chat SET status=True WHERE user=\"deepu\""
crsr.execute(sql1)
crsr.execute(sql2)
mydb.commit()