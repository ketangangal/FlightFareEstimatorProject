import numpy as np
from flask import Flask, request, render_template
from forms import SignUpForm
from joblib import load
from featureSetting import featureCorrection

# flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC235G5K8'
# connect post api call ---> predict() function


@app.route("/", methods = ['GET','POST'])
def home():
    form = SignUpForm()
    if request.method == 'POST':
        if form.is_submitted():
            model = load('FinalModel.pkl')
            result = request.form.to_dict()
            result = featureCorrection(result)
            output = model.predict(result)
            minfare = np.round(output)-1000
            maxfare = np.round(output)+1000

            return render_template('index.html', form=form,value1=int(minfare),value2=int(maxfare))

    return render_template('index.html',form=form,value1=None,value2=None)


if __name__ == "__main__":
    app.run(debug=True)

