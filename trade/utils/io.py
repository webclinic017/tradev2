import os
import pandas as pd

def write_data(filename, obj):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    ext = filename.split('.')[-1]
    if ext == 'csv':
        obj.to_csv(filename)

def read_data(filename):
    ext = filename.split('.')[-1]
    if ext == 'csv':
        return pd.read_csv(filename)
