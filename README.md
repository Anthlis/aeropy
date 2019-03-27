## AeroPy README #

### What is it?

AeroPy is a small Flask app to aid with private flying flight navigation preparation. Not for operational use, but purely as a theme to develop my understanding of Python and the Flask web framework.

* In development: 
    - Flying Weather report
    - Currency checker
    - Logbook API
    - Compass turns mental maths checker
    - Navigation PLOG worker

This repo is a copy of the files deployed as a Flask web application on www.pythonanywhere.com as faifieldlabs.pythonanywhere.com.

### Install

	$ python3 -m venv venv && source venv/bin/activate
	$ pip install -r requirements.txt

### Run 

	$ python flask_app.py
	# browse to http://127.0.0.1:5000/

### Tests (Still learning about this)

	python -m unittest test/test_app.py
 
