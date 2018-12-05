from flask import Flask, render_template
import sqlite3
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask import request

app = Flask(__name__)



@app.route('/')
def hello_world():


    return render_template('index.html')

@app.route('/myCards', methods = ['GET','POST'])
def cards():
    print("myCards endpoint called!!");
    conn = sqlite3.connect('lnp.db')
    c  = conn.cursor()
    #'select r_name from R order by LOWER(r_name)'

    c.execute('select ch_name from Characters ')
    resultCh = c.fetchall()

    return render_template('cards.html', resultCh = resultCh)
    #return render_template('creativity.html',re = re)
    #print ('r',r)

    conn.close()

@app.route('/myCards/<string:id>/<string:rare>', methods = ['GET', 'POST'])
def cards_id(id=None, rare=None):
    conn = sqlite3.connect('lnp.db')
    c  = conn.cursor()

    print("THE ID THAT YOU GOT IS: ", id)
    print("tHE RARE THAT YOU GOT IS: ", rare)

    # id = session.get('id');
    # print(id)

    # ch = "QI BAI"
    ch = id
    c.execute('select ch_id from Characters where ch_name = :ch',{'ch':ch})
    id = c.fetchone()

    id = id[0]

    c.execute('select r_name from R where r_chid = :id',{'id':id})
    re = c.fetchall()

    # if request.method == 'POST':
        #ch = request.form['CH']

    rare = request.form.get('rare')
    #return render_template('creativity.html')
    #n = request.form['n']
    return render_template('creativity.html',re = re)

    # return '''<h1>The language value is: {}</h1>
    #          <h1>The value is: {}</h1>
    #          <h1>The value is: {}</h1>
    #          <h1>The re is: {}</h1>
    #         '''.format(id,ch,rare, re)
    # else:
    #     return "hello";




if __name__ == '__main__':
    app.run(debug = True)




        # if request.method == 'POST':
        #     rare = request.form['rare']
        #
        #     if request.method == 'POST':
        #         c.execute('select ch_id from Characters where ch_name = :ch',{'ch':ch})
        #         id = c.fetchone()
        #
        #         if rare == 'R':
        #             c.execute('select r_name from R where r_chid = :id',{'id':id})
        #             re = c.fetchall()
        #             n = request.form['n']
        #             return render_template('creativity.html',re = re)

        #return  '''<h1>The framework value is: {}</h1>'''.format(r)
        # c.execute('select r_creativity from R where r_name = :r',{'r':r})
        # crea = c.fetchall()
        #return render_template('creativity.html',crea = crea)

    # c.execute('select r_creativity from R where r_name = :x',{'x':x})
    # crea = c.fetchall()

    # c.execute('select sr_name from SR order by LOWER(sr_name)')
    # resultSR = c.fetchall()
    #
    # c.execute('select ssr_name from SSR order by LOWER(ssr_name)')
    # resultSSR = c.fetchall()

    #, resultSR = resultSR,
    #resultSSR = resultSSR
