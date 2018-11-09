import sqlite3
import xlrd
#import csv
#import codecs


def main():
    conn = sqlite3.connect('lnp.db')
    c = conn.cursor()
    createTable(c)
    #insertC(c, conn)
    #    insertExcelSSR(c, conn)
    #insertExcelSR(c, conn)
    
    disc(conn)
#def insertExcelSSR(c, conn):
#
#    book = xlrd.open_workbook("SSR_data.xlsx")
#    sheet = book.sheet_by_name("Sheet1")
#
#    sql = """ INSERT INTO SSR (ssr_name, ssr_level, ssr_star, ssr_creativity, ssr_decisionMaking, ssr_affinity, ssr_execution, ssr_upgrade, ssr_chid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) """
#
#    for r in range(1, sheet.nrows):
#        ssr_name                = sheet.cell(r,0).value
#        ssr_level               = sheet.cell(r,1).value
#        ssr_star                = sheet.cell(r,2).value
#        ssr_creativity          = sheet.cell(r,3).value
#        ssr_decisionMaking      = sheet.cell(r,4).value
#        ssr_affinity            = sheet.cell(r,5).value
#        ssr_execution           = sheet.cell(r,6).value
#        ssr_upgrade             = sheet.cell(r,7).value
#        ssr_chid                = sheet.cell(r,8).value
#
#        values = (ssr_name, ssr_level, ssr_star, ssr_creativity, ssr_decisionMaking, ssr_affinity, ssr_execution, ssr_upgrade, ssr_chid)
#
#        c.execute(sql, values)
#
#    conn.commit()

#def insertExcelSR(c, conn):
#
#    book = xlrd.open_workbook("SR_data.xlsx")
#    sheet = book.sheet_by_name("Sheet1")
#
#    sql = """ INSERT INTO SR (sr_name, sr_level, sr_star, sr_creativity, sr_decisionMaking, sr_affinity, sr_execution, sr_upgrade, sr_chid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) """
#
#    for r in range(1, sheet.nrows):
#        sr_name                = sheet.cell(r,0).value
#        sr_level               = sheet.cell(r,1).value
#        sr_star                = sheet.cell(r,2).value
#        sr_creativity          = sheet.cell(r,3).value
#        sr_decisionMaking      = sheet.cell(r,4).value
#        sr_affinity            = sheet.cell(r,5).value
#        sr_execution           = sheet.cell(r,6).value
#        sr_upgrade             = sheet.cell(r,7).value
#        sr_chid                = sheet.cell(r,8).value
#
#        values = (sr_name, sr_level, sr_star, sr_creativity, sr_decisionMaking, sr_affinity, sr_execution, sr_upgrade, sr_chid)
#
#        c.execute(sql, values)
#
#    conn.commit()
#


def createTable(c):
    
    # create table stage R-cards;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageR (stgR_ID integer PRIMARY KEY,
        stgR_cardID decimal(2,0) NOT NULL,
        stgR_chapterNumber decimal(2,0) NOT NULL
        ); ''')
    
    # create table stage SR-cards;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageSR (stgSR_ID integer PRIMARY KEY,
        stgSR_cardID decimal(2,0) NOT NULL,
        stgSR_chapterNumber decimal(2,0) NOT NULL
        ); ''')
    
    # create table stage SSR-cards;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageSSR (stgSSR_ID integer PRIMARY KEY,
        stgSSR_cardID decimal(2,0) NOT NULL,
        stgSSR_chapterNumber decimal(2,0) NOT NULL
        ); ''')
    
    # create table stage_company;
    c.execute(''' CREATE TABLE IF NOT EXISTS stageCompany (sc_ID integer PRIMARY KEY,
        sc_chapterNumber decimal(2,0) NOT NULL,
        sc_companyID decimal(2,0) NOT NULL
        ); ''')
    
    # create table stage;
    c.execute(''' CREATE TABLE IF NOT EXISTS stage (s_chapterNumber integer PRIMARY KEY,
        s_requireScore decimal(2,0) NOT NULL,
        s_percentageC decimal(2,0) NOT NULL,
        s_percentageDM decimal(2,0) NOT NULL,
        s_percentageA decimal(2,0) NOT NULL,
        s_percentageE decimal(2,0) NOT NULL
        ); ''')







#def createTable (c):
#
## create table heroine;
#    c.execute(''' CREATE TABLE IF NOT EXISTS heroine (h_ID integer PRIMARY KEY,
#        h_name varchar(15) NOT NULL
#        ); ''')
#
## create table company;
#    c.execute(''' CREATE TABLE IF NOT EXISTS company (c_ID integer PRIMARY KEY,
#        c_name varchar(15) NOT NULL,
#        c_creativity decimal(2,0) NOT NULL,
#        c_decisionMaking decimal(2,0) NOT NULL,
#        c_affinity decimal(2,0) NOT NULL,
#        c_execution decimal(2,0) NOT NULL
#        ); ''')
#
## create table stage_company;
#    c.execute(''' CREATE TABLE IF NOT EXISTS stageCompany (sc_ID integer PRIMARY KEY,
#        sc_chapterNumber decimal(2,0) NOT NULL,
#        sc_calcScore decimal(2,0) NOT NULL,
#        sc_companyScore decimal(2,0) NOT NULL,
#        sc_clearScore decimal(2,0) NOT NULL
#        ); ''')
#
## create table stages;
#    c.execute(''' CREATE TABLE IF NOT EXISTS stages (s_chapterNumber integer PRIMARY KEY,
#        s_stars decimal(2,0) NOT NULL,
#        s_requireScore decimal(2,0) NOT NULL
#        ); ''')
#
## create table stage R-cards;
#    c.execute(''' CREATE TABLE IF NOT EXISTS stageR (stgR_ID integer PRIMARY KEY,
#        stgR_cardD decimal(2,0) NOT NULL,
#        stgR_chapterNumber decimal(2,0) NOT NULL,
#        stgR_calcScore decimal(2,0) NOT NULL,
#        stgR_sumScore decimal(2,0) NOT NULL
#        ); ''')
#
## create table stage R-cards;
#    c.execute(''' CREATE TABLE IF NOT EXISTS stageR (stgR_ID integer PRIMARY KEY,
#        stgR_cardD decimal(2,0) NOT NULL,
#        stgR_chapterNumber decimal(2,0) NOT NULL,
#        stgR_calcScore decimal(2,0) NOT NULL,
#        stgR_sumScore decimal(2,0) NOT NULL
#        ); ''')
#
#    # create table stage SR-cards;
#    c.execute(''' CREATE TABLE IF NOT EXISTS stageSR (stgSR_ID integer PRIMARY KEY,
#        stgSR_cardD decimal(2,0) NOT NULL,
#        stgSR_chapterNumber decimal(2,0) NOT NULL,
#        stgSR_calcScore decimal(2,0) NOT NULL,
#        stgSR_sumScore decimal(2,0) NOT NULL
#        ); ''')
#
#    # create table stage SSR-cards;
#    c.execute(''' CREATE TABLE IF NOT EXISTS stageSSR (stgSSR_ID integer PRIMARY KEY,
#        stgSSR_cardD decimal(2,0) NOT NULL,
#        stgSSR_chapterNumber decimal(2,0) NOT NULL,
#        stgSSR_calcScore decimal(2,0) NOT NULL,
#        stgSSR_sumScore decimal(2,0) NOT NULL
#        ); ''')
#
#    # create table R cards;
#    c.execute('''create table if not exists
#        R(r_id integer PRIMARY KEY,
#        r_name char(25) not null,
#        r_level decimal(2,0) not null,
#        r_star decimal(2,0) not null,
#        r_creativity decimal(2,0) not null,
#        r_decisionMaking decimal(2,0) not null,
#        r_affinity decimal(2,0) not null,
#        r_execution decimal(2,0) not null,
#        r_upgrade bit default 'FALSE' not null,
#        r_chid integer not null
#        )''')
#
#    # create table SR cards;
#    c.execute('''create table if not exists
#        SR(sr_id integer PRIMARY KEY,
#        sr_name char(25) not null,
#        sr_level decimal(2,0) not null,
#        sr_star decimal(2,0) not null,
#        sr_creativity decimal(2,0) not null,
#        sr_decisionMaking decimal(2,0) not null,
#        sr_affinity decimal(2,0) not null,
#        sr_execution decimal(2,0) not null,
#        sr_upgrade bit default 'FALSE' not null,
#        sr_chid integer not null
#        )''')
#
#    # create table SSR cards;
#    c.execute('''create table if not exists
#        SSR(ssr_id integer PRIMARY KEY,
#        ssr_name char(25) not null,
#        ssr_level decimal(2,0) not null,
#        ssr_star decimal(2,0) not null,
#        ssr_creativity decimal(2,0) not null,
#        ssr_decisionMaking decimal(2,0) not null,
#        ssr_affinity decimal(2,0) not null,
#        ssr_execution decimal(2,0) not null,
#        ssr_upgrade bit default 'FALSE' not null,
#        ssr_chid integer not null
#        )''')
#
#    # create table characters;
#    c.execute('''create table if not exists
#        Characters(ch_id integer PRIMARY KEY,
#        ch_name char(25) not null)''')
#
## insert characters;
#def insertC(c, conn):
#
#    name = [("MO XU",),
#            ("QI BAI",),
#            ("ZEYAN LI",),
#            ("QILUO ZHOU",),
#            ]
#
#    c.executemany('INSERT INTO Characters(ch_name) VALUES(?)', name)
#    conn.commit()


def disc(conn):
    conn.close()

if __name__ == '__main__':
    main()
