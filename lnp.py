import sqlite3
import csv

def main():
    conn = sqlite3.connect('lnp.db')
    c  = conn.cursor()
    createTable(c)
    #insertC(c, conn)
    insertR(c, conn)
    disc(conn)


def createTable (c):

# create table heroine;
    c.execute(''' CREATE TABLE IF NOT EXISTS heroine (h_ID integer PRIMARY KEY,
        h_name varchar(15) NOT NULL
        ); ''')

# create table company;
    c.execute(''' CREATE TABLE IF NOT EXISTS company (c_ID integer PRIMARY KEY,
        c_name varchar(15) NOT NULL,
        c_creativity decimal(2,0) NOT NULL,
        c_decisionMaking decimal(2,0) NOT NULL,
        c_affinity decimal(2,0) NOT NULL,
        c_execution decimal(2,0) NOT NULL
        ); ''' )

# create table stage_company;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageCompany (sc_ID integer PRIMARY KEY,
        sc_chapterNumber decimal(2,0) NOT NULL,
        sc_calcScore decimal(2,0) NOT NULL,
        sc_companyScore decimal(2,0) NOT NULL,
        sc_clearScore decimal(2,0) NOT NULL
        ); ''')

# create table stages;
    c.execute(''' CREATE TABLE IF NOT EXISTS stages (s_chapterNumber integer PRIMARY KEY,
        s_stars decimal(2,0) NOT NULL,
        s_requireScore decimal(2,0) NOT NULL
        ); ''')

# create table stage R-cards;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageR (stgR_ID integer PRIMARY KEY,
        stgR_cardD decimal(2,0) NOT NULL,
        stgR_chapterNumber decimal(2,0) NOT NULL,
        stgR_calcScore decimal(2,0) NOT NULL,
        stgR_sumScore decimal(2,0) NOT NULL
        ); ''')

# create table stage R-cards;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageR (stgR_ID integer PRIMARY KEY,
        stgR_cardD decimal(2,0) NOT NULL,
        stgR_chapterNumber decimal(2,0) NOT NULL,
        stgR_calcScore decimal(2,0) NOT NULL,
        stgR_sumScore decimal(2,0) NOT NULL
        ); ''')

    # create table stage SR-cards;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageSR (stgSR_ID integer PRIMARY KEY,
        stgSR_cardD decimal(2,0) NOT NULL,
        stgSR_chapterNumber decimal(2,0) NOT NULL,
        stgSR_calcScore decimal(2,0) NOT NULL,
        stgSR_sumScore decimal(2,0) NOT NULL
        ); ''')

    # create table stage SSR-cards;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageSSR (stgSSR_ID integer PRIMARY KEY,
        stgSSR_cardD decimal(2,0) NOT NULL,
        stgSSR_chapterNumber decimal(2,0) NOT NULL,
        stgSSR_calcScore decimal(2,0) NOT NULL,
        stgSSR_sumScore decimal(2,0) NOT NULL
        ); ''')

    # create table R cards;
    c.execute('''create table if not exists
        R(r_id integer PRIMARY KEY,
        r_name char(25) not null,
        r_level decimal(2,0) not null,
        r_star decimal(2,0) not null,
        r_creativity decimal(2,0) not null,
        r_decisionMaking decimal(2,0) not null,
        r_affinity decimal(2,0) not null,
        r_execution decimal(2,0) not null,
        r_upgrade bit default 'FALSE' not null,
        r_chid integer not null
        )''')

    # create table SR cards;
    c.execute('''create table if not exists
        SR(sr_id integer PRIMARY KEY,
        sr_name char(25) not null,
        sr_level decimal(2,0) not null,
        sr_star decimal(2,0) not null,
        sr_creativity decimal(2,0) not null,
        sr_decisionMaking decimal(2,0) not null,
        sr_affinity decimal(2,0) not null,
        sr_execution decimal(2,0) not null,
        sr_upgrade bit default 'FALSE' not null,
        sr_chid integer not null
        )''')

    # create table SSR cards;
    c.execute('''create table if not exists
        SSR(sr_id integer PRIMARY KEY,
        ssr_name char(25) not null,
        ssr_level decimal(2,0) not null,
        ssr_star decimal(2,0) not null,
        ssr_creativity decimal(2,0) not null,
        ssr_decisionMaking decimal(2,0) not null,
        ssr_affinity decimal(2,0) not null,
        ssr_execution decimal(2,0) not null,
        ssr_upgrade bit default 'FALSE' not null,
        ssr_chid integer not null
        )''')

    # create table characters;
    c.execute('''create table if not exists
        Characters(ch_id integer PRIMARY KEY,
        ch_name char(25) not null)''')

# insert characters;
#def insertC(c, conn):

#    name = [("MO XU",),
#            ("QI BAI",),
#            ("ZEYAN LI",),
#            ("QILUO ZHOU",),
#            ]
#
#            c.executemany('INSERT INTO Characters(ch_name) VALUES(?)', name)
#            conn.commit()

def insertR(c,conn):
    r_sql = "insert into R (r_name,r_level,r_star,r_creativity,r_decisionMaking,r_affinity,r_execution,r_upgrade,r_chid) values (?,?,?,?,?,?,?,?,?)"
    with open ('r.csv','r', encoding="ISO-8859-1") as r:
        dr = csv.DictReader(r)
        to_db = [(i['r_name'],i['r_level'],i['r_star'],i['r_creativity'],i['r_decisionMaking'],i['r_affinity'],i['r_execution'],i['r_upgrade'],i['r_chid']) for i in dr]

    c.executemany(r_sql,to_db)
    conn.commit()


def disc(conn):
    conn.close()



if __name__ == '__main__':
    main()



