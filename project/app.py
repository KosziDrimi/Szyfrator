import os
from flask import Flask, render_template, url_for, flash, redirect, make_response
from forms import EnquiryForm, EmailForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from methods import Szyfr, Gaderypoluki, Politykarenu 
import pdfkit


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')


db = SQLAlchemy(app)
Migrate(app,db)


class Enquiry(db.Model):
    
    __tablename__ = 'enquiries'
    
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String)
    method = db.Column(db.String)
    result_gad = db.Column(db.Text)
    result_pol = db.Column(db.Text)
    
    def __init__(self, word, method, result_gad=None, result_pol=None):
        self.word = word
        self.method = method
        self.result_gad = result_gad
        self.result_pol = result_pol
 

@app.route('/', methods=['GET', 'POST'])
def index():
   
    form = EnquiryForm()

    if form.validate_on_submit():
        word = form.word.data
        method = form.method.data
            
        if method == 'gaderypoluki':
    
            szyfr = Szyfr(Gaderypoluki())
            result_gad = szyfr.szyfrowanie(word)
            
            enq = Enquiry(word, method, result_gad)
            db.session.add(enq)
            db.session.commit()
            
            return render_template('action.html', enq=enq, form=form)    
        
        elif method == 'politykarenu':
        
            szyfr = Szyfr(Politykarenu())
            result_pol = szyfr.szyfrowanie(word)
            
            enq = Enquiry(word, method, result_pol)
            db.session.add(enq)
            db.session.commit()
                
            return render_template('action.html', enq=enq, form=form)    
        
        else:
            
           szyfr = Szyfr(Gaderypoluki())
           result_gad = szyfr.szyfrowanie(word) 
           szyfr.strategy = Politykarenu()
           result_pol = szyfr.szyfrowanie(word)     
           
           enq = Enquiry(word, method, result_gad, result_pol)
           db.session.add(enq)
           db.session.commit()
            
           return render_template('action.html', enq=enq, form=form)
        
    return render_template('main.html', form=form)  


@app.route('/<int:enq_id>')
def print_pdf(enq_id):
    enq = Enquiry.query.get(enq_id)
    rendered = render_template('pdf.html', enq=enq) 
    pdf = pdfkit.from_string(rendered, False, configuration=config)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response


 
if __name__ == '__main__':
    app.run(debug=True)
    