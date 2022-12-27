from flask import Flask, render_template, request
from datetime import datetime as dt
import smtplib
import os

site_email = "site.phumelela@gmail.com"
password = os.environ.get("TOKEN")
my_email = os.environ.get("PRIVATE_EMAIL")

x = dt.now()

app = Flask(__name__)


@app.route("/")
def home():
    # Footer #
    year = x.year
    return render_template("Phumelela Site.html", year=year)


@app.route("/", methods=["POST"])
def receive_data():
    name = request.form["username"]
    email = request.form["email"]
    msg = request.form["textarea"]
    # return f"<h1>Name: {name},<br> Email: {email} <br><br> Message: {msg}</h1>"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=site_email, password=password)
        connection.sendmail(
            from_addr=site_email,
            to_addrs=my_email,
            msg=f"Subject: Mail from Website\n\nHi, my name is {name}.\n\n{msg}. You can contact me on: {email}."
        )
    return render_template("Phumelela Site.html", scroll='#contact_me_page')


@app.route("/projects")
def projects():
    # Footer #
    year = x.year
    return render_template("Projects.html", year=year)

if __name__ == "__main__":
    app.run(debug=True)
