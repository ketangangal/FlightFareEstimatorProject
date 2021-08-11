import logging
import numpy as np
from Database import Connector
from flask import Flask, request, render_template
from forms import SignUpForm
from joblib import load
from featureSetting import getResult

# flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC235G5K8'
# connect post api call ---> predict() function

# Root Logger

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                   format=' %(name)s : %(asctime)s : %(filename)s : %(message)s ', filemode='w')

@app.route("/", methods = ['GET','POST'])
def home():
    form = SignUpForm()
    if request.method == 'POST':
        logging.info('Requested method : POST')
        if form.is_submitted():
            model = load('FinalModel.pkl')
            logging.info('Pickle Model Loaded')
            result = request.form.to_dict()
            try:
                logging.info('Data Converted ')
                #result['Total_Duration'] = int(result['Total_Duration'])
                result = getResult(result)
                output = model.predict(result)
                logging.info('Prediction success!')
                minfare = np.round(output) - 1000
                maxfare = np.round(output) + 1000
                logging.info('Output displayed!')
                return render_template('index.html', form=form, value1=int(minfare), value2=int(maxfare),Rs='Rs')
            except:
                logging.error("Excepted integer got String")
                return render_template('index.html', form=form,value1='Give Duration In numbers Only!')


    return render_template('index.html',form=form,value1=None,value2=None)

# Hidden database api
@app.route("/DatabaseData", methods = ['GET','POST'])
def test():
    heading = ("id", "Airline", "Source", "Day", "Month", "Destination", "Total_Duration","Total_Stops")
    data = Connector()
    return render_template('Databasedata.html', heading=heading, data=data.getData())



if __name__ == "__main__":
    app.run(debug=True)