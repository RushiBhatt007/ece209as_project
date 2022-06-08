import numpy as np
import pandas as pd

def uci(
) -> dict:

    """
    Loads UCI HAR dataset.

    Returns:
        A dictionnary containing:
            - 'X': Windowed timeseries X.
            - 'y': Corresponding labels for timeseries.
    """

    train_directory = "D:/GitHub/ece209as_project/data/UCI_HAR_Dataset/train/Inertial_Signals/"

    train_files = ["body_acc_x_train.txt", "body_acc_y_train.txt", "body_acc_z_train.txt", 
            "body_gyro_x_train.txt", "body_gyro_y_train.txt", "body_gyro_z_train.txt", 
            "body_acc_x_train.txt", "body_acc_y_train.txt", "body_acc_z_train.txt"]

    train_df = []
    train_y = pd.read_csv("D:/GitHub/ece209as_project/data/UCI_HAR_Dataset/train/y_train.txt", header=None)

    test_directory = "D:/GitHub/ece209as_project/data/UCI_HAR_Dataset/test/Inertial_Signals/"

    test_files = ["body_acc_x_test.txt", "body_acc_y_test.txt", "body_acc_z_test.txt", 
            "body_gyro_x_test.txt", "body_gyro_y_test.txt", "body_gyro_z_test.txt", 
            "body_acc_x_test.txt", "body_acc_y_test.txt", "body_acc_z_test.txt"]

    test_df = []
    test_y = pd.read_csv("D:/GitHub/ece209as_project/data/UCI_HAR_Dataset/test/y_test.txt", header=None)


    for train_file in train_files:
        df = pd.read_csv(train_directory+train_file, delim_whitespace=True, header=None)
        train_df.append(np.array(df))

    for test_file in test_files:
        df = pd.read_csv(test_directory+test_file, delim_whitespace=True, header=None)
        test_df.append(np.array(df))

    train_X = np.array(train_df).reshape([len(train_y), 128, 9])
    test_X = np.array(test_df).reshape([len(test_y), 128, 9])

    X = np.concatenate((train_X, test_X), axis=0)
    y = np.concatenate((train_y, test_y), axis=0)

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
