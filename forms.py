from flask_wtf import FlaskForm
from wtforms import SubmitField,SelectField,validators,FloatField
from wtforms.fields.html5 import DateField,IntegerRangeField

class SignUpForm(FlaskForm):
    airlineValues = ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet','Multiple carriers',
                'GoAir', 'Vistara', 'Air Asia', 'Vistara Premium economy', 'Jet Airways Business',
                'Multiple carriers Premium economy', 'Trujet']


    sourceValues = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']

    destinationValues = ['Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Hyderabad']

    stopValues = ['non-stop', '1 stop', '2 stops' ,'3 stops', '4 stops']

    Airline = SelectField('Select Your AirLine Service ', choices=airlineValues)
    Source = SelectField('Select Source ', choices=sourceValues)
    Destination = SelectField('Select Destination ', choices=destinationValues)
    Total_Stops = SelectField('Select Total Stops ', choices=stopValues )
    Total_Duration = FloatField('Enter Total Duration', validators=[validators.Required()])
    Departure_Date = DateField('Enter Departure Date: ', format='%m/%d/%Y', validators=[validators.data_required()])

    submit = SubmitField(' Calculate Total Flight Fare! ')
