from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def train_model(df):
    X = np.array(range(len(df))).reshape(-1, 1)
    y = df["total"]
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_future(df, days=7):
    model = train_model(df)
    X_future = np.array(range(len(df), len(df) + days)).reshape(-1, 1)
    return model.predict(X_future)
