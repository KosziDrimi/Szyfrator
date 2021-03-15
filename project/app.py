import os
from flask import Flask, render_template, url_for, flash, redirect
from forms import EnquiryForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_mail import Mail, Message


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#mail = Mail(app)

db = SQLAlchemy(app)
Migrate(app,db)


class Enquiry(db.Model):
    
    __tablename__ = 'enquiries'
    
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String)
    method = db.Column(db.String)
    
    def __init__(self, word, method):
        self.word = word
        self.method = method


@app.route('/', methods=['GET', 'POST'])
def index():
   
    form = EnquiryForm()

    if form.validate_on_submit():
        word = form.word.data
        method = form.method.data
        
        enq = Enquiry(word, method)
        db.session.add(enq)
        db.session.commit()
        
    
        if enq.method == 'gaderypoluki':
    
            gaderypoluki = {'g': 'a', 'd': 'e', 'r': 'y', 'p': 'o', 'l': 'u', 'k': 'i'} 
            gaderypoluki_inv = {val: key for key, val in gaderypoluki.items()}
        
            result = ''    
            for char in enq.word:
                if char in gaderypoluki.keys():
                    result += gaderypoluki[char]
                elif char in gaderypoluki_inv.keys():
                    result += gaderypoluki_inv[char]
                else:
                    result += char
                    
            return render_template('action.html', result=result, enq=enq, form=form)    
            
        
        elif enq.method == 'politykarenu':
        
            politykarenu = {'p': 'o', 'l': 'i', 't': 'y', 'k': 'a', 'r': 'e', 'n': 'u'} 
            politykarenu_inv = {val: key for key, val in politykarenu.items()}
        
            result = ''    
            for char in enq.word:
                if char in politykarenu.keys():
                    result += politykarenu[char]
                elif char in politykarenu_inv.keys():
                    result += politykarenu_inv[char]
                else:
                    result += char
                    
            return render_template('action.html', result=result, enq=enq, form=form)    
    
    
        else:
            
            gaderypoluki = {'g': 'a', 'd': 'e', 'r': 'y', 'p': 'o', 'l': 'u', 'k': 'i'} 
            gaderypoluki_inv = {val: key for key, val in gaderypoluki.items()}
        
            result_gad = ''    
            for char in enq.word:
                if char in gaderypoluki.keys():
                    result_gad += gaderypoluki[char]
                elif char in gaderypoluki_inv.keys():
                    result_gad += gaderypoluki_inv[char]
                else:
                    result_gad += char
            
            politykarenu = {'p': 'o', 'l': 'i', 't': 'y', 'k': 'a', 'r': 'e', 'n': 'u'} 
            politykarenu_inv = {val: key for key, val in politykarenu.items()}
        
            result_pol = ''    
            for char in enq.word:
                if char in politykarenu.keys():
                    result_pol += politykarenu[char]
                elif char in politykarenu_inv.keys():
                    result_pol += politykarenu_inv[char]
                else:
                    result_pol += char
            
            return render_template('action.html', result_gad=result_gad, 
                               result_pol=result_pol, enq=enq, form=form) 


    return render_template('main.html', form=form)  


if __name__ == '__main__':
    app.run(debug=True)
    
