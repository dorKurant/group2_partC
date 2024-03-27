from flask import Blueprint, render_template

SFS=Blueprint(
    'sfs',
    __name__,
    static_folder='static',
    static_url_path='/sfs',
    template_folder='templates'
)

@SFS.route('/SFS')
def sfs_page():  # put application's code here
    return render_template('sfs.html', page_name='sfs')