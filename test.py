from flask import Flask, render_template, request
from database_connection import login_validate, save_stock_details

app = Flask(__name__)


#dataList = [{'id': 1, 'name': 'Sadhat'}, {'id': 2, 'name': 'Hameed'}]


@app.route('/')
def hello_world():
    return render_template('login.html')


@app.route('/login', methods=['post'])
def login_check():
    loginform_data = request.form
    page = login_validate(loginform_data['username'], loginform_data['password'])
    return render_template(page, loginform_data=loginform_data)


@app.route('/farmers', methods=['post'])
def submit_farmer_details():
    save_stock_details(dict(request.form), request.form.getlist('bags'))
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
