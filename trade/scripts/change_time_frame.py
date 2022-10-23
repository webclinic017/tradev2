from re import L
import this
import pandas as pd
import os
import _initpaths
import glob
import datetime

from trade.utils.io import write_data, read_data
this_dir = os.path.dirname(os.path.abspath(__file__))

for filename in glob.glob(os.path.join(this_dir, '../../data/nifty50/*')):
    print(filename)
    df = read_data(filename)
    df['Date'] = pd.to_datetime(df['Date'])

    df = df[df['Date']>datetime.datetime(2017, 1, 1)]
    filename_out = filename.replace('nifty50','nifty50_5year')
    write_data(filename=filename_out, obj=df)
    # file = 
_=123

# xargs -a ../ind_nifty50list.csv cp -t ../nifty50