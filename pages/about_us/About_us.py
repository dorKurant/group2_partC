from flask import Blueprint, render_template

about_us=Blueprint(
    'about_us',
    __name__,
    static_folder='static',
    static_url_path='/About_us',
    template_folder='templates'
)

@about_us.route('/About_us')
def about_us_page():  # put application's code here
    return render_template('about_us.html', page_name='About Us')