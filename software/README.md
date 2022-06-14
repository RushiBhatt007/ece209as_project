## ❖ Installation
Install tsdb:
> pip install tsdb

Install pypots: 
> pip install pypots

## ❖ Description

### Main Notebooks
* Our_approach_UCIHAR.ipynb: contains all analysis done on our implementation of SAITS model
* BRITS_UCIHAR: contains all analysis done on BRITS model
* uci_baselime_imputation.ipynb: contains all analysis done on baseline model
* uci_baseline_varying_percentage_missingness: baseline models for 10%, 20% ...90% missingness rate
* pamaps2_mcar_mar_mnar.ipynb: mcar, mar and mnar analysis on pamaps2 dataset
* missingness_analysis.ipynb: basic analysis done on personal IMU phone data
* visualize_timeseries.ipynb: generated visual of imputation

### Utility code:
* dataload.py: loads both UCI HAR and PAMAPS2 dataset
* baseline.py: contains all baseline models
* simulate.py: artificial missingness: MCAR, MAR, MNAR

## ❖ Note
* We ran BRITS and SAITS models for several hundred epochs which takes a very long time, for short analysis change the epoch to smaller number between 1 and 5. (Approx. takes 15 min/ epoch for BRITS). Alternative could be to reduce the number of model parameters.
* Make sure that all background activity of system are closed when using PAMAPS2 dataset as it takes takes up close to 16 GB of RAM.
