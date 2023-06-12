from setup import mysql,session

class BMI:

    #Defining default constructor
    def __init__(self,bmi_id,user_id,weight,height):
        self.bmi_id=bmi_id
        self.user_id=user_id
        self.height=height
        self.weight=weight

    #Defining function to insert user_id, weight and height in bmi table and return true if inserted
    def insertBMI(self):
        mycursor=mysql.connection.cursor()

        try:
            query="INSERT INTO bmi (user_id,weight,height) VALUES (%s,%s,%s)"
            value=(self.user_id,self.weight,self.height)
            mycursor.execute(query,value)
            mysql.connection.commit()
            if (mycursor.rowcount>0):
                print("insertBMI  | successful")
                return True
            else:
                print("insertBMI | failed")
                return False
        except Exception as e:
            mysql.connection.rollback()
            print(f"insertBMI | Error : {e}")
            return False
                
        finally:
            mycursor.close()

    #Defining function to fetch all details from bmi table and return fetched values
    def getBmiDets(self,user_id):
        mycursor=mysql.connection.cursor()

        try:
            query="select * from bmi where bmi_id=(select max_bmi from (select max(bmi_id) as max_bmi,user_id from bmi group by user_id) user_bmi where user_id=%s);"
            value=(user_id,)
            mycursor.execute(query,value)
            result = mycursor.fetchall()
            if result:
                print("getBmiDets  | successful")
                return result
            else:
                print("getBmiDets | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"getBmiDets | Error : {e}")
            return False
                
        finally:
            mycursor.close()
