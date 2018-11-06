import sqlite3

conn = sqlite3.connect('lnp.db')
c  = conn.cursor()

def createTable (c):

# create table heroine;
    c.execute(''' CREATE TABLE IF NOT EXISITS heroine (h_ID integer PRIMARY KEY,
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










