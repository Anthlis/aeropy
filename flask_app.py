
# AeroPy Flask website 2019

from flask import Flask, render_template
from flask import request
import requests
import os
from flask import send_from_directory
from bs4 import BeautifulSoup
from flask_bootstrap import Bootstrap
from compute import compute
from model import InputForm
from compute2 import compute2
from model2 import InputForm2
import pyjokes
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('initial.html')

@app.route('/pyjokes')
def pyjoke():
    joke = pyjokes.get_joke()
    time = 'Last updated > ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('pyjokes.html', joke=joke, time=time)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/form')
def my_form():
    return render_template('my-form.html')

@app.route('/form', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return render_template('my-form2.html', processed_text=processed_text)


@app.route("/Algorithm", methods=['GET', 'POST'])
def calculation():
    result = 0
    error = ''
    # you may want to customize your GET... in this case not applicable
    if request.method=='POST':
        # get the form data
        first = request.form['first']
        second = request.form['second']
        if first and second:
            try:
                # do your validation or logic here...
                if int(first)>10 or int(first)<1:
                    raise ValueError
                result = int(first) + int(second)
            except ValueError:
                # you may pass custom error message as you like
                error = 'Please input integer from 1-10 only.'
    # you render the template and pass the context result & error
    return render_template('Algorithm.html', result=result, error=error)

@app.route('/AeroPyWx')
def AeroPyWx():
    url = 'http://www.aviationweather.gov/adds/tafs/?station_ids=nzch&std_trans=standard&submit_both=Get+TAFs+and+METARs'
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    strings = []
    for font in soup.findAll('font'):
        strings.append(font.string)

    time = 'Last updated > ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template('AeroPyWx.html', soupLines=strings, time=time)

@app.route('/dev')
def dev():
    return render_template('dev.html')

@app.route("/Compass", methods=['GET', 'POST'])
def compass():
    result = 0
    error = ''

    if request.method=='POST':
        # get the form data
        first = request.form['first']
        second = request.form['second']

        if first and second:
            try:
                # do your validation or logic here...
                if int(first) > 360:
                    raise ValueError
                result = int(first) - int(second)
            except ValueError:
                # you may pass custom error message as you like
                error = 'You entered a value > 360 degrees'
    # you render the template and pass the context result & error
    return render_template('Compass.html', result=result, error=error)


# View
@app.route('/view_input', methods=['GET', 'POST'])
def maths():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r)
        return render_template("view_output.html", form=form, s=s)
    else:
        return render_template("view_input.html", form=form)

# View2
@app.route('/view2', methods=['GET', 'POST'])
def view2():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r)
    else:
        s = None

    return render_template("view2.html", form=form, s=s)

# View_3
@app.route('/view_table', methods=['GET', 'POST'])  #changed from /view3
def view3():
    form = InputForm2(request.form)
    if request.method == 'POST' and form.validate():
        result = compute2(form.A.data, form.b.data,
                         form.w.data, form.T.data)
    else:
        result = None

    return render_template('view_table.html', form=form, result=result) # changed from view3.html

if __name__ == '__main__':
    app.run(debug=True)