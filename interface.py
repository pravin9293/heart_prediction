import config
from flask import Flask, request, jsonify, render_template
from utils import HeartDisease
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    # return "Heart Disease Prediction"


@app.route('/predict_disease', methods = ['GET','POST'])
def predict_disease():
    try:
        if request.method == 'POST':
            data = request.form.get

            print("Data :: ", data)
            age      = eval(data('age'))
            sex      = eval(data('sex'))
            cp       = eval(data('cp'))
            trestbps = eval(data('trestbps'))
            chol     = eval(data('chol'))
            fbs      = int(data('fbs'))
            restecg  = eval(data('restecg'))
            thalach  = eval(data('thalach'))
            exang    = eval(data('exang'))
            oldpeak  = eval(data('oldpeak'))
            slope    = eval(data('slope'))
            ca       = eval(data('ca'))
            thal     = eval(data('thal'))

            heart_diseas = HeartDisease(age,sex,cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
            predict_disease = heart_diseas.get_heart_disease_prediction()

            # return  jsonify({"Result" : f"Heart Disease Prediction class is  : {predict_disease}"})
            if predict_disease == 0:
                return render_template('index.html', prediction = "NO")
            else:
                return render_template('index.html', prediction = "YES")

        else:
            data = request.args.get

            print("Data :: ", data)
            age      = eval(data('age'))
            sex      = eval(data('sex'))
            cp       = eval(data('cp'))
            trestbps = eval(data('trestbps'))
            chol     = eval(data('chol'))
            fbs      = int(data('fbs'))
            restecg  = eval(data('restecg'))
            thalach  = eval(data('thalach'))
            exang    = eval(data('exang'))
            oldpeak  = eval(data('oldpeak'))
            slope    = eval(data('slope'))
            ca       = eval(data('ca'))
            thal     = eval(data('thal'))

            heart_diseas = HeartDisease(age,sex,cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
            predict_disease = heart_diseas.get_heart_disease_prediction()

            # return  jsonify({"Result" : f"Heart Disease Prediction class is  : {predict_disease}"})
            if predict_disease == 0:
                return render_template('index.html', prediction = "NO")
            else:
                return render_template('index.html', prediction = "YES")

    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})



if __name__ =='__main__':
    app.run(host = '0.0.0.0', debug = True, port= config.PORT)