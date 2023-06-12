from setup import mysql,session

class Progress:

    #Defining default constructor
    def __init__(self,progress_id,user_id,plan_id,completion_date,completion_time):
        self.progress_id=progress_id
        self.user_id=user_id
        self.plan_id=plan_id
        self.completion_date=completion_date
        self.completion_time=completion_time
    
    #Defining function to enter progress details into progress table
    def insertProgress(self):
        mycursor=mysql.connection.cursor()

        try:
            query = "INSERT INTO progress (user_id,plan_id,completion_date,completion_time) VALUES (%s,%s,%s,%s)"
            value = (self.user_id,self.plan_id,self.completion_date,self.completion_time)
            mycursor.execute(query,value)
            mysql.connection.commit()

            if (mycursor.rowcount>0):
                print('inserProgress | successful')
                return True
            
            else:
                print("insertProgress | failed")
                return False
        
        except Exception as e:
            mysql.connection.rollback()
            print(f"insertProgress | Error : {e}")
            return False
            
        finally:
            mycursor.close()
    
    #Defining function to fetch progress details from progress and workoutplan tables
    def viewProgress(self):
        mycursor=mysql.connection.cursor()

        try:
            query = 'select workoutplan.plan_name,progress.completion_date,progress.completion_time from progress inner join workoutplan on workoutplan.plan_id=progress.plan_id where user_id=%s'
            values = (self.user_id,)
            mycursor.execute(query, values)
            result = mycursor.fetchall()

            if result:
                print("viewProgress | successful")
                return result
            
            else:
                print("viewProgress | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"viewProgress | Error: {e}")
            return False
        
        finally:
            mycursor.close()

    #Defining funtion to return count of records in progress table for a specific user
    def viewUserDayCount(self):
        mycursor=mysql.connection.cursor()

        try:
            query='select COUNT(*) from progress where user_id=%s;'
            # query = 'select count from (select user_id,COUNT(completion_date) as count from progress group by user_id) userDayCount where user_id=%s'
            values = (self.user_id,)
            mycursor.execute(query, values)
            result = mycursor.fetchall()

            if result:
                print("viewUSerDayCount | successful")
                return result
            
            else:
                print("viewUserDayCount | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"viewUserDayCount | Error: {e}")
            return False
        
        finally:
            mycursor.close()
