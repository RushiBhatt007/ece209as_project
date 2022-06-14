import numpy as np
import pandas as pd

# load a single file as a numpy array
def load_file(filepath):
    dataframe = pd.read_csv(filepath, header=None, delim_whitespace=True)
    return dataframe.values

# load a list of files and return as a 3d numpy array
def load_group(filenames, prefix=''):
    loaded = list()
    for name in filenames:
        data = load_file(prefix + name)
        loaded.append(data)
    # stack group so that features are the 3rd dimension
    loaded = np.dstack(loaded)
    return loaded

# load a dataset group, such as train or test
def load_dataset_group(group, prefix=''):
    filepath = prefix + group + '/Inertial_Signals/'
    print('File Path : ',filepath)
    # load all 9 files as a single array
    filenames = list()
    # total acceleration
    filenames += ['total_acc_x_'+group+'.txt', 'total_acc_y_'+group+'.txt', 'total_acc_z_'+group+'.txt']
    # body acceleration
    filenames += ['body_acc_x_'+group+'.txt', 'body_acc_y_'+group+'.txt', 'body_acc_z_'+group+'.txt']
    # body gyroscope
    filenames += ['body_gyro_x_'+group+'.txt', 'body_gyro_y_'+group+'.txt', 'body_gyro_z_'+group+'.txt']
    # load input data
    X = load_group(filenames, filepath)
    # load class output
    y = load_file(prefix + group + '/y_'+group+'.txt')
    return X, y

def uci(
) -> dict:

    """
    Loads UCI HAR dataset.

    Returns:
        A dictionnary containing:
            - 'X': Windowed timeseries X.
            - 'y': Corresponding labels for timeseries.
    """

    X_train, y_train = load_dataset_group('train', 'D:/GitHub/ece209as_project/data/UCI_HAR_Dataset/')
    X_test, y_test = load_dataset_group('test', 'D:/GitHub/ece209as_project/data/UCI_HAR_Dataset/')

    X = np.concatenate((X_train, X_test), axis=0)
    y = np.concatenate((y_train, y_test), axis=0)

    return {"X": X, "y": y}


def pamaps2(
    window_size:int=40,
    drop_nan:bool=False
) -> dict:

    """
    Loads PAMAPS2 dataset.

    Args:
        mecha : Indicates window size for time series to be user. 40 by default
        drop_nan : Indicates if NaN values from original dataset to be dropped or not. False by defauly. Recommended True if using baseline methods with simulate.simulate_nan() functions, otherwise False works fine.

    Returns:
        A dictionnary containing:
            - 'X': Windowed timeseries X.
            - 'y': Corresponding labels for timeseries.
    """

    train_directory = "D:/GitHub/ece209as_project/data/PAMAP2_Dataset/Protocol"
    
    train_file_101 = "/subject101.dat"
    train_df = pd.read_csv(train_directory+train_file_101, delim_whitespace=True, header=None)
    y = np.array(train_df[1])
    X = np.array(train_df.drop(columns=[1,2]))

    train_files = ["/subject102.dat", "/subject103.dat",
                    "/subject104.dat", "/subject105.dat", "/subject106.dat",
                    "/subject107.dat", "/subject108.dat", "/subject109.dat"]

    for train_file in train_files:
        train_df = pd.read_csv(train_directory+train_file, delim_whitespace=True, header=None)
        y_temp = np.array(train_df[1])
        X_temp = np.array(train_df.drop(columns=[1,2]))
        X = np.concatenate((X, X_temp), axis=0)
        y = np.concatenate((y, y_temp), axis=0)
    
    if(drop_nan):
        nanIndex = np.argwhere(np.isnan(X))[:,0]
        X = np.delete(X, nanIndex, axis=0)
        y = np.delete(y, nanIndex, axis=0)

    return createWindows(X, y, window_size)


def createWindows(
    X:np.ndarray, 
    y:np.ndarray, 
    window_size:int) -> dict:
    
    X_w = []
    y_w = []
    i= 0

    while i<len(X):
        count = 0
        j = i
        while j<min(i+window_size, len(X)):
            if(y[int(j)] == y[int(i)]):
                count+=1
            else:
                break
            j=j+1
        if(count == window_size):
            X_w.append(X[int(i):int(i+window_size)])
            y_w.append(y[int(i)])
            i+=(window_size/2)
        else:
            i=i+1

    X_w = np.array(X_w)
    y_w = np.array(y_w)
    
    return {"X": X_w, "y": y_w}
