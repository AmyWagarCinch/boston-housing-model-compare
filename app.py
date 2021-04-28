from flask import Flask
from flask import request
from flask import render_template
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import try_model

app = Flask(__name__)

## load the model from disk
#loaded_model = pickle.load(open('homepriceModel_trained.sav', 'rb'))
#result = loaded_model.score(X_test, y_test)
#Check the pickle file by inputing the variables
#model = pickle.load(open('trained_model.pkl','rb'))
bloop = []

@app.route("/")
@app.route("/home")
def home():
    
    return render_template('home.html')

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')
    #result = model.predict([[55, 18, 0, 1, 1]])
    #return render_template('about.html', prediction_text='Apparently this worked: $ {}'.format(result))
    

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    #def passIn():

    bloop = [int(x) for x in request.form.values()]
    #froop = request.form.labels()
        #return bloop

    output = try_model.try_function(bloop)
    #return render_template('about.html',prediction_text='Testing Model Accuracy: {}'.format(variable))
    #return render_template('about.html',prediction_text=f"{output} for {froop}")
    return render_template('about.html',prediction_text=output)

if __name__ == "__main__":
    app.run(port=5001)