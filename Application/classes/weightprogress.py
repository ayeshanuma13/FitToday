from setup import mysql,session

class WeightProgress:
    #Defining default constructor
    def __init__(self,user_id,weight_date,weight):
        self.user_id=user_id
        self.weight_date=weight_date
        self.weight=weight

    #Defining function to insert new progress data into weight_prog table in database
    def insertProgress(self):
        mycursor=mysql.connection.cursor()

        try:
            query = "INSERT INTO weight_prog (user_id,weight_date,weight) VALUES (%s,%s,%s)"
            value = (self.user_id,self.weight_date,self.weight)
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

    #Defining function to fetch weight_date(for x-axis of chart) and weight(for y-axis of chart) for a specific user from weight_prog table 
    def weightChart(self):
        

        mycursor = mysql.connection.cursor()

        try:
            query = 'SELECT weight_date, weight FROM weight_prog WHERE user_id = %s ORDER BY weight_date ASC'
            values = (self.user_id,)
            mycursor.execute(query, values)
            result = mycursor.fetchall()
            x_values = []
            y_values = []

            if result:
                for row in result:
                    x_values.append(row[0].strftime('%Y-%m-%d'))
                    y_values.append(float(row[1]))
                return x_values, y_values
            else:
                print("weightChart | no data found")
                return [], []
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"weightChart | Error: {e}")
            return [], []
        
        finally:
            mycursor.close()
