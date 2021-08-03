from flask import render_template, url_for, flash, redirect, request
from flaskwebsite import app, db
from flaskwebsite.forms import ContactForm
from flaskwebsite.model import User
from scrape import Forex_list
import ast

# root page = "/"
@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        # return redirect(url_for("pairinfo"), Forex_list)
        return render_template("home.html", Forex_list=Forex_list)
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        user_inquiry = User(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(user_inquiry)
        db.session.commit()
        flash("Message successfully submitted!", "success")
        return redirect(url_for("home"))
    return render_template("contact.html", form=form)

@app.route("/pairinfo", methods=["GET", "POST"])
def pairinfo():
    try:
        select = request.form.get("Pairs", default=None)
        d_select = ast.literal_eval(select)    #return str(select)
        return render_template("pairinfo.html", d_select=d_select)
    except SyntaxError:
        return str("Error: \"Pair Name\" not a valid option. Please return to home page.")

@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html", Forex_list=Forex_list)

# Test page for select drop down menu for redirect to pairinfo()
@app.route("/selectdirect", methods=["GET", "POST"])
def selectdirect():
    return render_template("selectredirect.html", Forex_list=Forex_list)