import pandas as pd
import numpy as np
#import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

train_df = pd.read_csv(r'C:\Users\grety\Desktop\Git_Hub\Repositories\final-project\Resources\trainn.csv')

train_df.drop(['ID'],axis=1,inplace=True)

# Random Forest Regressor - MEDV, RM, PTRATIO, NOX, TAX
X = train_df.iloc[:,[-1,5,10,4,9]]
y = train_df.iloc[:,[-1]]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=0)

from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor()
reg.fit(X_train,y_train)

y_pred = reg.predict(X_train)

print("Testing Accuracy:",reg.score(X_test,y_test)*100)

# Visualizing the differences between actual prices and predicted values
plt.scatter(y_train, y_pred)
plt.xlabel("Prices")
plt.ylabel("Predicted prices")
plt.title("Prices vs Predicted prices")
plt.show()


