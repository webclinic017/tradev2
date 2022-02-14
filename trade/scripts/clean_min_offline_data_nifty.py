import datetime as dt
import jugaad_data as jd
from jugaad_data.nse import index_csv, index_df
import os
import _initpaths

from trade.utils.io import write_data, read_data
this_dir = os.path.dirname(os.path.abspath(__file__))

import glob

for path in glob.glob(os.path.join(this_dir,'data/min_data_nifty/*/*')):
    if 'BNF' in path:
        continue
    # print(path)
    df = read_data(path,header=None)
    if len(df.columns)==9:
        df.columns = ['index_name','date_','time','open','high','low','close','volume','_']
    elif len(df.columns)==7:
        df.columns = ['index_name','date_','time','open','high','low','close']
        df['volume'] = 0
    elif len(df.columns)==8:
        df.columns = ['index_name','date_','time','open','high','low','close','volume']
    else:
        print(len(df.columns))
        raise
    # print(df.tail())
    df = df.groupby('date_')

    # iterate over each group
    for group_name, df_group in df:
        print(group_name)
        df_group['date'] = df_group[['date_','time']].apply(
            lambda x: dt.datetime.strptime(f'{x[0]}-{x[1]}', '%Y%m%d-%H:%M'), axis=1)
        # print('\nCREATE TABLE {}('.format(group_name))
        # print(df_group)
        # print(group_name)
        date = dt.datetime.strptime(str(group_name), '%Y%m%d')
        file_name = os.path.join(this_dir,f'data/min_data_nifty_clean/{date.year}/{date.month}/{date.day}.csv')
        print(file_name)
        df_group = df_group[['date','open','high','low','close','volume']]
        write_data(df_group,file_name)