from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<h1>Hello Park Minwoo!</h1>"

@app.route('/profile')
def profile():
#     return "<h2>Park Minwoo's profile</h2>"
    dataObj = {
        'name' : "권나라"
        , 'list' : [
            'IT 초급 개발자', 'Back - Front 개발자' , '포스코 MES 3.0 작업중' , '한창 공부 중임.'
        ]
    }
    return render_template('profile.html' , data=dataObj)

if __name__ == '__main__' :
    app.run('0.0.0.0')