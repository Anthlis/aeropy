## AeroPy README #

### What is it?

AeroPy is a small Flask app to aid the preparation of flight navigation tasks for private flying. That is; get the weather, do weight and balance checks and plan the navigation route. Not for operational use, but purely as a theme to develop my understanding of Python and the Flask web framework.

* In development: 
    - Flying Weather report, get NZCH TAF & METAR reports and plot a windrose diagram for the wind direction and strength.
    - Weight and Balance calculations for ZK-EBZ and check within limits defined by a plot diagram.
    - Currency checker (add 90days from last flight and compare with today), currency in doing manoeuvers etc.
    - Logbook API, for checking how many hours in a particular aircraft type or rego or how many hours flown since last BFR.
    - Compass turns mental maths checker
    - Navigation PLOG worker, 
    	(The hard one - implementing a maths wind triangle into Flask WTF-forms, working out headings, bearings, S/D/T problems.

This repo is a copy of the files deployed as a Flask web application on www.pythonanywhere.com as faifieldlabs.pythonanywhere.com.

### Install

	$ python3 -m venv venv && source venv/bin/activate
	$ pip install -r requirements.txt

### Run 

	$ python flask_app.py
	# browse to http://127.0.0.1:5000/

### Tests 

(Still learning about this)

	python -m unittest test/test_app.py
 
