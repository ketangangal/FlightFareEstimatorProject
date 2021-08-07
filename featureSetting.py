from joblib import load
import pandas as pd
import numpy as np

def featureCorrection(result):

    frame = pd.read_csv("Outlier_removed.csv")
    frame = frame.drop('Price', axis=1)

    result['Journey_month'] = result['Departure_Date'].split('-')[1]
    result['Journey_day'] = result['Departure_Date'].split('-')[2]
    result.pop('submit')
    result.pop('Departure_Date')

    frame = frame.append(result, ignore_index=True)

    frame[['Journey_day', 'Journey_month']] = frame[['Journey_day', 'Journey_month']].astype('int64')
    frame['Total_Duration'] = frame['Total_Duration'].astype('float64')

    frame = pd.get_dummies(frame, drop_first=True)
    scaler = load("FeatureScaler.pkl")
    result = frame.iloc[-1].values
    result = scaler.transform(np.reshape(result, (1, -1)))

    return result
