#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Important Modules
from flask import Flask,render_template, url_for ,flash , redirect
import pickle
from flask import request
import numpy as np




import os
from flask import send_from_directory


#from this import SQLAlchemy
app=Flask(__name__,template_folder='template')




@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html")
 


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cancer")
def cancer():
    return render_template("cancer.html")


@app.route("/diabetes")
def diabetes():
    #if form.validate_on_submit():
    return render_template("diabetes.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")


@app.route("/liver")
def liver():
    #if form.validate_on_submit():
    return render_template("liver.html")

@app.route("/kidney")
def kidney():
    #if form.validate_on_submit():
    return render_template("kidney.html")



def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):#Diabetes
        loaded_model = pickle.load(open("Diabetes_model.pkl","rb"))
        result = loaded_model.predict(to_predict)
    elif(size==30):#Cancer
        loaded_model = pickle.load(open("Cancer_model.pkl","rb"))
        result = loaded_model.predict(to_predict)
    elif(size==18):#Kidney
        loaded_model = pickle.load(open("kidney_model.pkl","rb"))
        result = loaded_model.predict(to_predict)
    elif(size==10):#Liver
        loaded_model = pickle.load(open("Liver_model.pkl","rb"))
        result = loaded_model.predict(to_predict)
    elif(size==13):#Heart
        loaded_model = pickle.load(open("Heart_model.pkl","rb"))
        result =loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ["POST"])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        
        if(len(to_predict_list)==30):#Cancer
            result = ValuePredictor(to_predict_list,30)
            if(int(result)==1):
                prediction='Benign tumor has been detected in the patient.'
            else:
                prediction='Malignant tumor has been detected in the patient.'
                
        elif(len(to_predict_list)==8):#Daiabtes
            result = ValuePredictor(to_predict_list,8)
            if(int(result)==1):
                prediction='The patient is Diabetic.'
            else:
                prediction='The patient is Non-Diabetic.'
                
        elif(len(to_predict_list)==18):#kidney
            result = ValuePredictor(to_predict_list,18)
            if(int(result)==1):
                prediction='Chronic kidney disease has been detected in the patient.'
            else:
                prediction='No chronic kidney disease has been detected in the patient.'
                
        elif(len(to_predict_list)==13):#heart
            result = ValuePredictor(to_predict_list,13)
            if(int(result)==1):
                prediction="The patient's heart seems to be healthy."
            else:
                prediction="The patient's heart does not seems to be healthy."
                
        elif(len(to_predict_list)==10):#liver
            result = ValuePredictor(to_predict_list,10)
            if(int(result)==1):
                prediction="The patient's liver seems to be healthy."
            else:
                prediction="The patient's liver does not seems to be healthy."



    return(render_template("result.html", prediction=prediction))

if __name__ == "__main__":
    app.run(debug=True)

