import pickle
import json
import numpy as np
import pandas as pd
import datetime

__brands = None
__models = None
__brand_enc = None
__model_enc = None
__fuel_types = None
__data_columns = None
__xgbmodel = None

def predict_price(dist, model_year, fuel_type, brand, model):    
    try:
        fuel_index = __data_columns.index(fuel_type)
    except:
        fuel_index = -1

    current_yr = datetime.datetime.now().year
    age = current_yr - model_year

    x = np.zeros(len(__data_columns))
    x[0] = dist
    x[1] = age
    x[-1] = __model_enc[model]
    x[-2] = __brand_enc[brand]
    if fuel_index >= 0:
        x[fuel_index] = 1
    
    x = pd.DataFrame(x.reshape(1, -1), columns=__data_columns)
    
    return float(round(__xgbmodel.predict(x)[0], 2))


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __brands
    global __models
    global __brand_enc
    global __model_enc
    global __fuel_types

    with open("./artifacts/columns.json", "r") as f:
        data = json.load(f)
        __data_columns = data['data_columns']
        __brands = data['brands']
        __models = data['models']
        __brand_enc = data['brand_dict']
        __model_enc = data['model_dict']
        __fuel_types = data['fuel_types']

    global __xgbmodel
    if __xgbmodel is None:
        with open('./artifacts/car_resale_prediction.pickle', 'rb') as f:
            __xgbmodel = pickle.load(f)
    print("loading saved artifacts...done")

def get_brand_names():
    return __brands

def get_model_names():
    return __models

def get_fuel_types():
    return __fuel_types

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(predict_price(50000, 2010, 'Diesel', 'Maruti Suzuki', 'Swift'))
    print(predict_price(150000, 2009, 'Diesel', 'Toyota', 'Fortuner'))