from flask import Flask, render_template, redirect, request, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "a key"
a_list = []

@app.route("/")
def main():
    if not 'your_gold' in session:
        session['your_gold'] = 0

    return render_template('index.html')

@app.route('/process_money', methods = ["POST"])
def win_loose():
    global a_list
    building = request.form['building']
    gold = 0;
    if building == "farm":
        gold = random.randrange(10, 21)
    elif building == "cave":
        gold = random.randrange(5, 10)
    elif building == "house":
        gold = random.randrange(2, 5)
    elif building == "cassino":
        gold = random.randrange(-50, 50)
    if not 'your_gold' in session:
        session['your_gold'] = 0
    else:
        session['your_gold'] += gold

    played = datetime.datetime.now().strftime("%H:%M")           
    session["activities"] = gold
    session["building"] = building
    a_list.append([session["building"],  session["activities"], played])
    session["aList"] = a_list
    return redirect("/")

@app.route("/reset")
def reset():
    global a_list
    session.clear()
    a_list = []
    

    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)