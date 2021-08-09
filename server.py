# localhost:5000 - have the template render the number of times the client has visited this site

# localhost:5000/destroy_session - Clear the session. Once cleared, redirect to the root.

# Create a new Flask project called counter

# Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.

# Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.

# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2

# NINJA BONUS: Add a Reset button to reset the counter

# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly

# SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, as well as the value of the counter, given the above functionality

# SENSEI BONUS: Decode the cookie information as shown in the video

from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)  
app.secret_key = 'hello'

@app.route('/')   
def index():
    if 'clicks' not in session:
            session['clicks'] = 0
    if 'counter' not in session:
            session['counter'] = 0
    if 'tracker' not in session:
            session['tracker'] = []
    return render_template("index.html", act=session['tracker'], len_act=len(session['tracker'])
)  

@app.route('/process_clicks', methods=["POST"])   
def clicks():
    time = datetime.now()
    time_string = time.strftime('%m/%d/%Y %H:%M:%S')
    x = request.form['which_form']
    if x == 'click' and session['counter'] < 15 and session['clicks'] < 500:
        session['x'] = x
        new_value = 1
        session['clicks'] += new_value
        session['counter'] += 1
        session['tracker'].append([new_value,x,time_string])
    if x == 'click2' and session['counter'] < 15 and session['clicks'] < 500:
        session['x'] = x
        new_value = 2
        session['clicks'] += new_value
        session['counter'] += 1
        session['tracker'].append([new_value,x,time_string])
    if x == 'refresh' and session['counter'] < 15 and session['clicks'] < 500:
        session['x'] = x
        new_value = 1
        session['clicks'] += new_value
        session['counter'] += 1
        session['tracker'].append([new_value,x,time_string])
    elif x == 'reset' or session['counter'] >= 15 or session['clicks'] > 500:
        session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)   

