from Database import Connector
import threading
from joblib import load
import pandas as pd
import numpy as np
import logging

class ThreadWithResult(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)
        super().__init__(group=group, target=function, name=name, daemon=daemon)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(' %(name)s : %(asctime)s : %(filename)s : %(message)s ')
fileHandler = logging.FileHandler('test.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

def backend(result):

    logger.info('Data for Database: {}'.format(result))
    result['Journey_month'] = int(result['Journey_month'])
    result['Journey_day'] = int(result['Journey_day'])
    result['Total_Duration'] = int(result['Total_Duration'])

    load_data = Connector()
    load_data.addData(result)
    logger.info('Data retrieved')

def featureCorrection(result):

    logger.info('Data received From User : {}'.format(result))
    result['Journey_month'] = result['Departure_Date'].split('-')[1]
    result['Journey_day'] = result['Departure_Date'].split('-')[2]
    result.pop('submit')
    result.pop('Departure_Date')
    logger.info('Data Cleaned : {}'.format(result))

    frame = pd.read_csv("Outlier_removed.csv")
    frame = frame.drop('Price', axis=1)
    frame = frame.append(result, ignore_index=True)
    logger.info('Frame created and data appended')

    frame[['Journey_day', 'Journey_month']] = frame[['Journey_day', 'Journey_month']].astype('int64')
    frame['Total_Duration'] = frame['Total_Duration'].astype('float64')

    frame = pd.get_dummies(frame, drop_first=True)
    logger.info('Dummy variables created from received data')
    scaler = load("FeatureScaler.pkl")
    result = frame.iloc[-1].values
    result = scaler.transform(np.reshape(result, (1, -1)))
    logger.info('Data scaled and sent for prediction')

    return result

def getResult(result):
    logger.info('Threading Called !')
    in1 = result
    in2 = result
    thread1 = ThreadWithResult(target=featureCorrection, args=(in1,))
    thread2 = ThreadWithResult(target=backend, args=(in2,))
    logger.info('Threading Created !')
    thread1.start()
    thread2.start()
    logger.info('Threading Started !')
    thread1.join()
    thread2.join()
    logger.info('Threading join !')
    return thread1.result



