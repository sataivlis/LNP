import sqlite3

def main():
    conn = sqlite3.connect('lnp.db')
    c  = conn.cursor()
    print ('Welcome to Love and Producer Calcualtor!')
    id = getCompany(c,conn)
    if id == -1:
        print('The company does not exit, Calculator breaks')
        disc(conn)
    print (id)
#id = 1
    cardDeck = list()
    cardDeck = getCards(c)
    
    insertIntoUserDeck(c,conn,cardDeck,id)
    
    disc(conn)

def getCompany(c,conn):
    print ('Do you want to contine or exit?')
    ex = input ('Type ''e'' for exit, type ''c'' for contuinue: ')
    
    while (ex != 'e'):
        if ex == 'c':
  
            print ('Are you a new user?')
            inp = input ('Y/N: ')
            print (type(inp))
            print('int',inp)
            print ('Please Input your Company Name: ')
            comN = input ('Company Name:')
            print (type(inp))
            print('comN',comN)
            cId = -1
            
            print(inp == 'Y')

            if inp == 'Y' :
                comC = input ('Company Creativity: ')
                comD = input ('Company DecisionMaking: ')
                comA = input ('Company Affinity: ')
                comE = input ('Company Execution: ')

                if not (comC.isdigit() and comD.isdigit() and comA.isdigit() and comE.isdigit()):
                    print ('invaild')
                cData = (comN,comC,comD,comA,comE)
                c.execute ("insert into company (c_name,c_creativity,c_decisionMaking,c_affinity,c_execution) values (?,?,?,?,?)",cData )
                conn.commit()
                c.execute ("select c_ID from company where c_name = :comN",{"comN":comN})
                cId = c.fetchone()
                if cId == None:
                    print('error')
                else:
                    print(cId[0])

            if inp == 'N' :
                c.execute ("select c_ID from company where c_name = :comN",{"comN":comN})
                cId = c.fetchone()
                if cId == None:
                    print('error')
                else:
                    print(cId[0])
        else:
            print ('Wrong key')
        ex = input ('Type ''e'' for exit, type ''c'' for contuinue: ')
        
    if cId != None:
        cId = cId[0]
        return cId
    else:
        cId = -1
        return cId

def getCards(c):
    print('Please input the cards that you own')
    condition = True
    cardValidate = True
    cards = list()
    res = list()
    while (condition == True):
    

        cardChname = input ('Charater name [MO XU, QI BAI,ZEYAN LI,QILUO ZHOU]: ')
        
        if cardChname in ('MO XU', 'QI BAI','ZEYAN LI','QILUO ZHOU'):
        
            cardRare = input ('Rareality of the card [R,SR,SSR]: ')
            
            if cardRare in ('R','SR','SSR'):
   
                i = c.execute ("select ch_id from Characters where ch_name = :ch",{"ch":cardChname})
                i = c.fetchone()
                i = i[0]

                if cardRare == 'R':
                    c.execute("select r_name from R where r_chid = :id",{"id":i})
                    re = c.fetchall()
                    for r in re:
                        res.append(r[0])
                    print ('The name of cards ' ,res )
                    card = input ('Please choose: ')
                    if card in res:
                        cardValidate = True
                        c.execute("select * from R where r_name = :card",{"card":card})
                        cardInfo = c.fetchone()
                        print('cardInfo',cardInfo)

                    else:
                        cardValidate = False
                        print('error')
            
                if cardRare == 'SR':
                    c.execute("select sr_name from SR where sr_chid = :id",{"id":i})
                    re = c.fetchall()
                    #print(re)
                    for r in re:
                        res.append(r[0])
                    print ('The name of cards ' ,res )
                    card = input ('Please choose: ')
                    if card in res:
                        cardValidate = True
                        c.execute("select * from SR where sr_name = :card",{"card":card})
                        cardInfo = c.fetchone()
                        print('cardInfo',cardInfo)
                    else:
                        cardValidate = False
                        print('error')

                if cardRare == 'SSR':
                    c.execute("select ssr_name from SSR where ssr_chid = :id",{"id":i})
                    re = c.fetchall()
                    for r in re:
                        res.append(r[0])
                    print ('The name of cards ' ,res )
                    card = input ('Please choose: ')
                    if card in res:
                        cardValidate = True
                        c.execute("select * from SSR where ssr_name = :card",{"card":card})
                        cardInfo = c.fetchone()
                        print('cardInfo',cardInfo)
                    else:
                        cardValidate = False
                        print('error')

                if cardValidate == True:
                    cards.append(cardInfo)

                for ca in range(len(cards)):
                    print (ca, str(cards[ca])[1:-1])
                d = input ('Do you want to delete any wrong info card? (Y/N): ')
                while (d == 'Y'):
                    cindex = input ('Which one do you want to delete, please enter index: ')
                    cindex = int(cindex)
                    del cards[cindex]
                    for ca in range(len(cards)):
                        print (ca, str(cards[ca])[1:-1])
                    d = input ('Do you want to delete any wrong info card? (Y/N): ')
                    
                
            else:
                print ('Invalid Rareality')
        else:
            print ('Wrong name')
                        
        
        check = input ('one more card? (y/n): ')
        if check == 'y':
            condition = True
        else:
            condition = False
    for ca in range(len(cards)):
        print (ca, str(cards[ca])[1:-1])
    
    return cards

def insertIntoUserDeck(c,conn,cardDeck,id):
    print(cardDeck)
    level = 37
    star = 5









    
    
    
    





def disc(conn):
    conn.close()



if __name__ == '__main__':
    main()
