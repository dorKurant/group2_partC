from flask import Blueprint, render_template,request,session
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import redirect, url_for

uri = "mongodb+srv://d8o8r8:K8u8r8a8n8t8@cluster0.prckjxg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['mydatabase']  # יצירת דאטה בייס
customers_col = mydatabase['customers']  # מצביע ללקוחות

Log_in=Blueprint(
    'log_in',
    __name__,
    static_folder='static',
    static_url_path='/log_in',
    template_folder='templates'
)
@Log_in.route('/logout', methods=['GET'])
def logout_func():
    session['logged_in'] = False
    session['username'] = ''
    session['email'] = ''
    return redirect(url_for('log_in.Log_in_page'))

@Log_in.route('/Log_in', methods=['GET','POST'])
@Log_in.route('/', methods=['GET','POST'])
def Log_in_page():  # put application's code here
    session['logged_in'] = False
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        costumer=customers_col.find_one({'userName':username,'password':password})

        if not username:
            return render_template('log_in.html', page_name='Log In', message="please insert your username")
        if not password:
            return render_template('log_in.html', page_name='Log In', message="please insert your password")
        if costumer is None:
            return render_template('log_in.html', page_name='Log In', message="username or password dosent exist")
        else:
            session['username'] = username
            session['logged_in'] = True
            # print(session['logged_in'])
            return render_template('sfs.html', page_name='sfs', post_username=username)
    return render_template('log_in.html', page_name='Log In')