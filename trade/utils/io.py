import os
import pandas as pd

def read_data(filename, dataformat='csv', header=0, index=None):
    """
    reads the file. chooses what way to read based on dataformat.
    """
    if dataformat == 'csv':
        return pd.read_csv(filename, sep=',', index_col=index, header=header)
    elif dataformat == 'tsv':
        return pd.read_csv(filename, sep='\t', index_col=index, header=header)
    # elif dataformat == 'npy':
    #     return np.load(filename)
    # elif dataformat == 'pth':
    #     return torch.load(filename)
    # elif dataformat == 'json':
    #     with open(filename, 'r') as file:
            # return json.load(file)
    else:
        raise ValueError('Input file type ', dataformat, ' is not supported')

def write_data(filename, obj, dataformat='csv', header=True, index=False):
    """
    writes the object to given filename. chooses what way to write 
    based on dataformat.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if dataformat == 'csv':
        obj.to_csv(filename, sep=',', index=index, header=header)
    elif dataformat == 'tsv':
        obj.to_csv(filename, sep='\t', index=index, header=header)
    # elif dataformat == 'npy':
    #     np.save(filename, obj)
    # elif dataformat == 'pth':
    #     torch.save(obj.state_dict(), filename)
    # elif dataformat == 'json':
    #     with open(filename, 'w') as file:
    #         json.dump(obj, file, indent=4)
    else:
        raise ValueError('Input file type ', dataformat, ' is not supported for', type(obj) )