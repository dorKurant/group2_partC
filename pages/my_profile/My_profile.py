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

My_profile=Blueprint(
    'my_profile',
    __name__,
    static_folder='static',
    static_url_path='/my_profile',
    template_folder='templates'
)

@My_profile.route('/My_Profile')
def mongodb_func():
    costumer=customers_col.find_one({'userName':session.get('username')})
    my_list =list(requests_col.find({'userName':session.get('username')}))
    return render_template('My_Profile.html',page_name='My Profile', costumer=costumer,my_list=my_list)

@My_profile.route('/db_insert', methods=['POST'])
def insert_request():
    costumer=customers_col.find_one({'userName':session.get('username')})
    my_list =list(requests_col.find({'userName':session.get('username')}))
    new_dict={
        'userName':session.get('username'),
        'reques':request.form.get('category')
    }
    requests_col.insert_one(new_dict)
    return redirect(url_for('my_profile.mongodb_func'))

@My_profile.route('/db_delete', methods=['POST'])
def delete_func():
    requests_col.delete_one({'userName':session.get('username'),
                             'reques': request.form.get('category')})
    return redirect(url_for('my_profile.mongodb_func'))
