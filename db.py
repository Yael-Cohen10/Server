import sqlite3
from flask import g

conn=sqlite3.connect('message.db',check_same_thread=False)
c= conn.cursor()

def creaet_db():
    c= conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (application_id integer,session_id TEXT,message_id TEXT,participants TEXT, content TEXT)')
    conn.commit()

def insert(application_id,session_id,message_id,participantsList ,content):
    c.execute('INSERT INTO messages (application_id,session_id,message_id,participants ,content ) VALUES (?,?,?,?,?)',(application_id,session_id,message_id,participantsList ,content))
    conn.commit()

def read_from_db(column,req):
    c.execute("SELECT * FROM messages WHERE "+column+"=?",[req])
    data=c.fetchall()
    return data

def delete_from_db(column,req):
    c= conn.cursor()
    c.execute("DELETE FROM messages WHERE "+column+"=?",[req])
    conn.commit()






