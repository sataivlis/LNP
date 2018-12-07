import sqlite3

def main():
    conn = sqlite3.connect('lnp.db')
    c  = conn.cursor()
    print ('Welcome to Love and Producer Calcualtor!')
    #need to consider the case user exit
    id,inp = getCompany(c,conn)
    if id == -1:
        print('The company does not exit, Calculator breaks')
        disc(conn)
        return 0
#    print (id)

    #id = 1
    cardDeck = list()
    if inp=='Y':
        cardDeck = getCards(c,conn,id)
    else:
#        print('works')
        oldUserCard(c,conn,id)
    chap = chooseChapter (c,conn)
#    print ('chap',chap)
    if chap == None:
        print('Invalid chapter number ')
        cha = input ('Do you want to go back (y) or exit the program (n)? (y/n): ')
        if cha == 'y':
            chap = chooseChapter (c,conn)
        else:
            disc(conn)
            return 0
#    print ('id',id)
#chap = '1.3'
    calBestScore(c,chap,id)


    print ('See you Next Time! Hope you get a lot of SSRs ٩̋(๑˃́ꇴ˂̀๑)')
    
    
    
    #need to consider
    
    #insertIntoUserDeck(c,conn,cardDeck,id)
    
    disc(conn)

def getCompany(c,conn):
    print ('Do you want to contine or exit?')
    ex = input ('Type ''e'' for exit, type ''c'' for contuinue: ')
    cId = None
    inp = None
    while (ex != 'e'):
        if ex == 'c':
  
            print ('Are you a new user?')
            inp = input ('Y/N: ')
#            print (type(inp))
#            print('int',inp)
            print ('Please Input your Company Name: ')
            comN = input ('Company Name:')
#            print (type(inp))
#            print('comN',comN)
            cId = -1
            
#            print(inp == 'Y')

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
#                else:
#                    print(cId[0])

            if inp == 'N' :
                c.execute ("select c_ID from company where c_name = :comN",{"comN":comN})
                cId = c.fetchone()
                if cId == None:
                    print('error')
#                else:
#                    print(cId[0])
                print('These are the cards that you have ')
                c.execute ("select ud_cardName, ud_cardLevel,ud_cardStar,ud_cardCreativity,ud_cardDecision,ud_cardAffinity,ud_cardExecution,ud_cardUpgrade from UserDeck where ud_cID = :id",{"id":cId[0]})
                result = c.fetchall()
                for r in range(len(result)):
                    print (r, str(result[r])[1:-1])
                    
    
        else:
            print ('Wrong key')
        ex = 'e'

        
    if cId != None:
        cId = cId[0]
        return (cId,inp)
    else:
        cId = -1
        return (cId,inp)


#for new user

def getCards(c,conn,id):
    print('Please input the cards that you own')
    condition = True
    cardValidate = True
    prCards = list()
    cards = list()
    res = list()
    w = input ('If you do not have card want to input, please type ''no'' or else press any key to continue: ')
    if w == 'no':
        return 0
    while (condition == True):
    
    #input level and star, 0.level star = 100 upgrade + 0.45%
    #fix wrong name statement
    
        cardChname = input ('Charater name [MO XU, QI BAI,ZEYAN LI,QILUO ZHOU]: ')
        
        if cardChname in ('MO XU', 'QI BAI','ZEYAN LI','QILUO ZHOU'):
        
            cardRare = input ('Rareality of the card [R,SR,SSR]: ')
            
            if cardRare in ('R','SR','SSR'):
   
                i = c.execute ("select ch_id from Characters where ch_name = :ch",{"ch":cardChname})
                i = c.fetchone()
                i = i[0]
                
                c.execute ("select rare_id from Rarity where rare_type = :r",{"r":cardRare})
                r = c.fetchone()
                r = r[0]

                if cardRare == 'R':
                    c.execute("select c_name from Cards where c_chid = :i and c_rareid = :r",{"i":i,"r":r})
                    re = c.fetchall()
                    for rr in re:
                        res.append(rr[0])
                    print ('The name of cards ' ,res )
                    card = input ('Please choose: ')
                    if card in res:
                        cardValidate = True
                        c.execute("select c_name,c_level,c_star,c_creativity,c_decisionMaking,c_affinity,c_execution,c_upgrade,c_chid,c_rareid from Cards where c_name = :card",{"card":card})
                        cardInfo = c.fetchone()
#                        print ('',cardInfo)

                        level = input ('Plese Input Card Level: ')
                        
                        #need a case with no intger number
                        level = int (level)
                        
            
                        if level in range (1,41):
                            star = input ('Pleas input number of Card Stars ')
                            star = int(star)
                            if star in range (1,6):
                                upgrade = input ('Is it upgraded? (TRUE/FALSE)')
                                if upgrade == 'TRUE' or 'FALSE':
                                    if upgrade == 'TRUE':
                                        if level == 40 and star == 5:
                                            print('full card cardInfo',cardInfo)
                                        else:
                                            cr = cardInfo[3] * 1.45 + (cardInfo[3]*(level/40) - (cardInfo[3] - star *0.1))
                                            de = cardInfo[4] * 1.45 + (cardInfo[4]*(level/40) - (cardInfo[4] - star *0.1))
                                            af = cardInfo[5] * 1.45 + (cardInfo[5]*(level/40) - (cardInfo[5] - star *0.1))
                                            ex = cardInfo[6] * 1.45 + (cardInfo[6]*(level/40) - (cardInfo[6] - star *0.1))
                                            cr = int(cr)
                                            de = int(de)
                                            af = int(af)
                                            ex = int(ex)
                                            cardInfo = (card,level,star,cr,de,af,ex,upgrade,i,r)
                                            printcard = (card,level,star,cr,de,af,ex,upgrade,cardChname,cardRare)
                                #print(af)
                                    else:
                                        cr =  (cardInfo[3]*(level/40)  + star *0.1)
                                        de =  (cardInfo[4]*(level/40) + star *0.1)
                                        af =  (cardInfo[5]*(level/40) + star *0.1)
                                        ex =  (cardInfo[6]*(level/40) + star *0.1)
                                        cr = int(cr)
                                        de = int(de)
                                        af = int(af)
                                        ex = int(ex)
                                        cardInfo = (card,level,star,cr,de,af,ex,upgrade,i,r)
                                        printcard = (card,level,star,cr,de,af,ex,upgrade,cardChname,cardRare)
                        
                            else:
                                print ('wrong star: will choose card with full star and level')
                        else:
                            print ('wrong level: will choose card with full star and level')
                    else:
                        cardValidate = False
                        print('error')
            
                if cardRare == 'SR':
                    c.execute("select c_name from Cards where c_chid = :i and c_rareid = :r",{"i":i,"r":r})
                    re = c.fetchall()
                    #print(re)
                    for rr in re:
                        res.append(rr[0])
                    print ('The name of cards ' ,res )
                    card = input ('Please choose: ')


                    if card in res:
                        cardValidate = True
                        c.execute("select c_name,c_level,c_star,c_creativity,c_decisionMaking,c_affinity,c_execution,c_upgrade,c_chid,c_rareid from Cards where c_name = :card",{"card":card})
                        cardInfo = c.fetchone()
                        print('cardInfo',cardInfo)
                        level = input ('Plese Input Card Level: ')
                        level = int (level)
                        if level in range (1,51):
                            star = input ('Pleas input number of Card Stars ')
                            star = int(star)
                            if star in range (1,7):
                                upgrade = input ('Is it upgraded? (TRUE/FALSE)')
                                if upgrade == 'TRUE' or 'FALSE':
                                    if upgrade == 'TRUE':
                                        if level == 50 and star == 6:
                                            print('full card cardInfo',cardInfo)
                                        else:
                                            cr = cardInfo[3] * 1.45 + (cardInfo[3]*(level/50) - (cardInfo[3] - star *0.1))
                                            de = cardInfo[4] * 1.45 + (cardInfo[4]*(level/50) - (cardInfo[4] - star *0.1))
                                            af = cardInfo[5] * 1.45 + (cardInfo[5]*(level/50) - (cardInfo[5] - star *0.1))
                                            ex = cardInfo[6] * 1.45 + (cardInfo[6]*(level/50) - (cardInfo[6] - star *0.1))
                                            cr = int(cr)
                                            de = int(de)
                                            af = int(af)
                                            ex = int(ex)
                                            cardInfo = (card,level,star,cr,de,af,ex,upgrade,i,r)
                                            printcard = (card,level,star,cr,de,af,ex,upgrade,cardChname,cardRare)
                                            
                                            print(af)
                                    else:
                                        cr =  (cardInfo[3]*(level/50) +  star *0.1)
                                        de =  (cardInfo[4]*(level/50) + star *0.1)
                                        af =  (cardInfo[5]*(level/50) +  star *0.1)
                                        ex =  (cardInfo[6]*(level/50) + star *0.1)
                                        cr = int(cr)
                                        de = int(de)
                                        af = int(af)
                                        ex = int(ex)
                                        cardInfo = (card,level,star,cr,de,af,ex,upgrade,i,r)
                                        printcard = (card,level,star,cr,de,af,ex,upgrade,cardChname,cardRare)
                                else:
                                    cardValidate = False
                        

                            else:
                                print ('wrong star: will choose card with full star and level')
                            
                        else:
                            print ('wrong level: will choose card with full star and level')
                            
                    else:
                        cardValidate = False
                        print('error')

                if cardRare == 'SSR':
                    c.execute("select c_name from Cards where c_chid = :i and c_rareid = :r",{"i":i,"r":r})
                    re = c.fetchall()
                    for rr in re:
                        res.append(rr[0])
                    print ('The name of cards ' ,res )
                    card = input ('Please choose: ')
                    if card in res:
                        cardValidate = True
                        c.execute("select c_name,c_level,c_star,c_creativity,c_decisionMaking,c_affinity,c_execution,c_upgrade,c_chid,c_rareid from Cards where c_name = :card",{"card":card})
                        cardInfo = c.fetchone()
                        print('cardInfo',cardInfo)
                        level = input ('Plese Input Card Level: ')
                        level = int (level)
                                
                        if level in range (1,61):
                            star = input ('Pleas input number of Card Stars ')
                            star = int(star)
                            if star in range (1,8):
                                upgrade = input ('Is it upgraded? (TRUE/FALSE)')
                                
                                if upgrade == 'TRUE' or 'FALSE':
                                
                                    if upgrade == 'TRUE':
                                        if level == 60 and star == 7:
                                            print('full card cardInfo',cardInfo)
                                        else:
                                            cr = cardInfo[3] * 1.45 + (cardInfo[3]*(level/60) - (cardInfo[3] - star *0.1))
                                            de = cardInfo[4] * 1.45 + (cardInfo[4]*(level/60) - (cardInfo[4] - star *0.1))
                                            af = cardInfo[5] * 1.45 + (cardInfo[5]*(level/60) - (cardInfo[5] - star *0.1))
                                            ex = cardInfo[6] * 1.45 + (cardInfo[6]*(level/60) - (cardInfo[6] - star *0.1))
                                            cr = int(cr)
                                            de = int(de)
                                            af = int(af)
                                            ex = int(ex)
                                            cardInfo = (card,level,star,cr,de,af,ex,upgrade,i,r)
                                            printcard = (card,level,star,cr,de,af,ex,upgrade,cardChname,cardRare)
                                    else:
                                        cr =  (cardInfo[3]*(level/60) - (cardInfo[3] - star *0.1))
                                        de =  (cardInfo[4]*(level/60) - (cardInfo[4] - star *0.1))
                                        af =  (cardInfo[5]*(level/60) - (cardInfo[5] - star *0.1))
                                        ex =  (cardInfo[6]*(level/60) - (cardInfo[6] - star *0.1))
                                        cr = int(cr)
                                        de = int(de)
                                        af = int(af)
                                        ex = int(ex)
                                        cardInfo = (card,level,star,cr,de,af,ex,upgrade,i,r)
                                        printcard = (card,level,star,cr,de,af,ex,upgrade,cardChname,cardRare)
                                else:
                                    cardValidate = False
                                                
                                        
                            else:
                                print ('wrong star: will choose card with full star and level')
                        else:
                            print ('wrong level: will choose card with full star and level')
                    else:
                        cardValidate = False
                        print('error')
                
                

                if cardValidate == True:
                    cards.append(cardInfo)
                    prCards.append(printcard)
            #bug?????
                for ca in range(len(prCards)):
                    print (ca, str(prCards[ca])[1:-1])

                d = input ('Do you want to delete any wrong info card? (Y/N): ')
                #bug???
                while (d == 'Y'):
                    cindex = input ('Which one do you want to delete, please enter index: ')
                    cindex = int(cindex)
                    print (cards[cindex])
                    for ca in range(len(cards)):
                        print (ca, str(cards[ca])[1:-1])
                    d = input ('Do you want to delete any wrong info card? (Y/N): ')
                    
                
            else:
                print ('Invalid Rareality')
        else:
            print ('Wrong name')
                        
        
        check = input ('one more card? (y/n): ')
        res = list()
        if check == 'y':
            condition = True
        else:
            condition = False
                
    if cards != None:
        for ca in range(len(cards)):
            print (ca, str(cards[ca])[1:-1])
        insertIntoUserDeck(c,conn,cards,id)

    
    return cards

def insertIntoUserDeck(c,conn,cards,id):
    newcards = list()
#    print(cards)
    chid = list
    chid = (id,)
    leng = len(cards)
#    print (leng)

    for car in cards:
        newcards = (chid + car)
        c.execute("select ud_cardName from UserDeck where ud_cardName = :name and ud_cID = :id",{"name":newcards[1],"id":id})
        n = c.fetchone()
        print ('n',n)
        if n == None:
            sql = "insert into UserDeck values (?,?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql,newcards)
            conn.commit()
        else:
            print ('already have '+ newcards[1])


    print (newcards)

def oldUserCard(c,conn,id):
    choice = input('Do you want to edit your table? (1:add cards, 2: delete cards, 3: keep the same) Please select: ')
    while (choice == '1' or choice == '2' ):
        if choice == '1':
            getCards(c,conn,id)
        elif choice == '2':
            n = input ('Please choose the card name that you want to delete: ')
            c.execute ("delete from UserDeck where ud_cardName = :n",{"n":n})
            conn.commit()
        c.execute ("select ud_cardName, ud_cardLevel,ud_cardStar,ud_cardCreativity,ud_cardDecision,ud_cardAffinity,ud_cardExecution,ud_cardUpgrade from UserDeck where ud_cID = :id",{"id":id})

        result = c.fetchall()
        for r in range(len(result)):
            print (r, str(result[r])[1:-1])
        choice = input('Do you want to edit your table? (1:add cards, 2: delete cards, 3: keep the same) Please select: ')







def chooseChapter (c,conn):
    
    comN = list()
    c.execute("select s_chapterNumber from stage")
    
    com = c.fetchall()
    print (com)
#    if com != None:
    for co in com:
        comN.append(str(co[0]))
#    else:
#        print ('error')
    print ('Avaliable Chapter: ',comN)
    chap = input ('Please select one: ')

    chap = str(chap)
#    print ('chap',chap)
    if chap in comN:
        
        return chap
    else:
        print ('Not Available')

def calBestScore(c,chap,id):
    num = input ('Please choose how many cards you want to see to pass the chapter? (1: 1, 2: 2, 3: 3, 4: exit the program): ')
    
    print ('Begining Calculation ..................................... ...(｡•ˇ‸ˇ•｡) ... ')
    cRe = list()
    state = True
    while (num == '1' or num == '2' or num == '3'):
        
    
        if num == '1':
            c.execute("SELECT i.ud_cardName FROM UserDeck i, stage, stageCompany WHERE (((s_percentageA * i.ud_cardAffinity) + (s_percentageC * i.ud_cardCreativity) +(s_percentageDM * i.ud_cardDecision) + (s_percentageE * i.ud_cardExecution)))>= s_requireScore AND i.ud_cID = sc_companyID  AND sc_chapterNumber = s_chapterNumber AND s_chapterNumber = :chap and i.ud_cID = :id group by i.ud_cardName ",{"id":id,"chap":chap})
            result = c.fetchall()
            if len(result) == 0:
                print ('No cards combination can do it ')
            elif len(result[0]) == 1:
                print ('The Best Results are: ',result[0][0] )
    
    
        if num == '2':
            c.execute("SELECT i.ud_cardName,j.ud_cardName FROM UserDeck i, stage, stageCompany,UserDeck j WHERE (((s_percentageA * i.ud_cardAffinity) + (s_percentageC * i.ud_cardCreativity) +(s_percentageDM * i.ud_cardDecision) + (s_percentageE * i.ud_cardExecution))+((s_percentageA * j.ud_cardAffinity) +(s_percentageC * j.ud_cardCreativity) +(s_percentageDM * j.ud_cardDecision) +(s_percentageE * j.ud_cardExecution)))>= s_requireScore AND i.ud_cID = sc_companyID  and i.ud_cID = j.ud_cID AND sc_chapterNumber = s_chapterNumber and i.ud_cardName <> j.ud_cardName AND s_chapterNumber = :chap and i.ud_cID = :id group by i.ud_cardName and j.ud_cardName ",{"id":id,"chap":chap})
            result = c.fetchall()
            if len(result) == 0:
                print ('No cards combination can do it ')

            elif len(result[0]) == 2:
                print ('The Best Three Results are: ',result[0][0] + ', ', result[0][1] )
            elif len(result[0]) == 1:
                print ('There are no more than one card. The Best Results are: ',result[0][0] )
                    
        if num == '3':

    
            c.execute("SELECT i.ud_cardName,j.ud_cardName,k.ud_cardName FROM UserDeck i, stage, stageCompany,UserDeck j,UserDeck k WHERE (((s_percentageA * i.ud_cardAffinity) + (s_percentageC * i.ud_cardCreativity) +(s_percentageDM * i.ud_cardDecision) + (s_percentageE * i.ud_cardExecution))+((s_percentageA * j.ud_cardAffinity) +(s_percentageC * j.ud_cardCreativity) +(s_percentageDM * j.ud_cardDecision) +(s_percentageE * j.ud_cardExecution))+((s_percentageA * k.ud_cardAffinity) +(s_percentageC * k.ud_cardCreativity) +(s_percentageDM * k.ud_cardDecision) +(s_percentageE * k.ud_cardExecution)))>= s_requireScore AND i.ud_cID = sc_companyID  and i.ud_cID = j.ud_cID and j.ud_cID = k.ud_cID AND sc_chapterNumber = s_chapterNumber and i.ud_cardName <> j.ud_cardName and j.ud_cardName <> k.ud_cardName and i.ud_cardName <> k.ud_cardName AND s_chapterNumber = :chap and i.ud_cID = :id group by i.ud_cardName and j.ud_cardName and k.ud_cardName",{"id":id,"chap":chap})
        #
            result = c.fetchall()
            
#            print ('result3',result )
#            print (len(result) == None)

        
#            print (result)
        #    for r in result:
        #        cRe.append(r)


            if len(result) == 0:
                print ('No cards combination can do it ')
            elif len(result[0]) == 3:
                print ('The Best Three Results are: ',result[0][0] + ', ', result[0][1] + ', ', result[0][2])
            elif len(result[0]) == 2:
                print ('There are no more than two cards. The Best Results are: ',result[0][0] + ', ', result[0][1] )
            elif len(result[0]) == 1:
                print ('There are no more than one card. The Best Results are: ',result[0][0] )



        num = input ('Please choose how many cards you want to see to pass the chapter? (1: 1, 2: 2, 3: 3, 4: exit the progroam ): ')
#        print ('Begining Calculation ..................................... ')
#        if num != '1' or num != '1' or num != '1' :
#            state = False




    



#    cRe = list()
#    c.execute("select ud_cardName,ud_cardCreativity,ud_cardDecision,ud_cardAffinity,ud_cardExecution from UserDeck where ud_cID = :id",{"id":id})
#    result = c.fetchall()
#    c.execute("select s_requireScore,s_percentageC,s_percentageDM,s_percentageA,s_percentageE from stage where s_chapterNumber = :chap",{"chap":chap})
#    comRe = c.fetchone()
#    s_requireScore = comRe[0]
#    s_percentageC = comRe[1]
#    s_percentageDM = comRe[2]
#    s_percentageA = comRe[3]
#    s_percentageE = comRe[4]
#    print (s_percentageC)
#    print (result)
#    if result != None:
#        if len(result) >=3:
#            for i in result:
#                j =i+1
#                for j in result:
#                    z = i+2
#                    for z in result:
#                        ((s_percentageA * i[3]) +
#                         (s_percentageC * i[1]) +
#                         (s_percentageDM * i[2]) +
#                         (s_percentageE * i[4]) +
#                         (s_percentageA * j[3]) +
#                         (s_percentageC * j[1]) +
#                         (s_percentageDM * j[2]) +
#                         (s_percentageE * j[4]) +
#                         (s_percentageA * z[3]) +
#                         (s_percentageC * z[1]) +
#                         (s_percentageDM * z[2]) +
#                         (s_percentageE * z[4])
#                         ) >= s_requireScore
#
#            print (cRe)



    



#    if chap in comN:
#        sql = "select ud_cardCreativity+ud_cardDecision+ud_cardAffinity+ud_cardExecution from UserDeck group by ud_cardName"


def disc(conn):
    conn.close()



if __name__ == '__main__':
    main()
