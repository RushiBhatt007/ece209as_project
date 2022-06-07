import numpy as np


def zero_filling_imputation(
    X:np.ndarray
) -> np.ndarray:
    """
    Performs zero filling imputation - replaces all NaN values with 0s.

    Args:
        X : Data for which zero filling imputation is to be performed.

    Returns:
        X_zero_imputed : X imputed with 0s.

    """
    X_zero_imputed = X.copy()
    X_zero_imputed[np.isnan(X_zero_imputed)] = 0
    return X_zero_imputed


def mean_imputation(
    X:np.ndarray
) -> np.ndarray:
    """
    Performs mean imputation - replaces all NaN values with means.

    Args:
        X : Data for which mean imputation is to be performed.

    Returns:
        X_zero_imputed : X imputed with means.

    """
    X_mean_imputed = X.copy()
    n, d, z = X_mean_imputed.shape

    for i in range(n):
        X_mean_temp = X_mean_imputed[i,:,:]
        X_mean = np.nanmean(X_mean_temp, axis=0)
        for j in range(z):
            X_mean_temp[np.isnan(X_mean_temp)] = X_mean[j]

    return X_mean_imputed


def median_imputation(
    X:np.ndarray
) -> np.ndarray:
    """
    Performs median imputation - replaces all NaN values with medians.

    Args:
        X : Data for which median imputation is to be performed.

    Returns:
        X_zero_imputed : X imputed with medians.

    """
    X_median_imputed = X.copy()
    n, d, z = X_median_imputed.shape

    for i in range(n):
        X_median_temp = X_median_imputed[i,:,:]
        X_median = np.nanmedian(X_median_temp, axis=0)
        for j in range(z):
            X_median_temp[np.isnan(X_median_temp)] = X_median[j]

    return X_median_imputed

