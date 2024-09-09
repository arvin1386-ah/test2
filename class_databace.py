import sqlite3




class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur=self.con.cursor()
        self.cur.execute("""
                         create table if not exists Contacts
                         (id integer primary key,fname text, lname text, address text, phone text)
                         """)
    def insert(self,fname,lname,address,phone):
        self.cur.execute("""
                         insert into Contacts values(NULL,?,?,?,?)
                         """,(fname,lname,address,phone))
        self.con.commit()
    def fetch(self):
        self.cur.execute('select * from Contacts order by lname desc')
        rows = self.cur.fetchall()
        return rows
    def remove(self,id):
        self.cur.execute('delete from Contacts where id = ?',(id,))
        self.con.commit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    