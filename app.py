from flask import *

app=Flask(__name__)



@app.route('/login',methods = ['POST'])
def login():
    uname=request.form['uname']
    passwrd=request.form['pass']
    if uname=="basha" and passwrd=="bhai":
        return "welcome %s" %uname
    else:
        return "soory try agai %s" %uname



if __name__=='__main__':
    app.run(debug=True)