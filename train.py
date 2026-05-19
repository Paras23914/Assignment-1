import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
df= pd.read_csv("Weather.csv")
df.head()
df= df[[
    "Temp (C)",
    "Rel Hum (%)",
    "Wind Spd (km/h)",
    "Stn Press (kPa)"
]]

df=df.dropna()
X=df
Y=df["Temp (C)"].shift(-1)

X = X[:-1]
Y = Y[:-1]

Xtrain,Xtest,Ytrain,Ytest=train_test_split(
    X,Y,test_size=0.2,random_state=42
)

randomforest=RandomForestRegressor()
randomforest.fit(Xtrain,Ytrain)
prediction=randomforest.predict(Xtest)

print("Mean Absolute Error be : ",mean_absolute_error(Ytest,prediction))

joblib.dump(randomforest,"weather_model.pkl")


