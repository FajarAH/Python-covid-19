# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:58:30 2020

@author: Fajar
"""

import requests
import json
import mysql.connector

url = "https://pomber.github.io/covid19/timeseries.json"

response = requests.get(url)
data = response.text
parsed_json = json.loads(data)

country = parsed_json

#print(country)
#type(country)

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE covid")
except:
    print("database already exist")

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="covid"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE covid_data (country VARCHAR(255), confirmed VARCHAR(50) , recovered VARCHAR(50), deaths VARCHAR(50), datex VARCHAR(50))")
except:
    print("table already exist")
finally:
    
    sql = "INSERT INTO covid_data (country, confirmed, recovered, deaths, datex) VALUES (%s,%s,%s,%s,%s)"
    
    for y,z in country.items():
        for x in z:
            mycursor.execute(sql, (y, x["confirmed"], x["recovered"],x["deaths"], x["date"]))
    
    mydb.commit()
    print(mycursor.rowcount, "record successfully inserted.")