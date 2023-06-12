# Title: FitToday - Customizable Fitness Tracking Application
# Author: Ayesha Numa Syed
# Created on: 01/06/2023
# Last Modified Date: 12/06/2023
# Reviewed on: Naveen Subraminiam
# Reviwed on: 12/06/2023



from setup import app,request,render_template,url_for,redirect,session
from datetime import datetime
import calendar


############################### Classes ########################################

from classes.user import User
from classes.workouts import Workouts
from classes.exercise import Exercise
from classes.progress import Progress
from classes.weightprogress import WeightProgress
from classes.bmi import BMI

############################### Classes ########################################

@app.route('/')
def Initial():
    #Redirecting the users to Homepage function on first running the app
    return redirect(url_for('Homepage'))

#Decorator used to define route and specify the function to be executed
#Route handles both GET and POST requests.

@app.route('/home',methods=['GET','POST'])
#Function reads form submission from home.html and redirects users to login or signup 
def Homepage():
    if request.method=="POST":
        action=request.form['action']
        if action=='login':
            return redirect(url_for('Login'))
        elif action=='signup':
            return redirect(url_for('Signup'))
        else:
            return render_template('homepage.html')
    else:
        return render_template('homepage.html')

@app.route('/signup',methods=['GET','POST'])
#Sign up function registers users
def Signup():
    if request.method=="POST":
        action=request.form['action']
        if action=='Signup':
            #Reads the user input from signup.html form 
            username=request.form['username']
            email=request.form['email']
            password=request.form['password']
            gender=request.form['gender']
            age=(request.form['age'])
            height=(request.form['height'])
            weight=(request.form['weight'])
            
            #Creating an instance of User class
            user=User(0,username,email,password,gender,(age),(height),(weight))

            #Calling function to insert user details into database
            registrationResult=user.registerUser()

            #If details inserted successfully redirects to login page else reloads the signup page
            if(registrationResult):
                return render_template('login.html')
            else:
                return render_template('signup.html')
        else:
            return render_template('signup.html')
    else:
        return render_template('signup.html')


@app.route('/login',methods=['GET','POST'])
#Login function performs server validation
def Login():
    if request.method=="POST":
        action=request.form['action']
        if action=='godashboard':
            #Reading the username and password from login.html form
            username=request.form['username']
            password=request.form['password']

            #Creating an instance of User class
            user=User("",username,"",password,"","","","")

            #Calling function to verify results with backend data
            loginResult=user.loginUser()

            #If data matches user is redirected to dashboard 
            if(loginResult):
                return redirect(url_for('Dashboard'))
            else:
                #Else login page is reloaded with invalid credentials message
                error = 'Invalid credentials'
                return render_template('login.html',error=error)
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route('/dashboard',methods=['GET','POST'])
#Dashboard function renders the dashboard.html template 
def Dashboard():
    if request.method=="POST":
        #Rendering the dashboard.html template
        return render_template('dashboard.html')
    else:
        if 'userid' in session:
            #Creating an instance of User class
            user=User("","","","","","","","")
            #Calling function to return total count of users from database
            user_num=user.userCount()
            #Displaying the count in dashboard.html
            return render_template('dashboard.html',user_num=user_num)
        else:
            return redirect(url_for("Login"))

@app.route('/workout',methods=['GET','POST'])
#Workout function renders the main workout page and redirects each plan to workout_plan_detail with plan_id as parameter
def Workout():
    if request.method=="POST":
        action=request.form["action"]
        if (action=="wp1"):
            return redirect(url_for('workout_plan_detail', plan_id=1))
        elif (action=="wp2"):
            return redirect(url_for('workout_plan_detail', plan_id=2))
        elif (action=="wp3"):
            return redirect(url_for('workout_plan_detail', plan_id=3))
        elif (action=="wp4"):
            return redirect(url_for('workout_plan_detail', plan_id=4))
        elif (action=="wp5"):
            return redirect(url_for('workout_plan_detail', plan_id=5))
        elif (action=="wp6"):
            return redirect(url_for('workout_plan_detail', plan_id=6))
        else:
            print("Workout| Invalid action")
            return redirect(url_for('Workout'))
    else:
        return render_template('workout.html')

@app.route('/workout_plan/<int:plan_id>', methods=['GET','POST'] )
#workout_plan_detail function modifies the existing plan depending on the user's customization preferences
def workout_plan_detail(plan_id):
    if request.method=="POST":
        action=request.form["action"]
        if (action=="done"):
            #If user clicks on done, storing the date and time of completion in variables
            completion_date=datetime.now().date()
            completion_time=datetime.now().time()
            user_id = session['userid']

            #Creating an instance of Progress class with user_id, completion date and time as arguments
            progress=Progress("",user_id,plan_id,completion_date,completion_time)

            #Calling function to insert progress values into progress database
            progress.insertProgress()

            #Redirecting to ProgressDets
            return redirect(url_for('ProgressDets'))
        
        elif (action=="remove"):
            #If user clicks on remove fetching exercise id of removed exercise
            exercise_id=request.form["exercise_id"]
            print("exercise_id:",exercise_id)

            #Creating an instance of Workouts class with plan_id as parameter
            workout=Workouts(plan_id,"","","")
            user_id=session['userid']

            #Calling function to fetch the previously stored exercise sequence for this user for this plan
            retrieveSeq=workout.fetchExerciseSeq(user_id)
            exercise_str=retrieveSeq[0][3]

            #Converting the string fetched to list with items of int datatype
            exercise_list = exercise_str.split(',')
            print(exercise_list)
            for i in range(len(exercise_list)):
                exercise_list[i] = int(exercise_list[i])

            #Removing the exercise_id that matches with the selected exercise from the list
            for i in exercise_list:
                if (i==int(exercise_id)):
                    exercise_list.remove(i)

            #Converting the updated list back to string
            exercise_str = ','.join(map(str, exercise_list))

            #Creating an instance of Workouts class
            updateSeq=Workouts(plan_id,"","","")

            #Calling function to update the new exercise sequence in the database
            updateseq=updateSeq.updateExerciseSeq(user_id,exercise_str)

            if(updateseq):
                print("Update sequence successfullly")
                #Reloads the page with the changes
                return redirect(url_for('workout_plan_detail', plan_id=plan_id))
            else:
                return render_template('workout.html')
            
        elif (action=="add"):
            #If user selects add, fetching the exercise_id of the exercise to be added
            exercise_id=request.form["exercise_id"]
            user_id=session['userid']

            #Creating an instance of Workouts class
            workout=Workouts(plan_id,"","","")

            #Callin function to fetch the existing exercise sequence for this user for this plan
            retrieveSeq=workout.fetchExerciseSeq(user_id)
            exercise_str=retrieveSeq[0][3]

            #Converting fetched string to list
            exercise_list = exercise_str.split(',')
            for i in range(len(exercise_list)):
                exercise_list[i] = int(exercise_list[i])

            #Adding the new exercise to the list
            exercise_list.append(exercise_id)

            #Converting updated list back to string
            exercise_str = ','.join(map(str, exercise_list))

            #Creating an instance of Workouts class
            updateSeq=Workouts(plan_id,"","","")

            #Calling function to update the new exercise sequence in the database
            updateseq=updateSeq.updateExerciseSeq(user_id,exercise_str)

            if(updateseq):
                print("Update sequence successfullly")
                #Reloading the page with the new changes
                return redirect(url_for('workout_plan_detail', plan_id=plan_id))
            else:
                return render_template('workout.html')



        else:
            print("workout_plan_detail | Invalid action")
            return render_template('workout.html')


    else:
        user_id = session['userid']
        workouts=Workouts(plan_id,"","","")
        workout_plan,exercises=workouts.workoutPlanDetail(plan_id)
        result=workouts.fetchExerciseSeq(user_id)
        if(result):
            exercise_tuple = tuple(map(int, result[0][3].split(',')))
            exercise=Exercise(exercise_tuple,"","","","","")
            custom_exercise=exercise.customExercise()
            exercise_dropdown=exercise.dropdownExercise()
            if(custom_exercise):
                print("customized exercises fetched")
                return render_template('wp_details.html', workoutplan=workout_plan, exercise_details=custom_exercise,plan_id=plan_id,exercise_dropdown=exercise_dropdown)
            else:
                print("customized exercises NOT fetched")
                return redirect(url_for('Workout'))

        else:
            workouts=Workouts("","","","")
            workout_plan,exercises=workouts.workoutPlanDetail(plan_id)
            exercise_str=""
            for row in exercises:
                exercise_id=row[0]
                if len(exercise_str)==0:
                    exercise_str=exercise_str + str(exercise_id)
                else:
                    exercise_str=exercise_str + ',' + str(exercise_id)
            exercise=Exercise(exercise_str,"","","","","")
            fillexerciseseq=exercise.fillExerciseSeq(user_id,plan_id)
            exercise_dropdown=exercise.dropdownExercise()

            if(fillexerciseseq):
                print("sequence added successfully")
                return render_template('wp_details.html', workoutplan=workout_plan, exercise_details=exercises,plan_id=plan_id,exercise_dropdown=exercise_dropdown)
            else:
                print("sequence not added")
                return redirect(url_for('Workout'))
            
@app.route('/exercise',methods=['GET','POST'])
#ExerciseDets function displays all exercise details
def ExerciseDets():
    #Creating an instance of Exercise class
    exercises=Exercise("","","","","","")

    #Calling function to fetch all data from exercise table in database
    exercisedets=exercises.exerciseDetail()

    #Rendering the html page with the fetched details
    return render_template('exercise.html',exercise_details=exercisedets)

@app.route('/progress',methods=['GET','POST'])
#ProgressDets function displays the various types of progress made by the specific user
def ProgressDets():
    if 'userid' in session:
        if request.method=="POST":
            action=request.form["action"]
            if (action=="update"):
                #Reading the weight input from the html form
                weight=request.form["weight"]
                print("THIS IS WEIGHT:",weight)

                #Fetching user_id from session user_id
                user_id=session['userid']

                #Creating an instance of User class
                height_obj=User(user_id,"","","","","","","")

                #Calling a function to get height
                heightdet=height_obj.getHeight(user_id)
                print("THIS IS WEIGHT:",weight)
                print("THIS IS HEIGHT:",heightdet)

                #Creating an instance of BMI class with userid, heigth and weight as arguments
                bmi_obj=BMI("",user_id,weight,heightdet)

                #Calling function to insert user_id, height,weight into bmi table in database
                bmi_obj.insertBMI()

                #Storing the current date and time in variable
                weight_date=datetime.now().date()

                #Creating an instance of WeightProgress class
                weightdet=WeightProgress(user_id,weight_date,weight)

                #Calling function to insert user_id,date and weight in weight_prog table in database
                weightResult=weightdet.insertProgress()
    
    

                if(weightResult):
                    print("VWeight details inserted successfully")
                    return redirect(url_for("ProgressDets"))
                else:
                    print("Weight update | failed")
                    return redirect(url_for("ProgressDets"))
            else:
                print("Weight update | invalid action")
                return redirect(url_for("ProgressDets"))



        else:
            user_id = session['userid']

            #Creating an instance of User class
            weight_obj=User(user_id,"","","","","","","")

            #Calling gunction to fetch weight_goal of user from user_details table 
            weight_goal=weight_obj.getWeight(user_id)

            #Creating an instance of Progress class
            userProgress = Progress("",user_id,"","","")

            #Calling function to return all data of progress table
            result = userProgress.viewProgress()

            #Calling function to return count of progress recorded for the specific
            result2=userProgress.viewUserDayCount()

            #Creating an instance of BMI class
            bmi_obj=BMI("",user_id,"","")

            #Calling a function to get data from bmi table in database
            bmidet=bmi_obj.getBmiDets(user_id)
            if bmidet:
                #If record exists height and weight are stored in variables for bmi calculation
                bmi_weight=bmidet[0][2]
                bmi_height=bmidet[0][3]
                bmi_weight=int(bmi_weight)
                bmi_height=int(bmi_height)
                #BMI calclation formula is applied on user height and weight
                bmi_value=round(((bmi_weight/(bmi_height*bmi_height))*10000),2)

                #Difference of weight goal and current weight is recorded in weight_diff
                weight_diff=(bmi_weight)-weight_goal[0][0]
                print("THIS IS WEIGHT DIFF:",weight_diff)

                #If current weight is less than weight_goal, weight_diff is considered 0, else it remains the same
                if weight_diff>0:
                    weight_diff=weight_diff
                else:
                    weight_diff=0 

                #Depending on the calculated BMI value appropriate message is stored in message variable 
                if bmi_value<=18.4:
                    message="Underweight"
                elif 18.5<bmi_value<24.9:
                    message="Normal"
                elif 25<bmi_value<39.9:
                    message="Overweight"
                elif bmi_value>=40:
                    message="Obese"
                else:
                    message="Invalid BMI value"
            else:
                print("Bmidet failed")
                bmi_value=0
                message="Update weight to check BMI"
                weight_diff=0

            #Creating an instance of WeightProgress class
            weightdet=WeightProgress(user_id,"","")

            #Calling function to return list of dates and weight from weight_prog table in database
            chart_x,chart_y=weightdet.weightChart()
            if result:

                print("viewProgress | successful")
                marked_dates=[]
                for row in result:
                    marked_dates.append(datetime.strptime(str(row[1]), '%Y-%m-%d').date())
            
                #Storing current month and year in variables
                current_year = datetime.now().year
                current_month = datetime.now().month


                #An instance of the HTMLCalendar class from the calendar module is created.
                cal = calendar.HTMLCalendar()

                #Generating an HTML representation of a calendar month for the current year and month
                calendar_html = cal.formatmonth(current_year, current_month, withyear=True)

                #Iterates through the marked_dates list and modifies the generated HTML calendar by changing background color of marked dates to yellow
                for date in marked_dates:
                    calendar_html = calendar_html.replace(f'>{date.day}<', f' style="background-color: yellow; color: black; font-weight: bold;">{date.day}<')
                return render_template('progress.html', calendar_html=calendar_html, details=result2, chart_x=chart_x, chart_y=chart_y,bmi_value=bmi_value,bmi_msg=message,weight_diff=weight_diff)

            else:
                #If no progress by user has been made set details to 0 and render same template

                userProgress = Progress("",user_id,"","","")
                result2=userProgress.viewUserDayCount()

                bmi_value=0
                message="Update weight to check BMI"
                weight_diff=0

                weightdet=WeightProgress(user_id,"","")
                chart_x,chart_y=weightdet.weightChart()
                
                current_year = datetime.now().year
                current_month = datetime.now().month
                cal = calendar.HTMLCalendar()
                calendar_html = cal.formatmonth(current_year, current_month, withyear=True)

                print("viewProgress | failed")
                return render_template('progress.html',details=result2,chart_x=chart_x, chart_y=chart_y,calendar_html=calendar_html,bmi_value=bmi_value,bmi_msg=message,weight_diff=weight_diff)
    else:
        return redirect(url_for('Login'))

@app.route('/profile',methods=['GET','POST'])
#Profile function displays the profile details of the specific user
def Profile():
    if request.method=="POST":
        action=request.form["action"]
        if (action=="editProfile"):
            #If user wants to edit profile they are redirected to UpdateProfile
            return redirect(url_for('UpdateProfile'))
        
        elif(action=="logout"):
             #If user wants to logout the session is cleared and they are redirected to login page
             session.clear()
             print("ProfileLogout | Session data cleared successfully.")
             return redirect(url_for('Login'))
        else:
            print("Profile| Invalid action")
            return redirect(url_for('Profile'))


    else:
        if 'userid' in session:
            #user_id is fetched from session user id
            userid = session['userid']

            #An instance of User class is created with user_id as parameter
            user = User(userid,"","","","","","","")

            #Calling a function to fetch all details from user_details table in database
            result = user.viewProfile()
            if result:
                #Rendering profile.html with the fetched detials
                return render_template('profile.html', details = result)
            else:
                print("viewProfile | failed to get details.")
                return render_template('profile.html')
        else:
            return redirect(url_for('Login'))
        
@app.route('/editprofile',methods=['GET','POST'])
#Profile function updates the profile details of the specific user
def UpdateProfile():
    if request.method=="POST":
        action=request.form["action"]
        if (action=="editProfile"):
            #If user clicks on update profile the input values of form are read
            userid=session['userid']
            username=request.form['username']
            email=request.form['email']
            password=request.form['password']
            gender=request.form['gender']
            age=request.form['age']
            height=request.form['height']
            weight=request.form['weight']
          
            #An instance of user class is created with the values read in the form as parameters
            user=User(userid,username,email,password,gender,age,height,weight)

            #Calling a function to update the values into the user_details table
            result=user.editProfile()

            if result:
                print("editProfile | successful")
                return redirect(url_for('Profile'))
            
            else:
                print("editProfile | failed")
                return redirect(url_for('Profile'))
        else:
            return render_template('profile.html')
    else:
            userid = session['userid']
            #Creating an instance of user class
            user = User(userid,"","","","","","","")

            #Calling the function the fetch details from the updated table
            result = user.viewProfile()
            if result:
                #Rendering profile template with fetched details
                return render_template('update_profile.html', details = result)

#Checking if the current module is the main module being executed directly and if yes, runs the app
#Allows us to start the Flask application when executing the script directly but not when it is imported as a module.
if __name__=='__main__':
    app.run(debug=True)