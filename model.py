from wtforms import Form, FloatField, validators

class InputForm(Form):
    r = FloatField(validators=[validators.InputRequired()])

r = 0.0 # input
s = None # Output