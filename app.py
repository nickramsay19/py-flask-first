from flask import Flask, render_template

app = Flask(__name__)

users = ['Nicholas Ramsay', 'Belle Delphine', 'Wadingo Wajahjah']

@app.route("/")
def index():
    return render_template('welcome.html', name='nick')

@app.route('/users/')
@app.route('/users/<id>')
def getUsers(id = None):
    if id == None:
        res = '<h1>Users:</h1><ul>'
        if len(users) < 1:
            return res + 'No users found'
        for user in users:
            res += '<li>' + user + '</li>'
        return res + '</ul>'

    try:
        return '<h1>' + users[int(id)] + '</h1>'
    except:
        return 'User not found'