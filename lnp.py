import sqlite3

conn = sqlite3.connect('lnp.db')
c  = conn.cursor()

def createTable (c):
