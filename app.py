import flask
from flask import Flask, render_template, request
import pickle
import sklearn
#from flask_ngrok import run_with_ngrok
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

model = pickle.load(open('flightpriceRFR.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', "POST"])
def predict():
    input_values = [float(x) for x in request.form.values()]
    input_values.append(1)
    input_values.append(1)
    input_values.append(1)
    input_values.append(1)
    inp_features = [input_values]
    print(inp_features)
    prediction = model.predict(inp_features)
    
    return render_template('index.html', prediction_text=prediction)
if __name__=='__main__':
    app.run(debug=True)