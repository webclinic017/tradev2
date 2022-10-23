import datetime as dt
import os
this_dir = os.path.dirname(os.path.abspath(__file__))


def get_data_file(config, previous_day=False):
    if previous_day==False:
        filename = os.path.join(
            this_dir,
            f'../../output/prod/{config["data_feed"]["symbol_name"]}',
            dt.date.today().strftime('%Y/%m/%d.csv')
        )
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        output_file_object = open(filename,'w')
        #  if v is int and v>=0
        output_file_object.write(config['data_feed']['p']['header']+'\n')
        return output_file_object
    else:
        delta=1
        while True:
            filename = os.path.join(
                this_dir,
                f'../../output/prod/{config["data_feed"]["symbol_name"]}',
                (dt.date.today()-dt.timedelta(days = delta)).strftime('%Y/%m/%d.csv')
            )
            if os.path.exists(filename):
                output_file_object = open(filename,'r')
                break
            else:
                delta = delta+1
                continue
        return output_file_object

def get_result_files(config):
    if config['live']==True:
        filename_plot = os.path.join(
            this_dir,
            f'../../output/prod/{config["data_feed"]["symbol_name"]}',
            dt.date.today().strftime('%Y/%m/%d.png')
        )

        filename_pl = os.path.join(
            this_dir,
            f'../../output/prod/{config["data_feed"]["symbol_name"]}',
            dt.date.today().strftime('%Y/%m/%d.yaml')
        )
        os.makedirs(os.path.dirname(filename_plot), exist_ok=True)
    else:
        filename_plot = os.path.join(
            this_dir,
            f'../../output/offline/{config["testing_param"]}_{config["run_id"]}_{config["data_feed"]["symbol_name"]}.png'
        )

        filename_pl = os.path.join(
            this_dir,
            f'../../output/offline/{config["testing_param"]}_{config["run_id"]}_{config["data_feed"]["symbol_name"]}.yaml'
        )
        os.makedirs(os.path.dirname(filename_plot), exist_ok=True)
    return filename_plot, filename_pl