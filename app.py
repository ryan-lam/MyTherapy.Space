from flask import Flask, redirect, url_for, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = "secret_key"

check ={"Ryan":[],
        "Jax":[],
        "Bob":[]}

login_fact = [
    "\"An initial surprise people tend to experience is a feeling of relief\" - Katrina Taylor", 
    "Therapy can be exciting and fascinating. One to two years of weekly therapy appears to be indicated for meaningful and lasting change to occur",
    "\"One of the best methods of preventative health care you can do for your mind and your body before problems get too big\" - Tara Fairbanks, Ph.D",
    "It is estimated that currently there are over 500 different types of therapies for mental health problems",
    "Even a few sessions with a therapist can lower the risk of suicide among at-risk patients",
    "People suffering from major depression are more likely to improve with a combination of therapy and medication, as opposed to just medication",
    "The benefits of the therapy continue to grow even after treatment has ended",
    "The effects of trauma can have physical symptoms that result in long term medical issues, including high blood pressure and cancer"
    ]

patient_accounts = {
    "Jax":"1234", 
    "Ryan":"1234",
    "Bob":"1234"
    }

doc_accounts = {
    "Doc1":"1234",
    "Doc2":"1234"
}

# Date (string)
# How was your day? (1-7)
# Energy level?  (1-7)
# Which of the follow tasks did you complete today? ("Yes" or "No")
# - Brushed teeth
# - Took a shower
# - Took a walk
# - Eat a nutritious meal
# - Did you get an adequate amount of sleep?
# Did you encounter any problems or inconveniences today? If so, how did you resolve it?(string answer)
# What interesting thing(s) did you do today? (string answer)
database = {
  "Ryan":{
    "date":["Feb 10", "Feb 11", "Feb 12", "Feb 13", "Feb 14", "Feb 15", "Feb 16", "Feb 17", "Feb 18", "Feb 19", "Feb 20", "Feb 21", "Feb 22", "Feb 23", "Feb 24", 
        "Feb 25", "Feb 26", "Feb 27", "Feb 28", "Mar 1", "Mar 2", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
    "how was your day": [3, 2, 3, 2, 7, 5, 3, 2, 1, 6, 6, 7, 7, 2, 1, 3, 6, 5, 7, 1, 2, 1, 7, 2, 6, 4, 1, 1, 4, 4],
    "tasks": {
            "brush teeth":['Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'], 
            "shower":['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No'], 
            "walk":['No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No'], 
            "meal":['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No'], 
            "sleep":['No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']},
    "problems_and_solutions":["Mar 9: I was sad during lunch because my friends were busy and I was lonely. I ended up going to the library to read and to pass the time",
                        "Feb 12: I was overwhelmed by my school work and was anxious on not finishing them. As a solution, I used the pomodoro technique to work diligently."]
    },

  "Jax":{
    "date":["Feb 10", "Feb 11", "Feb 12", "Feb 13", "Feb 14", "Feb 15", "Feb 16", "Feb 17", "Feb 18", "Feb 19", "Feb 20", "Feb 21", "Feb 22", "Feb 23", "Feb 24", 
        "Feb 25", "Feb 26", "Feb 27", "Feb 28", "Mar 1", "Mar 2", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
    "how was your day": [1, 1, 2, 3, 6, 3, 7, 4, 2, 1, 2, 2, 3, 5, 6, 3, 7, 5, 4, 3, 3, 7, 4, 2, 6, 7, 5, 3, 6, 5],
    "tasks": {
            "brush teeth":['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No'], 
            "shower":['Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes'], 
            "walk":['No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes'], 
            "meal":['Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No'], 
            "sleep":['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']},
    "problems_and_solutions":["Mar 6: I recently learned about Minecraft and it has helped distract me from using drugs. I'm worried that it's only a short-term fix for my problems",
                        "Feb 28: My girlfirend and I broke up and I started getting more and more depressed. I relapsed and starting doing drugs again even though I shouldn't"]
    

  },

  "Bob":{
    "date":["Feb 10", "Feb 11", "Feb 12", "Feb 13", "Feb 14", "Feb 15", "Feb 16", "Feb 17", "Feb 18", "Feb 19", "Feb 20", "Feb 21", "Feb 22", "Feb 23", "Feb 24", 
            "Feb 25", "Feb 26", "Feb 27", "Feb 28", "Mar 1", "Mar 2", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],    "how was your day": [2, 2, 4, 6, 7, 5, 5, 2, 3, 5, 4, 6, 5, 2, 3, 7, 7, 5, 7, 1, 1, 1, 4, 5, 6, 1, 5, 5, 4, 6],
    "how was you day": [7, 3, 6, 2, 5, 7, 5, 6, 5, 2, 6, 3, 7, 1, 2, 7, 1, 1, 3, 3, 4, 6, 5, 6, 7, 1, 1, 6, 6, 2],
    "tasks": {
            "brush teeth":['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes'], 
            "shower":['No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No'], 
            "walk":['No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'], 
            "meal":['No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No'], 
            "sleep":['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes']},
    "problems_and_solutions":["March 10: I got an A on my school essay! I'm very happy that my hard work resulted in a good grade",
                        "Feb 13: I went for a run in the park today and it helped me de-stress but made me stressed afterwards because I had less time to work on my school work",
                        "Feb 11: I was walking in the park today and I realized that going outside helped calm me down"]
  }
}

# currentGuy = "NoOne"
chartLength = 7


# INDEX
@app.route("/") #HOME BUTTON PRESSED
def home():
    return render_template("index.html")

# TOS PAGE
@app.route("/tos")
def tos():
    return render_template("tos.html")

# LOGIN PAGE
@app.route("/login")  #LOGIN PAGE
def login():
    n = random.randint(0,len(login_fact)-1)
    return render_template("login.html", loginfact=login_fact[n])


# LOGIN FUNCTION
@app.route("/loging", methods=['POST', 'GET']) #GOES TO DASHBOARD
def logging():

    if request.method == "POST":
        name = request.form["name"] #NAME OF LOGIN USER INPUTS
        password = request.form["password"] #PASSWORD OF LOGIN USER INPUTS
        session["patient_user_dashboard"] = name
        patient = name

        if patient in patient_accounts:
            problems_and_sol = database[patient]["problems_and_solutions"]
            last_14_days=database[patient]["date"][len(database[patient]["date"])- 14:]
            last_14_days_task =[database[patient]["tasks"]["brush teeth"][len(database[patient]["tasks"]["brush teeth"])-14:],
                                database[patient]["tasks"]["shower"][len(database[patient]["tasks"]["shower"])-14:],
                                database[patient]["tasks"]["walk"][len(database[patient]["tasks"]["walk"])-14:],
                                database[patient]["tasks"]["meal"][len(database[patient]["tasks"]["meal"])-14:],
                                database[patient]["tasks"]["sleep"][len(database[patient]["tasks"]["sleep"])-14:]]
        
        if name in patient_accounts and password == patient_accounts[name]:
            # global currentGuy
            # currentGuy = name
            global chartLength
            chartLength = 7
            x = database[patient]["date"][len(database[patient]["date"])- 7:]
            y = database[patient]["how was your day"][len(database[patient]["how was your day"])- 7:]
            return render_template("dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x, values=y, patient=name, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
        elif name in doc_accounts and password == doc_accounts[name]:
            session["patient_user_dashboard"] = "Bob"
            chartLength = 7
            x = database["Bob"]["date"][len(database["Bob"]["date"])- 7:]
            y = database["Bob"]["how was your day"][len(database["Bob"]["how was your day"])- 7:]
            problems_and_sol = database["Bob"]["problems_and_solutions"]
            last_14_days=database["Bob"]["date"][len(database["Bob"]["date"])- 14:]
            last_14_days_task =[database["Bob"]["tasks"]["brush teeth"][len(database["Bob"]["tasks"]["brush teeth"])-14:],
                                database["Bob"]["tasks"]["shower"][len(database["Bob"]["tasks"]["shower"])-14:],
                                database["Bob"]["tasks"]["walk"][len(database["Bob"]["tasks"]["walk"])-14:],
                                database["Bob"]["tasks"]["meal"][len(database["Bob"]["tasks"]["meal"])-14:],
                                database["Bob"]["tasks"]["sleep"][len(database["Bob"]["tasks"]["sleep"])-14:]]
            return render_template("doc-dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x, values=y, patient="Bob", task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
        else:
            n = random.randint(0,len(login_fact)-1)
            return render_template("login.html", loginmessage="False", loginfact=login_fact[n])


# GO TO DASHBOARD FUNC
@app.route("/dashboard", methods=['POST', 'GET'])  #LOGIN PAGE
def showChart():

    if "patient_user_dashboard" in session:
        patient = session["patient_user_dashboard"]


    # FUNC FOR GRAPH
    if request.method == 'POST':
        length = request.form["content"]

        # dont change this stuff there. its outta order bc I mixed x and y axis
        graph_x = database[patient]["date"]
        graph_y = database[patient]["how was your day"]
        problems_and_sol = database[patient]["problems_and_solutions"]
        last_14_days = database[patient]["date"][len(database[patient]["date"])- 14:]
        last_14_days_task =[database[patient]["tasks"]["brush teeth"][len(database[patient]["tasks"]["brush teeth"])-14:],
                            database[patient]["tasks"]["shower"][len(database[patient]["tasks"]["shower"])-14:],
                            database[patient]["tasks"]["walk"][len(database[patient]["tasks"]["walk"])-14:],
                            database[patient]["tasks"]["meal"][len(database[patient]["tasks"]["meal"])-14:],
                            database[patient]["tasks"]["sleep"][len(database[patient]["tasks"]["sleep"])-14:]]
        global chartLength
        if length == "30":  #IF 30 DAYS BUTTON PRESSED
            chartLength = 30
            x = graph_x[(len(graph_x)- 30):]
            y = graph_y[(len(graph_y)- 30):]
            return render_template('dashboard.html', graph_title='30 Day Mood Change', min=1, max=7, labels=x, values=y, patient=patient, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
        elif length == "14": #IF 14 DAYS BUTTON PRESSED
            chartLength = 14
            x = graph_x[(len(graph_x)- 14):]
            y = graph_y[(len(graph_y)- 14):]
            return render_template('dashboard.html', graph_title='14 Day Mood Change', min=1, max=7, labels=x, values=y, patient=patient, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
        else: #length == "7": (IF 7 DAYS BUTTON PRESSED)
            chartLength = 7
            x = graph_x[(len(graph_x)- 7):]
            y = graph_y[(len(graph_y)- 7):]
            return render_template("dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x, values=y, patient=patient, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
    else:
        x = graph_x[(len(graph_x)- 7):]
        y = graph_x[(len(graph_x)- 7):]
        return render_template("dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x,  values=y, patient=patient, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
    # return render_template("dashboard.html", labels = labels, values = values, max=7, min=1)

@app.route("/dashboardcheckin", methods=['POST', 'GET'])  #CHECKIN FROM PATIENT
def checkIn():
    patient = session["patient_user_dashboard"]
    x = database[patient]["date"][len(database[patient]["date"])- 7:]
    y = database[patient]["how was your day"][len(database[patient]["how was your day"])- 7:]
    problems_and_sol = database[patient]["problems_and_solutions"]
    last_14_days=database[patient]["date"][len(database[patient]["date"])- 14:]
    last_14_days_task =[database[patient]["tasks"]["brush teeth"][len(database[patient]["tasks"]["brush teeth"])-14:],
                                database[patient]["tasks"]["shower"][len(database[patient]["tasks"]["shower"])-14:],
                                database[patient]["tasks"]["walk"][len(database[patient]["tasks"]["walk"])-14:],
                                database[patient]["tasks"]["meal"][len(database[patient]["tasks"]["meal"])-14:],
                                database[patient]["tasks"]["sleep"][len(database[patient]["tasks"]["sleep"])-14:]]
    if request.method == 'POST':
        mood = request.form["mood"]
        print(mood)        
        brushed = request.form.get("brushed")
        showered = request.form.get("showered")
        walked = request.form.get("walked")
        ate = request.form.get("ate")
        slept = request.form.get("slept")
        txt = request.form["txt"]
        print(txt)
        
        if len(check[patient]) == 1:
            return render_template("dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x,  values=y, patient=session["patient_user_dashboard"], task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
        else:
            database[patient]["date"].append("Mar 14")
            database[patient]["how was your day"].append(mood)
            database[patient]["problems_and_solutions"].insert(0, "Mar 14: "+txt)
            if brushed == "":
                database[patient]["tasks"]["brush teeth"].append("Yes")
                print("YOU BRUSHED")
            else:
                database[patient]["tasks"]["brush teeth"].append("No")

            if showered == "":
                print("YOU SHOWERED")
                database[patient]["tasks"]["shower"].append("Yes")
            else:
                database[patient]["tasks"]["shower"].append("No")

            if walked == "":
                print("YOU WALKED")
                database[patient]["tasks"]["walk"].append("Yes")
            else:
                database[patient]["tasks"]["walk"].append("No")

            if ate == "":
                database[patient]["tasks"]["meal"].append("Yes")
            else:
                database[patient]["tasks"]["meal"].append("No")
                
            if slept == "":
                database[patient]["tasks"]["sleep"].append("Yes")
            else:
                database[patient]["tasks"]["sleep"].append("No")

            check[patient].append(1)
            x = database[patient]["date"][len(database[patient]["date"])- 7:]
            y = database[patient]["how was your day"][len(database[patient]["how was your day"])- 7:]
            problems_and_sol = database[patient]["problems_and_solutions"]
            last_14_days=database[patient]["date"][len(database[patient]["date"])- 14:]
            last_14_days_task =[database[patient]["tasks"]["brush teeth"][len(database[patient]["tasks"]["brush teeth"])-14:],
                                        database[patient]["tasks"]["shower"][len(database[patient]["tasks"]["shower"])-14:],
                                        database[patient]["tasks"]["walk"][len(database[patient]["tasks"]["walk"])-14:],
                                        database[patient]["tasks"]["meal"][len(database[patient]["tasks"]["meal"])-14:],
                                        database[patient]["tasks"]["sleep"][len(database[patient]["tasks"]["sleep"])-14:]]
            
            return render_template("dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x,  values=y, patient=session["patient_user_dashboard"], task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
    return render_template("dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x,  values=y, patient=session["patient_user_dashboard"], task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)

@app.route("/docdashboard", methods=['POST', 'GET'])  #LOGIN PAGE
def showPatientChart():

    if "patient_user_dashboard" in session:
        patient = session["patient_user_dashboard"]


    # FUNC FOR GRAPH
    if request.method == 'POST':
        length = request.form["content"]

        # dont change this stuff there. its outta order bc I mixed x and y axis
        graph_x = database[patient]["date"]
        graph_y = database[patient]["how was your day"]
        problems_and_sol = database[patient]["problems_and_solutions"]
        last_14_days = database[patient]["date"][len(database[patient]["date"])- 14:]
        last_14_days_task =[database[patient]["tasks"]["brush teeth"][len(database[patient]["tasks"]["brush teeth"])-14:],
                            database[patient]["tasks"]["shower"][len(database[patient]["tasks"]["shower"])-14:],
                            database[patient]["tasks"]["walk"][len(database[patient]["tasks"]["walk"])-14:],
                            database[patient]["tasks"]["meal"][len(database[patient]["tasks"]["meal"])-14:],
                            database[patient]["tasks"]["sleep"][len(database[patient]["tasks"]["sleep"])-14:]]
        global chartLength
        if length == "30":  #IF 30 DAYS BUTTON PRESSED
            chartLength = 30
            x = graph_x[(len(graph_x)- 30):]
            y = graph_y[(len(graph_y)- 30):]
            return render_template('dashboard.html', graph_title='30 Day Mood Change', min=1, max=7, labels=x, values=y, patient=patient, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
        elif length == "14": #IF 14 DAYS BUTTON PRESSED
            chartLength = 14
            x = graph_x[(len(graph_x)- 14):]
            y = graph_y[(len(graph_y)- 14):]
            return render_template('dashboard.html', graph_title='14 Day Mood Change', min=1, max=7, labels=x, values=y, patient=patient, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
        else: #length == "7": (IF 7 DAYS BUTTON PRESSED)
            chartLength = 7
            x = graph_x[(len(graph_x)- 7):]
            y = graph_y[(len(graph_y)- 7):]
            return render_template("dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x, values=y, patient=patient, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
    else:
        x = graph_x[(len(graph_x)- 7):]
        y = graph_x[(len(graph_x)- 7):]
        return render_template("dashboard.html", graph_title='7 Day Mood Change', min=1, max=7, labels=x,  values=y, patient=patient, task_14=last_14_days_task, days_14=last_14_days, problems_and_sol=problems_and_sol)
    # return render_template("dashboard.html", labels = labels, values = values, max=7, min=1)


#pip3 install virtualenv
#virtualenv env
#source env/bin/activate
#pip3 install flask 



if __name__ == "__main__":
    app.run(debug=True)
