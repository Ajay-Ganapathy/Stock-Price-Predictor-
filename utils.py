import numpy as np 
import joblib 


def preprocessdata(open,high,volume,low,adj_close):
    test_data = [[open,high,volume,low,adj_close] ]
    trained_model = joblib.load("model.pkl") 
    prediction = float(trained_model.predict(test_data) )

    return prediction 