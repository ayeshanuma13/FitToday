from setup import mysql,session

class User:
    #Defining default constructor
    def __init__(self,userid,username,email,password,gender,age,height,weight):
        self.userid=userid
        self.username=username
        self.email=email
        self.password=password
        self.gender=gender
        self.age=age
        self.height=height
        self.weight=weight

    #Defining function to check if user already exists or register new user
    def registerUser(self):
        mycursor=mysql.connection.cursor()
        
        try:
            query = 'SELECT * FROM user_details WHERE USERNAME=%s'
            value = (self.username,)
            mycursor.execute(query,value)
            result = mycursor.fetchall()

            if result:

                print('Register | Username already exists')
                return False
            
            else:
                query="INSERT INTO user_details (username,email,password,gender,age,height,weight) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                value=(self.username,self.email,self.password,self.gender,self.age,self.height,self.weight)
                mycursor.execute(query,value)
                mysql.connection.commit()
                if (mycursor.rowcount>0):
                    print("registerUser  | successful")
                    return True
                else:
                    print("registerUser | failed")
                    return False
        except Exception as e:
            mysql.connection.rollback()
            print(f"registerUser | Error : {e}")
            return False
                
        finally:
            mycursor.close()

    #Defining function to verify if user_details match with the corresponding data in the database
    def loginUser(self):
        mycursor=mysql.connection.cursor()

        try:
            query = 'SELECT * FROM user_details WHERE USERNAME=%s AND PASSWORD=%s'
            values = (self.username, self.password)
            mycursor.execute(query, values)
            result = mycursor.fetchall()

            if result:
                self.userid =  result[0][0]
                self.username = result[0][1]
                self.email = result[0][2]
                self.password=result[0][3]
                self.gender = result[0][4]
                self.age = result[0][5]
                self.height = result[0][6]
                self.weight = result[0][7]

                session['userid'] = result[0][0]
                session['username'] = result[0][1]
                session['email'] = result[0][2]
                session['password']=result[0][3]
                session['gender'] = result[0][4]
                session['age'] = result[0][5]
                session['height'] = result[0][6]
                session['weight'] = result[0][7]

                print("Login | successful")
                return True

            else:
                print("Login | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"Login | Error: {e}")
            return False
      
        finally:
            mycursor.close()

    #Defining function to fetch all details of a specific user from database
    def viewProfile(self):
        mycursor=mysql.connection.cursor()

        try:
            query = 'SELECT * FROM user_details WHERE USERID=%s'
            values = (self.userid,)
            mycursor.execute(query, values)
            result = mycursor.fetchall()

            if result:
                print("viewProfile | successful")
                return result
            
            else:
                print("viewProfile | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"viewProfile | Error: {e}")
            return False
        
        finally:
            mycursor.close()

    #Defining function to update the data for a specific user in user_details table
    def editProfile(self):
        mycursor=mysql.connection.cursor()

        try:
            query ="UPDATE user_details SET username = %s, email=%s,password=%s,gender=%s,age=%s,height=%s,weight=%s WHERE userid=%s;"
            values=(self.username,self.email,self.password,self.gender,self.age,self.height,self.weight,self.userid)
            mycursor.execute(query, values)
            mysql.connection.commit()
            if (mycursor.rowcount>0):
                print("editProfile | successful")
                return True
            else:
                print("editProfile | failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"editProfile | Error : {e}")
            return False
                
        finally:
            mycursor.close()

    #Defining function to eturn count of total number of users from user_details table
    def userCount(self):
        mycursor=mysql.connection.cursor()

        try:
            mycursor.execute("SELECT count(userid) from user_details")
            result = mycursor.fetchall()

            if result:
                print("userCount | successful")
                return result
            
            else:
                print("userCount| failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"userCount | Error: {e}")
            return False
        
        finally:
            mycursor.close()

    #Defining function to fetch the height of a particular user from user_details table
    def getHeight(self,userid):
        mycursor=mysql.connection.cursor()

        try:
            query="SELECT height from user_details where userid=%s"
            value=(userid,)
            mycursor.execute(query,value)
            result = mycursor.fetchall()

            if result:
                print("getHeight | successful")
                return result
            
            else:
                print("getHeight| failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"getHeight | Error: {e}")
            return False
        
        finally:
            mycursor.close()

    #Defining function to fetch the weight of a particular user from user_details table
    def getWeight(self,userid):
        mycursor=mysql.connection.cursor()

        try:
            query="SELECT weight from user_details where userid=%s"
            value=(userid,)
            mycursor.execute(query,value)
            result = mycursor.fetchall()

            if result:
                print("getWeight | successful")
                return result
            
            else:
                print("getWeight| failed")
                return False
            
        except Exception as e:
            mysql.connection.rollback()
            print(f"getWeight | Error: {e}")
            return False
        
        finally:
            mycursor.close()