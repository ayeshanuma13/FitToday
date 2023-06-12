from setup import mysql,session

class Exercise:
    #Definig default constructor
    def __init__(self,exercise_id,exercise_name,exercise_time,exercise_intensity,exercise_desc,reps):
        self.exercise_id=exercise_id
        self.exercise_name=exercise_name
        self.exercise_time=exercise_time
        self.exercise_intensity=exercise_intensity
        self.exercise_desc=exercise_desc
        self.reps=reps

    #Defing function to fetch all details from exercise table and return fetched values
    def exerciseDetail(self):
        mycursor=mysql.connection.cursor()
        try:
            mycursor = mysql.connection.cursor()
            mycursor.execute("SELECT * FROM exercise")
            exercises = mycursor.fetchall()
            mysql.connection.commit()
            if (mycursor.rowcount>0):
                print('exerciseDetail | successful')
                return exercises
            else:
                print("exerciseDetail | failed")
                return False
        
        except Exception as e:
            mysql.connection.rollback()
            print(f"exerciseDetail | Error : {e}")
            return False
            
        finally:
            mycursor.close()
    
    #Define function to return set of specified exercises from exercise table 
    def customExercise(self):
        mycursor=mysql.connection.cursor()
        try:
            mycursor = mysql.connection.cursor()
            mycursor.execute("SELECT * FROM exercise WHERE exercise_id in %s;",(self.exercise_id,))
            exercises = mycursor.fetchall()
            if (exercises):
                print('customExercise | successful')
                return exercises
            else:
                print("exerciseDetail | failed")
                return False
        
        except Exception as e:
            mysql.connection.rollback()
            print(f"customExercise| Error : {e}")
            return False
            
        finally:
            mycursor.close()

        
    #Defining function to fill an exercise sequence in user_workout table
    def fillExerciseSeq(self,user_id,plan_id):
        mycursor=mysql.connection.cursor()

        try:
            mycursor = mysql.connection.cursor()
            mycursor.execute("INSERT INTO user_workout (user_id,plan_id,exercise_id) VALUES (%s,%s,%s)", (user_id,plan_id,self.exercise_id))
            mysql.connection.commit()

            if (mycursor.rowcount>0):
                print('fillExerciseSeq | successful')
                return True
            else:
                print("fillExerciseSeq | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"fillExerciseSeq  | Error : {e}")
            return False
                
        finally:
             mycursor.close()

    #Defining function to return all data fromexercise table for the dropdown menu
    def dropdownExercise(self):
        mycursor=mysql.connection.cursor()
        try:
            mycursor = mysql.connection.cursor()
            mycursor.execute("SELECT * FROM exercise;")
            exercises = mycursor.fetchall()
            if (exercises):
                print('dropdownExercise | successful')
                return exercises
            else:
                print("dropdownExrecise | failed")
                return False
        
        except Exception as e:
            mysql.connection.rollback()
            print(f"dropdownExercise| Error : {e}")
            return False
            
        finally:
            mycursor.close()
    