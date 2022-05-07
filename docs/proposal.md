# Project Proposal

## 1. Motivation & Objective

Human Activity Recognition (HAR) is the process of automatically inferring a user’s activity (e.g., walking, sitting, standing) based on sensor data (e.g., accelerometers, gyroscope) typically from devices like smartphones and smartwatches. However traditional machine learning method’s performance decreases significantly in real-life applications due to the problem of data missingness. Data Missingness in sensors typically happens due to power limitation, hardware failure, transmission packet loss, and many more. Our goal through this project is two folds, first is to investigate the data missingness distribution for Inertial Measurement Units (IMU). Secondly, it is to build robust models that not only impute the IMU signals but also successfully perform the task of activity classification.

## 2. State of the Art & Its Limitations

How is it done today, and what are the limits of current practice?

## 3. Novelty & Rationale

What is new in your approach and why do you think it will be successful?

## 4. Potential Impact

HAR classification from IMU signals is applicable in various domains like sports, eldercare, and healthcare. However, these HAR models, when deployed on edge devices, won’t necessarily perform validation on “clean data.” Missing data is an inherent problem in many applications involving sensors, and therefore mitigating it can have tremendous implications.

Following are the potential impact that our work can make: 

- **Robust HAR on-edge**: Our work can improve the performance of edge devices in scenarios where power constraints, channel noise, and other interferences cause data missingness. 
- **IMUs beyond HAR**: IMU signals from smartphones and smartwatches are also used for various other applications like gait classification, step counting, and gesture control; therefore, the reconstructed signals from our imputation method can be utilized for the performance of the abovementioned tasks. 
- **Generalized time-series missingness**: We make very few assumptions about the signals and their missingness (experiment over multiple types of missingness); therefore, it is also possible to extend these robust models to other time-series-based problems like stock market prediction and EEG/ ECG classification, and COVID-spread forecast.


## 5. Challenges

Some of the challenges and risks associated with this research project are:

- Performing a thorough investigation and having a deep understanding of the various types of IMU data missingness distribution. Although it is easy to assume the missingness distribution to be random (MAR, MCAR, MNAR) like in most literature, it might not necessarily be the case in real-life applications.
- Making assumptions about the missingness distribution (e.g., fading channel) can also be a potential risk because it can make the model biased toward such missingness. 
- Most State of the Art implementations on data imputation deal with low-frequency biological data sets like medical records. A potential challenge would be to extend similar models and ideas for high-frequency data from IMUs for the task of HAR.   

## 6. Requirements for Success

What skills and resources are necessary to perform the project?

## 7. Metrics of Success

What are metrics by which you would check for success?

## 8. Execution Plan

The project implementation can be broken down into the following tasks:

- Data preprocessing
- IMU data missingness analysis
	- Random - MAR, MCAR, MNAR
	- Prior distribution’s knowledge-based missingness
- Baseline model implementations
	- default value (e.g., 0), mean, median, mode, smoothing, interpolation, KNN
	- Forward filling
	- Mask (indicator) variable approach
- Replicating State-of-the-Art (SOTA) implementation
- Performance metrics, comparative analysis, and visualizations 

## 9. Related Work

### 9.a. Papers

List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).

### 9.b. Datasets

List datasets that you have identified and plan to use. Provide references (with full citation in the References section below).

### 9.c. Software

List softwate that you have identified and plan to use. Provide references (with full citation in the References section below).

## 10. References

List references correspondign to citations in your text above. For papers please include full citation and URL. For datasets and software include name and URL.
