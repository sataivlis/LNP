import sqlite3

def main():
    conn = sqlite3.connect('lnp.db')
    c  = conn.cursor()
    createTable(c)

def createTable (c):
    c.execute('''create table if not exists
        R(r_id integer PRIMARY KEY,
        r_name char(25) not null,
        r_level decimal(2,0) not null,
        r_star decimal(2,0) not null,
        r_creativity decimal(2,0) not null,
        r_decisionMaking decimal(2,0) not null,
        r_affinity decimal(2,0) not null,
        r_execution decimal(2,0) not null,
        r_upgrade bit default 'FALSE' not null
        )''')






if __name__ == '__main__':
    main()

