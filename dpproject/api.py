#! /home/linuxbrew/.linuxbrew/bin/python3

from flask import Flask, g, make_response, request, json, jsonify
import mysql
from mysql.connector import Error

app = Flask(__name__)

config = {
    'user' : 'root',
    'password': 'develpreneur',
    'host': '127.0.0.1',
    'database': 'dpproject',
    'raise_on_warnings': True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()

@app.route("/db")
def dbTest():
    try:
        query = "select * from dpproject_task"
        cursor.execute(query)
        rows = cursor.fetchall()
    except Error as e:
        return make_response(jsonify(e),500)    

    return make_response(jsonify(rows),200)

@app.route("/")
def home():
    return "API is Active!"

@app.route("/about")
def about():
    return "Version 1.0"

@app.route("/complete/id")
def completeTask():
    try:
        query = "update dpproject_task set lkpStatus_id=3 where id = :id"
        cursor.execute(query)
        print("Task " + str(id) + " is complete.")
    except Error as e:
        return make_response(jsonify(e),500)    

    return HttpResponse("Success")


app.run()
