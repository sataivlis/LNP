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

    c.execute('''create table if not exists
        SR(sr_id integer PRIMARY KEY,
        sr_name char(25) not null,
        sr_level decimal(2,0) not null,
        sr_star decimal(2,0) not null,
        sr_creativity decimal(2,0) not null,
        sr_decisionMaking decimal(2,0) not null,
        sr_affinity decimal(2,0) not null,
        sr_execution decimal(2,0) not null,
        sr_upgrade bit default 'FALSE' not null
        )''')

    c.execute('''create table if not exists
        SSR(sr_id integer PRIMARY KEY,
        ssr_name char(25) not null,
        ssr_level decimal(2,0) not null,
        ssr_star decimal(2,0) not null,
        ssr_creativity decimal(2,0) not null,
        ssr_decisionMaking decimal(2,0) not null,
        ssr_affinity decimal(2,0) not null,
        ssr_execution decimal(2,0) not null,
        ssr_upgrade bit default 'FALSE' not null
        )''')

    c.execute('''create table if not exists
        Characters(ch_id integer PRIMARY KEY,
        ch_name char(25) not null)''')






if __name__ == '__main__':
    main()

