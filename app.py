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
model = pickle.load(open('trained_model.pkl','rb'))

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
    #select = request.form.get('value')
    #return select
    #return(str(select)) //yields "none"

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #return final_features // TypeError: The view function did not return a valid response. The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a list.
    #return(str(final_features)) // returned [array([3, 4, 5])] on http://127.0.0.1:5001/submit
    return render_template('about.html',prediction_text='Did this work? {}'.format(final_features))
    
    #variable = try_model.try_function()
    #return render_template('about.html',prediction_text='Did this work? {}'.format(variable))

if __name__ == "__main__":
    app.run(port=5001)