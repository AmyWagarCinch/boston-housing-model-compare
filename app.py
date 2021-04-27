from flask import Flask
from flask import request
from flask import render_template
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

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

@app.route("/about")
def about():
    result = model.predict([[55, 18, 0, 1, 1]])
    return render_template('about.html', prediction_text='Apparently this worked: $ {}'.format(result))
    

if __name__ == "__main__":
    app.run(port=5001)