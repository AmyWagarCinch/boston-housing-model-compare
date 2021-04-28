import pandas as pd
import numpy as np
#import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

#bloop = []

def try_function(bloop):
    train_df = pd.read_csv(r'C:\Users\grety\Desktop\Git_Hub\Repositories\final-project\Resources\trainn.csv')

    train_df.drop(['ID'],axis=1,inplace=True)

    # Random Forest Regressor 
    #bloop = [-1,5,10,4,9]

    X = train_df.iloc[:,bloop]
    y = train_df.iloc[:,[-1]]

    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=0)

    from sklearn.ensemble import RandomForestRegressor
    reg = RandomForestRegressor()
    reg.fit(X_train,y_train)

    y_pred = reg.predict(X_train)

    ta = reg.score(X_test,y_test)*100

    #return "Testing Accuracy:",ta

    # Visualizing the differences between actual prices and predicted values
    plt.scatter(y_train, y_pred)
    plt.xlabel("Prices")
    plt.ylabel("Predicted prices")
    plt.title("Prices vs Predicted prices")
    #plt.show()
    final_num = round(ta,2)
    #return plt
    result = f'Testing Accuracy: {final_num}%'
    #return result, plt.show()
    return result


