from flask import Blueprint, render_template,request,session
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import redirect, url_for

uri = "mongodb+srv://d8o8r8:K8u8r8a8n8t8@cluster0.prckjxg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['mydatabase']  # יצירת דאטה בייס
customers_col = mydatabase['customers']  # מצביע ללקוחות
requests_col = mydatabase['request']  # מצביע ללקוחות

costumer_list = list(customers_col.find())
print(costumer_list)
request_list = list(requests_col.find())
print(request_list)