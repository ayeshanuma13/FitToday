from setup import mysql,session

class Workouts:
    #Defining default constructor
    def __init__(self,plan_id,plan_name,plan_time,plan_intensity):
        self.plan_id=plan_id
        self.plan_name=plan_name
        self.plan_time=plan_time
        self.plan_intensity=plan_intensity

    #Defining function to display all workout plan details from workoutplan table
    def workoutPlanDetail(self,plan_id):
        cur=mysql.connection.cursor()

        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM workoutplan WHERE plan_id = %s", (plan_id,))
            workout_plan = cur.fetchall()
            cur.execute("""
            SELECT e.*
            FROM exercise e
            INNER JOIN PlanExercise pe ON pe.exercise_id=e.exercise_id
            WHERE pe.plan_id = %s
            ORDER BY pe.sequence""", (plan_id,))
            exercises = cur.fetchall()
            mysql.connection.commit()
            if (cur.rowcount>0):
                print('workout_plan_detail | successful')
                return workout_plan,exercises
            else:
                print("workout_plan_detail | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"workout_plan_detail | Error : {e}")
            return False
                
        finally:
             cur.close()

    #Defing function to fetch details for a specific user for a specific plan from user_workout table 
    def fetchExerciseSeq(self,user_id):
        mycursor=mysql.connection.cursor()

        try:
            mycursor = mysql.connection.cursor()
            mycursor.execute("SELECT * FROM user_workout WHERE plan_id = %s AND user_id=%s", (self.plan_id,user_id))
            user_workout_sequences = mycursor.fetchall()
            
            if (user_workout_sequences):
                print('fetchExerciseSeq | successful')
                return user_workout_sequences
            else:
                print("No existing sequence")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"fetchExerciseSeq  | Error : {e}")
            return False
                
        finally:
             mycursor.close()

    #Defining function to update user_workout table wit the user_id,plan_id and the customized list of exercises for that workout by that user
    def updateExerciseSeq(self,user_id,exercise_id):
        mycursor=mysql.connection.cursor()

        try:
            mycursor = mysql.connection.cursor()
            mycursor.execute("update user_workout set exercise_id=%s where plan_id=%s and user_id=%s;", (exercise_id,self.plan_id,user_id))
            
            mysql.connection.commit()
            if (mycursor.rowcount>0):
                print('updateExerciseSeq | successful')
                return True
            else:
                print("updateExercisSeq | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"updateExerciseSeq| Error : {e}")
            return False
                
        finally:
             mycursor.close()   
