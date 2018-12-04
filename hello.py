from flask import Flask, render_template
import sqlite3
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from flask import request

app = Flask(__name__)



@app.route('/')
def hello_world():

    conn = sqlite3.connect('lnp.db')
    c  = conn.cursor()

    c.execute('SELECT s_chapterNumber FROM stage')
    stages = c.fetchall()

    return render_template('index.html',stages = stages)

    conn.close()


@app.route('/myCards',methods = ['GET','POST'])
def cards():
    conn = sqlite3.connect('lnp.db')
    c  = conn.cursor()

    c.execute('select r_name from R order by LOWER(r_name)')
    resultR = c.fetchall()

    if request.method == 'POST':
        r = request.form['Submit']



    # c.execute('select r_creativity from R where r_name = :x',{'x':x})
    # crea = c.fetchall()

    # c.execute('select sr_name from SR order by LOWER(sr_name)')
    # resultSR = c.fetchall()
    #
    # c.execute('select ssr_name from SSR order by LOWER(ssr_name)')
    # resultSSR = c.fetchall()

    #, resultSR = resultSR,
    #resultSSR = resultSSR
    return render_template('cards.html',resultR = resultR)
    print ('r',r)

    conn.close()


if __name__ == '__main__':
    app.run(debug = True)
