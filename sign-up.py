__author__ = 'ada'

from flask import Flask
from flask import render_template, redirect, request
from random import random

app = Flask(__name__)

@app.route('/')
def index():

    if random() <= 0.5:
        return render_template('index.html', message = "Take your startup to the next level, with Podio")
    else:
        return render_template('index.html', message = "Upgrade your startup, with Podio")


@app.route('/signup', methods=['POST'])
def signin():
    print request.form['user[mail]']

    statistics = open('statistics','a')
    statistics.write(request.form['message'] + '\n' + request.form['used-form'] +'\n')
    statistics.close()


    return redirect("https://podio.com/signup", code=302)
    # 307 if you want to redirect as a POST request


@app.route('/statistics2', methods=['GET'])
def statistics2():
    statistics = open('statistics','r')
    d = dict()

    for line in statistics:
        if line in d:
            d[line] += 1
        else:
            d[line] = 1

    return render_template('statistics.html', stats_dict=d)


if __name__ == '__main__':
    app.run(debug=True)
