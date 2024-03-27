from flask import Blueprint, render_template
from flask import render_template
from flask import request, session
from flask import jsonify
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import redirect, url_for

uri = "mongodb+srv://d8o8r8:K8u8r8a8n8t8@cluster0.prckjxg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['mydatabase']  # יצירת דאטה בייס
customers_col = mydatabase['customers']  # מצביע ללקוחות
requests_col = mydatabase['request']  # מצביע ללקוחות
obligations_col = mydatabase['obligations']  # מצביע ללקוחות

Contact_info=Blueprint(
    'contact_info',
    __name__,
    static_folder='static',
    static_url_path='/contact_info',
    template_folder='templates'
)

@Contact_info.route('/Contact_info')
def Contact_info_page():  # put application's code here
    my_list = list(requests_col.find())


    # new_dict={
    #     'userName': session.get('username'),
    #     'request': request.form.get('category')
    # }
    # obligations_col.insert_one(new_dict)

    return render_template('contact_info.html',page_name='Choose Your Pro',my_list=my_list)