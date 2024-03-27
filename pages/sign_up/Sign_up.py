from flask import Blueprint, render_template
from flask import render_template
from flask import request, session
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import redirect, url_for

uri = "mongodb+srv://d8o8r8:K8u8r8a8n8t8@cluster0.prckjxg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['mydatabase']  # יצירת דאטה בייס
customers_col = mydatabase['customers']  # מצביע ללקוחות

Sign_up=Blueprint(
    'sign_up',
    __name__,
    static_folder='static',
    static_url_path='/sign_up',
    template_folder='templates'
)

@Sign_up.route('/db_insert')
def insert_func():
    new_dict={
    'firstName':request.args['firstName'],
    'lastName':request.args['lastName'],
    'userName':request.args['userName'],
    'password':request.args['password'],
    'email':request.args['universityMail'],
    'phoneNumber':request.args['phoneNumber'],
    'address': request.args['address'],
    'credit_number':50
    }
    costumer = customers_col.find_one({'userName': request.args['userName']})
    print(costumer)
    if not new_dict['firstName']:
        return render_template('Sign_Up.html',page_name='Sign up',message="please enter your first name")
    if not new_dict['lastName']:
        return render_template('Sign_Up.html',page_name='Sign up',message="please enter your last name")
    if not new_dict['userName']:
        return render_template('Sign_Up.html', page_name='Sign up', message="please enter your userName")
    if not new_dict['password']:
        return render_template('Sign_Up.html', page_name='Sign up', message="please enter your password")
    if not new_dict['email']:
        return render_template('Sign_Up.html', page_name='Sign up', message="please enter your email")
    if not new_dict['phoneNumber'] or len(new_dict['phoneNumber']) != 10:
        return render_template('Sign_Up.html', page_name='Sign up', message="please enter your valid phoneNumber")
    if not new_dict['email']:
        return render_template('Sign_Up.html', page_name='Sign up', message="please enter your address")

    # Validate phone number
    # if not new_dict['phoneNumber'].isdigit() or len(new_dict['phoneNumber']) != 10:
    #     return render_template('Sign_Up.html', page_name='Sign up', message="Phone number must be 10 digits")

    if costumer is None:
        customers_col.insert_one(new_dict)
        return render_template('Sign_Up.html', page_name='Sign up')
    else:
        return render_template('Sign_Up.html',page_name='Sign up',message="userName already exists")

@Sign_up.route('/Sign_up')
def sign_up_page():  # put application's code here
    return render_template('Sign_Up.html',page_name='Sign up')