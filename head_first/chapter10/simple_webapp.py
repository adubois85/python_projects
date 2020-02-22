from flask import Flask, session
from chapter10.checker import check_logged_in

app = Flask(__name__)

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'

# @app.route('/status')
# def check_status() -> str:
#     if 'logged_in' in session:
#         return 'You are currently logged in.'
#     return 'You are NOT logged in.'

app.secret_key = 'MyKeyIsSecretYo'

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'

@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1.'

@app.route('/page1')
@check_logged_in
def page2() -> str:
    return 'This is page 2.'

@app.route('/page1')
@check_logged_in
def page3() -> str:
    return 'This is page 3.'

if __name__ == '__main__':
    app.run(debug=True)
