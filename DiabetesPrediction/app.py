from flask import Flask,render_template,request,Response
import pickle
import numpy as np


filename = 'diabetes-prediction-knn-model.pkl'
knn = pickle.load(open(filename,'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
'''
def diabetespredictor():
    preg = input("Number of Pregnancies eg. 0",type=NUMBER)
    glucose = input("Glucose (mg/dL) eg. 80",type=FLOAT)
    bp = input("Blood Pressure (mmHg) eg. 80", type=FLOAT)
    skint = input("Skin Thickness (mm) eg. 20", type=FLOAT)
    insulin = input("Insulin Level (IU/mL) eg. 80", type=FLOAT)
    bmi = input("Body Mass Index (kg/m²) eg. 23.1", type=FLOAT)
    dpf = input("Diabetes Pedigree Function eg. 0.52", type=FLOAT)
    age = input("Age (years) eg. 34", type=NUMBER)
    data = np.array([[preg, glucose, bp, skint, bmi, insulin, dpf, age]])
    my_prediction = knn.predict(data)
    if my_prediction == 1:
        #put_text("danger' Oops! You have DIABETES.:(")
    else :
        put_text("Great! You DON'T have diabetes.:)")
'''

@app.route('/predict',methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            preg = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bp = int(request.form['bloodpressure'])
            skint = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])

            data = np.array([[preg,glucose,bp,skint,insulin,bmi,dpf,age]])
            my_prediction = knn.predict(data)

            return  render_template('output.html',prediction=my_prediction)

    except ValueError:
        return Response("Error Occured! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)


if __name__ == '__main__':
    app.run(debug=True)
