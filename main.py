from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, URL, Email
from mail import Message


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sodeffjed179'
Bootstrap(app)

class Leieform(FlaskForm):
    email = StringField('Epost', validators=[DataRequired(), Email()])
    days = SelectField('Hvor mange døgn vil du leie?', choices=["-", "1", "2", "3"], validators=[DataRequired()])
    date = DateField('Hvilken dato vil du leie fra?', format='%d-%m-%Y')
    address = StringField('Hvilken addresse skal vi levere til?', validators=[DataRequired()])
    submit = SubmitField("Bestill")


@app.route('/', methods=["POST", "GET"])
def home():
    form = Leieform()
    if request.method == "GET":
        email = None
        days = None
        date = None
        address = None
        message = None
        return render_template("index.html", form=form)
    else:
        email = None
        days = None
        date = None
        address = None
        message = None
        if request.method == "POST":
            email = request.form["email"]
            days = request.form["days"]
            date = request.form["date"]
            address = request.form["address"]
            message = request.form["message"]
            mail = Message()
            print(mail.my_password)
            mail.send_self(email, days, date, address, message)
            mail.send_cus(email, days, date, address, message)
            return render_template("index.html", form=form, email=email, days=days,
                                   date=date, address=address, message=message)


if __name__ == "__main__":
    app.run(debug=True)