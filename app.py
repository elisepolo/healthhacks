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
            mammogramMessage = "Your family history of breast cancer means that you should begin getting mammogram screenings earlier than most. Mammograms are extremely important in detecting breast cancer."
        else:
            familyMessage = "You should already have begun scheduling yearly mammograms"
            mammogramMessage = "Your family history of breast cancer means that you should have already begun getting mammogram screenings. Mammograms are extremely important in detecting breast cancer."
    else:
        familyHistory = "No"
        if age < 40:
            familyMessage = "Schedule a yearly mammogram when you're 40, starting in "+ str(today.year + (40-age))
            mammogramMessage = "Mammograms are extremely important in detecting breast cancer, and involve getting x-rays at a radiologist."


    if age < 21:
        message = "Schedule a pap smear when you're 21, in "+ str((today.year + 21-age))
        gynoMessage = "While you should not schedule a gynecological visit unitl you are 21, a visit is reccomended if you have any concerns about your reproductive health or menstrual cycle."
    elif age >= 21 and age < 30:
        message = "You should schedule a pap smear every 1-3 years."
        gynoMessage = "A visit to the gynecologist is recommended for annual screening and any time a woman has concerns about symptoms such as pelvic, vulvar, and vaginal pain or abnormal bleeding from the uterus. A Pap smear is important in detecting cervical cancer, and involves collecting cells from your uterus."
    elif age >= 30 and age <65:
        message = "You should schedule a pap smear once every 5 years."
        gynoMessage = "A visit to the gynecologist is recommended for annual screening and any time a woman has concerns about symptoms such as pelvic, vulvar, and vaginal pain or abnormal bleeding from the uterus. A Pap smear is important in detecting cervical cancer, and involves collecting cells from your uterus."
    else:
        message = "You don't need to schedule a pap smear."
        gynoMessage = "Your age suggests that you do not need to get a pap smear."

    return render_template('results.html', checkage=message, history=familyMessage, first=mammogramMessage, second=gynoMessage)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))