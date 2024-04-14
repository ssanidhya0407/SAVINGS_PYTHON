import sqlite3

def create_savingsdb():
    con=sqlite3.connect(database=r'savings.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS savings(Ac text PRIMARY KEY ,custID text,Name text,remark TEXT,card text,bank text,branch text,opendate text)")
    con.commit()


create_savingsdb()

def create_fixeddepositdb():
    con=sqlite3.connect(database=r'fixeddeposit.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS fixeddeposit(Name	TEXT,Principal Amount	INTEGER,Operation Type	TEXT,Period	TEXT,Maturity Amount	INTEGER,Auto Renewal	TEXT,Auto Closure	TEXT,Nominee Name	TEXT,Bank	TEXT,Branch	TEXT,Date Of Deposit	TEXT,Account Number	TEXT,CIF ID	TEXT,Remark(s)	TEXT,Maturity Date	TEXT,PRIMARY KEY(Name)")
    con.commit()


create_fixeddepositdb()