from flask import Flask, redirect, url_for


# app.config.from_pyfile('settings.py')
app = Flask(__name__)
app.secret_key='123'

# Create a new client and connect to the server



# @app.route('/db_insert')
# def insert_func():
#     # to check if exists
#     # insert_one
#     my_dict = {
#         'name': request.args['name'],
#         'address': request.args['address'],
#         'rating': int(request.args['rating']),
#     }
#     customers_col.insert_one(my_dict)
#     return redirect(url_for('mongodb_func'))




from pages.about_us.About_us import about_us
app.register_blueprint(about_us)

from pages.contact_info.Contact_info import Contact_info
app.register_blueprint(Contact_info)

from pages.find_me_a_pro.Find_me_a_pro import Find_me_a_pro
app.register_blueprint(Find_me_a_pro)

from pages.log_in.Log_in import Log_in
app.register_blueprint(Log_in)

from pages.my_profile.My_profile import My_profile
app.register_blueprint(My_profile)

from pages.sfs.SFS import SFS
app.register_blueprint(SFS)

from pages.sign_up.Sign_up import Sign_up
app.register_blueprint(Sign_up)








if __name__ == '__main__':
    app.run(debug=True)
