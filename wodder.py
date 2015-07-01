from flask import Flask, render_template, session, url_for 
import random 

# create the application object 
app = Flask(__name__) 

WODList = {"wod1" : "Jackie\n 1000 Meter Row\n 45 Thrusts\n 30 Pull-ups", 
           "wod2" : "Annie\n 50 Meter Row\n 44444 Thrusts\n 10000 Pull-ups",
           "wod3" : "Bill\n 50 Meter Row\n 44444 Thrusts\n 10000 Pull-ups",
           "wod4" : "Tom\n 50 Meter Row\n 44444 Thrusts\n 10000 Pull-ups"

           };

@app.route('/')
def index():
    wodprime = randgen()
    return render_template('index.html', wodprime=wodprime) 

def randgen(): 
    keys = [x for x in random.sample(WODList, 4)]
    workout = WODList[random.choice(keys)]
    workout1 = workout.replace('\n', '<br>')
    return workout1


if __name__ == '__main__':
    app.run(debug=True)





#goal of wodder generator engine 
# 1. Need to have a dictionary of workouts stored somewhere. Can store it in wodder.py 
# 2. Need to pull a workout when the user hits the generate WOD button 
        # Question - how do I connect the JS/HTML button function into the python logic? 
        # Question - how do I randomly have the computer pick something?
            # Answer - import random package // select random number in range // 
            # assign dictionary key to each variable so that when it gets selected it will 
            # pick that variable 
            # import random
            # d = {'VENEZUELA':'CARACAS', 'CANADA':'TORONTO'}
            # random.choice(d.keys())

            # "Jackie" - Name / # of rounds
            # For Time - Type of Constraint
            # 1000 Meter Row - Subworkout #1
            # 45 Thrusts (45#/30#) - Subworkout #2
            # 30 Pull-ups - Subworkout #3 
            # WODlist = [Jackie, Annie, Murph]
            # Jackie = ["Jackie", "1000 Meter Row", "45 Thrusts (45#/30#)", "30 Pull-ups"]
            # Annie = 
