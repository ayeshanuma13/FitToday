from flask import Flask,render_template,url_for,redirect,session,flash,request
from flask_mysqldb import MySQL



app=Flask(__name__)

host="localhost"
user="root"
password="Aspire@123"
db="fittoday"
secret_key="abc"

app.config['MYSQL_HOST'] = host
app.config['MYSQL_USER'] = user
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = db

app.secret_key=secret_key
mysql=MySQL(app)


#, redirect, url_for, render_template, request,  jsonify