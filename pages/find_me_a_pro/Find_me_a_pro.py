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

Find_me_a_pro=Blueprint(
    'find_me_a_pro',
    __name__,
    static_folder='static',
    static_url_path='/find_me_a_pro',
    template_folder='templates'
)


@Find_me_a_pro.route('/Find_me_a_pro')
def find_me_a_pro_page():  # put application's code here
    # my_list = list(requests_col.find({'request':category}))
    return render_template('find_me_a_pro.html',page_name='Find me a pro')