# All Necessary Library Imports
from DatabaseConnection.Database import Connector
import threading
from joblib import load
import pandas as pd
import numpy as np
from CustomLogger.logger import Logger

logging = Logger('logFiles/test.log')

class ThreadWithResult(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)
        super().__init__(group=group, target=function, name=name, daemon=daemon)

def backend(result):
    """
    :DESC: This function send data into database. If table is not present it creates one and adds data.
    :param result: provided by Thread creater
    :return: None
    """

    logging.info('INFO', 'Data for Database: {}'.format(result))
    result['Journey_month'] = int(result['Journey_month'])
    result['Journey_day'] = int(result['Journey_day'])
    result['Total_Duration'] = int(result['Total_Duration'])

    load_data = Connector()
    try:
        load_data.master()
        load_data.addData(result)
    except:
        load_data.addData(result)
    finally:
        logging.info('INFO', 'Data retrieved')

def featureCorrection(result):
    """
    :DESC: This Function takes data provided by user and performs OneHot Endcoding + Feature Scaling
           It uses two files 1) outlier removed file 2) FeatureScaler File

    :param result: Provided by Thread creater
    :return: Sends Data to front end
    """

    logging.info('INFO', 'Data received From User : {}'.format(result))
    result['Journey_month'] = result['Departure_Date'].split('-')[1]
    result['Journey_day'] = result['Departure_Date'].split('-')[2]
    result.pop('submit')
    result.pop('Departure_Date')
    logging.info('INFO', 'Data Cleaned : {}'.format(result))

    frame = pd.read_csv("Outlier_removed.csv")
    frame = frame.drop('Price', axis=1)
    frame = frame.append(result, ignore_index=True)
    logging.info('INFO', 'Frame created and data appended')

    frame[['Journey_day', 'Journey_month']] = frame[['Journey_day', 'Journey_month']].astype('int64')
    frame['Total_Duration'] = frame['Total_Duration'].astype('float64')

    frame = pd.get_dummies(frame, drop_first=True)
    logging.info('INFO', 'Dummy variables created from received data')
    scaler = load("FeatureScaler.pkl")
    result = frame.iloc[-1].values
    result = scaler.transform(np.reshape(result, (1, -1)))
    logging.info('INFO', 'Data scaled and sent for prediction')

    return result

def getResult(result):
    """
    :Desc: This function creates thread for featureCorrection,backend
    :param result: User Provided
    :return: Sends data into featureCorrection,backend
    """
    logging.info('INFO', 'Threading Called !')
    in1 = result
    in2 = result
    thread1 = ThreadWithResult(target=featureCorrection, args=(in1,))
    thread2 = ThreadWithResult(target=backend, args=(in2,))
    logging.info('INFO', 'Threading Created !')
    thread1.start()
    thread2.start()
    logging.info('INFO', 'Threading Started !')
    thread1.join()
    thread2.join()
    logging.info('INFO', 'Threading join !')
    return thread1.result



