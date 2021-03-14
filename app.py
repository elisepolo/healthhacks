from flask import Flask, render_template, url_for, request
from datetime import datetime
from datetime import date
import requests
import random 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)

@app.route('/results', methods=["POST"])
def results():
    answer = request.form['answer']
    Birthdate = request.form.get("Birthdate")
    Birthday = datetime.strptime(Birthdate, '%Y-%m-%d')
    age = calculate_age(Birthday)
    today = date.today()

    if request.form.get("theItems") == "other":
        familyHistory = "Yes"
        familyAge = int(request.form.get("otherField"))
        if familyAge - 5 > age:
            familyMessage = "Begin scheduling a yearly mammogram when you're "+ str(familyAge - 5)
        else:
            familyMessage = "You should already begin scheduling mammograms"
    else:
        familyHistory = "No"
        if age < 40:
            familyMessage = "Schedule a yearly mammogram starting in "+ str(today.year + (40-age))


    if age < 21:
        message = "Schedule a pap smear in "+ str((today.year + 21-age))
    elif age >= 21 and age < 30:
        message = "You should schedule a pap smear every 1-3 years." 
    elif age >= 30 and age <65:
        message = "You should schedule a pap smear once every 5 years."
    else:
        message = "You don't need to schedule a pap smear."

    return render_template('results.html', checkage=message, history=familyMessage)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))