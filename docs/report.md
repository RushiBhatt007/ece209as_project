# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

Traditional machine learning methods for Human Activity Recognition (HAR) are significantly impacted due to data missingness. Our goal through this project is to build robust models that not only impute these signals but also build robust classifiers that can infer HAR classes from these imputed signals. Recurrent Neural Networks (RNN) have been proven to work well with time-series data due to their ability to learn temporal features and dependencies. Therefore, one of the SOTA imputation architectures we have implemented for HAR is a Bidirectional RNN based on the BRITS architecture. Also, recently self-attention mechanism-based imputation models have been used in missing value imputation for multivariate time series. Therefore, another SOTA imputation architecture we have implemented is a self-attention mechanism-based SAITS architecture. Our overall goal is to perform a comparative study between baseline models like zero-filling, mean, and median imputation, and SOTA models like BRITS and SAITS, not just for missing value imputation; but also for the downstream task of HAR classification. Most research on imputation only focuses on random Missingness, also known as Missingness Completely at Random (MCAR); but IMU signals encounter other types of Missingness too, namely Missingness at Random (MAR) and Missingness Not at Random (MNAR). Therefore, through this project, we have also extensively evaluated these models on various missingness types, as well as varying missingness rates, all performed on two popular publicly available HAR datasets: UCI HAR and PAMAPS2.

# 1. Introduction

## 1.1 Motivation & Objective : What are you trying to do and why? (plain English without jargon)

Human Activity Recognition (HAR) is the process of automatically inferring a user’s activity (e.g., walking, sitting, standing) based on sensor data (e.g., accelerometers, gyroscope) typically from devices like smartphones and smartwatches. However, the traditional machine learning method’s performance decreases significantly in real-life applications due to the problem of data missingness. Data Missingness in sensors typically happens due to power limitation, hardware failure, transmission packet loss, and many more. Our goal through this project is twofold, first is to investigate the data missingness distribution for Inertial Measurement Units (IMU). Secondly, it is to build robust models that not only impute the IMU signals but also successfully perform the task of activity classification.

## 1.2 State of the Art & Its Limitations : How is it done today, and what are the limits of current practice?

### 1.2.1 Current State of the Art (SOTA)
* **RNN** (Recurrent neural network)-based: RNN-based architectures were first established in [1], using a GRU-based network for the clinical time-series classification with missing data. In [2], the same research group later designed an RNN-based method targeting imputation and classification tasks. This, later on, evolved into the state-of-the-art work (for HAR data), that’s the use of Bi-directional RNNs in BRITS [3] which has been published at NeurIPS’18. BRITS proposes a combination of a recurrent dynamic network and regression models that simultaneously work to impute the missing values. This makes BRITS robust to multiple correlated missing values and can be applied to different settings(datasets) as a data-driven imputation procedure. The limitation of this work is that BRITS has eliminated just 10% of the time-series data randomly from the ground truth. Since BRITS’ network depends on the value of the missing variables (using them as variables for the RNN graph), an increase in the missingness will possibly lead to a quick rise in the error rate and consecutively the classification accuracy. Also, attention-based networks have performed way better than BRITS on other datasets.
* **GAN** (Generative Adversarial Network)-based: In [4], a generative adversarial network-based architecture has been introduced for the imputation task. The generator itself, however, consists of a GRU unit meant for imputation. Imputation is being treated as a data generation task, and once the complete time series has been obtained, it is used in downstream prediction applications, amongst others. This has experimented with datasets in the Medical and environmental domains. E2GAN [5] is a better version of this network which solves the imputation task in a single stage while using an auto-encoder-based GRU network in the generator block. There’s also a non-autoregressive model called * * NAOMI [6] for Spatio-temporal sequence imputation, which consists of a bidirectional encoder and a multiresolution decoder. These networks were tested on PhysioNet (medical) and Air-quality related datasets.
* **VAE** (Variational Autoencoder Network)-based: [7] introduces GP-VAE, a variational auto-encoder (VAE) architecture for the imputation of time series along with a Gaussian process (GP) prior defined in the latent space. This GP-prior helps with the embedding of data into a smooth explainable representation. Other similar VAE-based works focus on other statistical aspects of the time series and infuse that information with the GP-Prior.
* **Self-attention-based**: SAITS [8] - Self-attention-based time-series is currently the best research work for time-series-imputation that outperforms the reconstruction performance of all the previous RNN/GAN/VAE-based architectures. It has been implemented on the datasets of PhysioNet, Air-quality, and electricity load monitoring systems. As mentioned earlier, learns missing values from a weighted combination of two diagonally-masked self-attention blocks which explicitly capture both the temporal dependencies and feature correlations between time steps which in turn improves imputation accuracy and training speed.

### 1.2.2 Limitations

* All the previous RNN-based networks have memory constraints when dealing with long-term dependency in time series when the number of time steps missing in the data sample is relatively significant.
* There’s also susceptibility for compounding error for most of these models predicting based on the recently amputated time series.
* The GAN, as well as VAE-based research, involve a complex training cycle caused due to issues such as non-convergence and mode-collapse due to their respective loss formulations.
* Only baseline approaches like mean/median/KNN-based methods have been tested on UCI HAR and PAMAPS2 datasets for imputation+classification related tasks.
* For IMU data, MCAR, MAR, and MNAR - all the types of missingness are very common, but no existing HAR research focuses on experimenting with all of them.
* SOTA imputation models like SAITS and BRITS have only been used on time-series datasets like PhysioNet, Air-Quality, and Electricity. The only dataset remotely close to HAR is the UCI Localization dataset, consisting of spatial x,y, and z coordinates of IMU sensors, which was used for BRITS. Moreover, from our findings on HAR datasets, the existing research only focuses on baseline imputation approaches.
* Additionally, BRITS has many limitations like lengthy training cycles, lack of support for training on data with missingness in the raw signal, and compounding errors due to being auto-regressive.

## 1.3 Novelty & Rationale : What is new in your approach and why do you think it will be successful?

The novelty of our work are as follows:
* Inspired by SAITS, we propose a self-attention-based network that delivers its training objectives from masked language modeling.
* It is the first in its kind to effectively perform missing data imputation as well as a multi-class classification for human activity recognition. Further, it has been tested on two popular HAR datasets - UCI HAR and PAMAPS2.
* From our initial missingness analysis using smartphone IMU data, we observe that these devices not only have MCAR but also have MAR and MNAR missingness types. Therefore, our work is the first to perform a comparative study using SOTA models on multiple types of missingness (MCAR, MAR, and MNAR) with varying missingness rates for HAR datasets.
* Our approach not only outperforms other SOTA imputation models over various metrics but also has a faster training and inference time cycle. This makes it much more feasible for mobile applications where IMU data is extensively used.
* Our approach is also capable of handling potential use cases where the raw data itself contains missing values. We have showcased this through experimentations on the PAMAPS2 dataset, which includes a lot of missing values.


## 1.4 Potential Impact : If the project is successful, what difference will it make, both technically and broadly?

HAR classification from IMU signals is applicable in various domains like sports, eldercare, and healthcare. However, these HAR models, when deployed on edge devices, won’t necessarily perform validation on “clean data.” Missing data is an inherent problem in many applications involving sensors, and therefore mitigating it can have tremendous implications.

Following are the potential impact that our work can make:
* **Robust HAR on-edge**: Our work can improve the performance of edge devices in scenarios where power constraints, channel noise, and other interferences cause data missingness. Also, because it is lightweight and has a faster inference time, it becomes a natural choice for the task of on-edge HAR.
* **IMUs beyond HAR**: IMU signals from smartphones and smartwatches are also used for various other applications like gait classification, step counting, and gesture control; therefore, the reconstructed signals from our imputation method can be utilized to improve the performance of the abovementioned tasks.
* **Generalized time-series missingness**: We make very few assumptions about the signals and their missingness (experiment over multiple types of missingness, varying missingness rates, and multiple HAR datasets); therefore, it is also possible to extend these robust models to other time-series-based problems like stock market prediction and EEG/ ECG classification, and COVID-spread forecast.


## 1.5 Challenges : What are the challenges and risks?

## 1.6 Requirements for Success : What skills and resources are necessary to perform the project?

## 1.7 Metrics of Success : What are metrics by which you would check for success?

We will be using two sets of evaluation metrics to determine the success of our research work. 

Metrics for imputation performance: 
* **MAE** (Mean Absolute Error)
* **RMSE** (Root Mean Square Error)
* **MRE** (Mean Relative Error) 

Metrics for classification performance: 
* **Accuracy** (percentage of correct predictions)
* **F1-Score** (to take into account class distribution)

We will be evaluating these parameters for three missingness types, namely: MCAR, MAR, and MNAR, with varying missingness rates from 10 % to 90 % for all five imputation models. 


# 2. Related Work

## 2.1 Papers
A brief summary of the research work mentioned in earlier sections can be found here. There are numerous publications at top conferences which focus on data imputation using architectures based on RNNs/GANs/VAEs/Self-attention.

* **SAITS**: A novel method based on the self-attention mechanism for missing value imputation in multivariate time series.
* **BRITS**: Bidirectional RNN-based method directly learns the missing values in a bidirectional recurrent dynamical system, without any specific assumption.
* **GAN**: Learn the overall distribution of a multivariate time series dataset with GAN, which is further used to generate the missing values for each sample.
* **M-RNN**: A Multi-directional Recurrent Neural Network (M-RNN). The main difference of An M-RNN between a bi-directional RNN is that it sequentially operates across streams.
* **NAOMI**: A non-autoregressive approach and proposes a novel deep generative model: Non-AutOregressive Multiresolution Imputation (NAOMI) to impute long-range sequences given arbitrary missing patterns.
* **E2GAN**: An end-to-end generative model E²GAN to impute missing values in multivariate time series. With the help of the discriminative loss and the squared error loss, E²GAN can impute the incomplete time series by the nearest generated complete time series at one stage.


## 2.2 Dataset
* **UCI HAR Dataset**:
  * 6 activities (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING)
  * 128 readings/ window (~10k time series)
  * 3-axis accelerometer and 3-axis gyroscope
* **PAMAP 2 Dataset**:
  * 24 activities
  * 52 features
    * Heart Beat
    * IMU hand (2 x 3-axis accelo, 3-axis gyro, 3-axis magneto, orientation)
    * IMU chest
    * IMU ankle
  * We found window size of 40, as best for imputation and classification performance

## 2.3 Software
* Python >= 3.9
* Packages: PyPots, TSDB, PyTorch, Matplotlib, Pandas, Scipy, Numpy, Scikit Learn

# 3. Technical Approach

## 3.1 Data Missingness

### 3.1.1 Types of data missingness:
* Missing completely at random (MCAR), missing values are independent of any other values
* Missing at random (MAR), missing values depend only on observed values
  * E.g., missingness rate for walking is higher than that for standing?
  * E.g., missingness rate for sensor X is higher than sensor Y?
* Missing not at random (MNAR), missing values depend on both observed and unobserved values
  * E.g., if you run very fast (more acceleration), missingness is likely to be higher than normal run

### 3.1.2 Synthetically introducing MCAR, MAR, and MNAR

* **MCAR**: Generates missingness completely at random based on a given missingness rate ‘p’
* **MAR** (with logistic masking model): First, a subset of variables with no missing values is randomly selected. The remaining variables have missing values according to a logistic model with random weights, re-scaled so as to attain the desired proportion of missing values on those variables.
* **MNAR** (with logistic masking model): It is implemented by selecting missingness probabilities with a logistic model, taking all variables as inputs. Hence, values that are inputs can also be missing.

## 3.2 Imputation Models

### 3.2.1 Baseline Models
* **Zero imputation** - Filling the missing data directly with 0.
* **Mean imputation** - Filling the missing data with mean of the values in the window.
* **Median imputation** - Filling the missing data with median of the values in the window. 

### 3.2.2 BRITS

### 3.2.3 SAITS

## 3.3 Classification Models

# 4. Evaluation and Results

## Results UCI HAR Dataset

### Imputation performance for MCAR, MAR, and MNAR missingness type

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky" rowspan="2"></th>
    <th class="tg-fymr" colspan="3">MCAR</th>
    <th class="tg-fymr" colspan="3">MAR</th>
    <th class="tg-fymr" colspan="3">MNAR</th>
  </tr>
  <tr>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MRE</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MRE</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MRE</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">Zero Imputation</td>
    <td class="tg-0pky">0.11486</td>
    <td class="tg-0pky">0.23322</td>
    <td class="tg-0pky">1.36e+14</td>
    <td class="tg-0pky">0.163882</td>
    <td class="tg-0pky">0.309273</td>
    <td class="tg-0pky">9.71e+13</td>
    <td class="tg-0pky">0.137518</td>
    <td class="tg-0pky">0.269574</td>
    <td class="tg-0pky">1.63e+13</td>
  </tr>
  <tr>
    <td class="tg-fymr">Mean Imputation</td>
    <td class="tg-0pky">0.115776</td>
    <td class="tg-0pky">0.232347</td>
    <td class="tg-0pky">7.88e+00</td>
    <td class="tg-0pky">0.165468</td>
    <td class="tg-0pky">0.309157</td>
    <td class="tg-0pky">5.46e+00</td>
    <td class="tg-0pky">0.138558</td>
    <td class="tg-0pky">0.268663</td>
    <td class="tg-0pky">6.24e+00</td>
  </tr>
  <tr>
    <td class="tg-fymr">Median Imputation</td>
    <td class="tg-0pky">0.113634</td>
    <td class="tg-0pky">0.234785</td>
    <td class="tg-0pky">5.55e+00</td>
    <td class="tg-0pky">0.162335</td>
    <td class="tg-0pky">0.310746</td>
    <td class="tg-0pky">4.6e+00</td>
    <td class="tg-0pky">0.136083</td>
    <td class="tg-0pky">0.271151</td>
    <td class="tg-0pky">4.81e+00</td>
  </tr>
  <tr>
    <td class="tg-fymr">BRITS Imputation</td>
    <td class="tg-0pky">0.071421</td>
    <td class="tg-0pky">0.189044</td>
    <td class="tg-0pky">1.01e+00</td>
    <td class="tg-0pky">0.161633</td>
    <td class="tg-0pky">0.309093</td>
    <td class="tg-0pky">2.17e+00</td>
    <td class="tg-0pky">0.127701</td>
    <td class="tg-0pky">0.243318</td>
    <td class="tg-0pky">2.89e+00</td>
  </tr>
  <tr>
    <td class="tg-fymr">SAITS Imputation</td>
    <td class="tg-0pky">0.025206</td>
    <td class="tg-0pky">0.068027</td>
    <td class="tg-0pky">2.19e-01</td>
    <td class="tg-0pky">0.059130</td>
    <td class="tg-0pky">0.289041</td>
    <td class="tg-0pky">1.00e+00</td>
    <td class="tg-0pky">0.043189</td>
    <td class="tg-0pky">0.134634</td>
    <td class="tg-0pky">1.03e+00</td>
  </tr>
</tbody>
</table>


### Classification performance for MCAR, MAR, and MNAR missingness type

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky" rowspan="2"></th>
    <th class="tg-fymr" colspan="2">MCAR</th>
    <th class="tg-fymr" colspan="2">MAR</th>
    <th class="tg-fymr" colspan="2">MNAR</th>
  </tr>
  <tr>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">Zero Imputation</td>
    <td class="tg-0pky">25.22%</td>
    <td class="tg-0pky">0.22</td>
    <td class="tg-0pky">27.84%</td>
    <td class="tg-0pky">0.23</td>
    <td class="tg-0pky">18.92%</td>
    <td class="tg-0pky">0.17</td>
  </tr>
  <tr>
    <td class="tg-fymr">Mean Imputation</td>
    <td class="tg-0pky">44.23%</td>
    <td class="tg-0pky">0.46</td>
    <td class="tg-0pky">38.66%</td>
    <td class="tg-0pky">0.40</td>
    <td class="tg-0pky">42.25%</td>
    <td class="tg-0pky">0.45</td>
  </tr>
  <tr>
    <td class="tg-fymr">Median Imputation</td>
    <td class="tg-0pky">45.64%</td>
    <td class="tg-0pky">0.48</td>
    <td class="tg-0pky">33.27%</td>
    <td class="tg-0pky">0.35</td>
    <td class="tg-0pky">40.42%</td>
    <td class="tg-0pky">0.42</td>
  </tr>
  <tr>
    <td class="tg-fymr">BRITS Imputation</td>
    <td class="tg-0pky">91.17%</td>
    <td class="tg-0pky">0.94</td>
    <td class="tg-0pky">86.62%</td>
    <td class="tg-0pky">0.88</td>
    <td class="tg-0pky">89.85%</td>
    <td class="tg-0pky">0.90</td>
  </tr>
  <tr>
    <td class="tg-fymr">SAITS Imputation</td>
    <td class="tg-0pky">92.52%</td>
    <td class="tg-0pky">0.95</td>
    <td class="tg-0pky">88.54%</td>
    <td class="tg-0pky">0.91</td>
    <td class="tg-0pky">90.92%</td>
    <td class="tg-0pky">0.93</td>
  </tr>
</tbody>
</table>


### Imputation performance over varying missingness rate

<table class="tg">
<thead>
  <tr>
    <th class="tg-fymr" rowspan="2"></th>
    <th class="tg-fymr" colspan="3">Zero Imputation</th>
    <th class="tg-fymr" colspan="3">Mean Imputation</th>
    <th class="tg-1wig" colspan="3">Median Imputation</th>
    <th class="tg-1wig" colspan="3">BRITS Imputation</th>
    <th class="tg-1wig" colspan="3">SAITS Imputation</th>
  </tr>
  <tr>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MRE</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MRE</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MRE</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MRE</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MRE</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">10 %</td>
    <td class="tg-0pky">0.114886</td>
    <td class="tg-0pky">0.233225</td>
    <td class="tg-0pky">1.36e+14</td>
    <td class="tg-0pky">0.115776</td>
    <td class="tg-0pky">0.232347</td>
    <td class="tg-0pky">7.88e+00</td>
    <td class="tg-0lax">0.113634</td>
    <td class="tg-0lax">0.234785</td>
    <td class="tg-0lax">5.55e+00</td>
    <td class="tg-0lax">0.071421</td>
    <td class="tg-0lax">0.189044</td>
    <td class="tg-0lax">1.01e+00</td>
    <td class="tg-0lax">0.025206</td>
    <td class="tg-0lax">0.078027</td>
    <td class="tg-0lax">2.19e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">20 %</td>
    <td class="tg-0pky">0.114861</td>
    <td class="tg-0pky">0.233171</td>
    <td class="tg-0pky">2.72e+14</td>
    <td class="tg-0pky">0.115862</td>
    <td class="tg-0pky">0.232386</td>
    <td class="tg-0pky">7.52e+00</td>
    <td class="tg-0lax">0.113686</td>
    <td class="tg-0lax">0.234810</td>
    <td class="tg-0lax">5.45e+00</td>
    <td class="tg-0lax">0.103246</td>
    <td class="tg-0lax">0.184325</td>
    <td class="tg-0lax">9.57e-01</td>
    <td class="tg-0lax">0.039735</td>
    <td class="tg-0lax">0.099199</td>
    <td class="tg-0lax">3.46e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">30 %</td>
    <td class="tg-0pky">0.114897</td>
    <td class="tg-0pky">0.233380</td>
    <td class="tg-0pky">4.09e+14</td>
    <td class="tg-0lax">0.116015</td>
    <td class="tg-0lax">0.232767</td>
    <td class="tg-0lax">7.11e+00</td>
    <td class="tg-0pky">0.113850</td>
    <td class="tg-0pky">0.235246</td>
    <td class="tg-0pky">5.35e+00</td>
    <td class="tg-0lax">0.095643</td>
    <td class="tg-0lax">0.186893</td>
    <td class="tg-0lax">9.97e-01</td>
    <td class="tg-0lax">0.043035</td>
    <td class="tg-0lax">0.107692</td>
    <td class="tg-0lax">3.74e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">40 %</td>
    <td class="tg-0pky">0.114970</td>
    <td class="tg-0pky">0.233541</td>
    <td class="tg-0pky">5.45e+14</td>
    <td class="tg-0pky">0.116230</td>
    <td class="tg-0pky">0.233240</td>
    <td class="tg-0pky">6.74e+00</td>
    <td class="tg-0lax">0.114093</td>
    <td class="tg-0lax">0.235702</td>
    <td class="tg-0lax">5.21e+00</td>
    <td class="tg-0lax">0.113654</td>
    <td class="tg-0lax">0.189329</td>
    <td class="tg-0lax">9.99e-01</td>
    <td class="tg-0lax">0.049995</td>
    <td class="tg-0lax">0.121676</td>
    <td class="tg-0lax">4.34e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">50 %</td>
    <td class="tg-0pky">0.114846</td>
    <td class="tg-0pky">0.233221</td>
    <td class="tg-0pky">6.81e+14</td>
    <td class="tg-0pky">0.116242</td>
    <td class="tg-0pky">0.233056</td>
    <td class="tg-0pky">6.39e+00</td>
    <td class="tg-0lax">0.1141123</td>
    <td class="tg-0lax">0.235713</td>
    <td class="tg-0lax">4.9e+00</td>
    <td class="tg-0lax">0.113654</td>
    <td class="tg-0lax">0.19139</td>
    <td class="tg-0lax">1.10e00</td>
    <td class="tg-0lax">0.058269</td>
    <td class="tg-0lax">0.136983</td>
    <td class="tg-0lax">5.0e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">60 %</td>
    <td class="tg-0pky">0.114908</td>
    <td class="tg-0pky">0.233391</td>
    <td class="tg-0pky">8.18e+14</td>
    <td class="tg-0pky">0.116668</td>
    <td class="tg-0pky">0.233770</td>
    <td class="tg-0pky">5.83e+00</td>
    <td class="tg-0lax">0.114482</td>
    <td class="tg-0lax">0.236468</td>
    <td class="tg-0lax">4.71e+00</td>
    <td class="tg-0lax">0.115624</td>
    <td class="tg-0lax">0.198277</td>
    <td class="tg-0lax">1.13e+01</td>
    <td class="tg-0lax">0.061764</td>
    <td class="tg-0lax">0.142273</td>
    <td class="tg-0lax">5.37e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">70 %</td>
    <td class="tg-0pky">0.114844</td>
    <td class="tg-0pky">0.233293</td>
    <td class="tg-0pky">9.53e+14</td>
    <td class="tg-0pky">0.117091</td>
    <td class="tg-0pky">0.234323</td>
    <td class="tg-0pky">5.31e+00</td>
    <td class="tg-0lax">0.114992</td>
    <td class="tg-0lax">0.237402</td>
    <td class="tg-0lax">4.42e+00</td>
    <td class="tg-0lax">0.115988</td>
    <td class="tg-0lax">0.199835</td>
    <td class="tg-0lax">1.23e+00</td>
    <td class="tg-0lax">0.075420</td>
    <td class="tg-0lax">0.167893</td>
    <td class="tg-0lax">6.56e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">80 %</td>
    <td class="tg-0pky">0.114819</td>
    <td class="tg-0pky">0.233297</td>
    <td class="tg-0pky">1.09e+15</td>
    <td class="tg-0pky">0.117917</td>
    <td class="tg-0pky">0.235792</td>
    <td class="tg-0pky">4.44e+0</td>
    <td class="tg-0lax">0.115974</td>
    <td class="tg-0lax">0.239364</td>
    <td class="tg-0lax">3.87e+00</td>
    <td class="tg-0lax">0.118903</td>
    <td class="tg-0lax">0.21341</td>
    <td class="tg-0lax">1.83e+00</td>
    <td class="tg-0lax">0.086623</td>
    <td class="tg-0lax">0.186676</td>
    <td class="tg-0lax">7.54e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">90 %</td>
    <td class="tg-0pky">0.114822</td>
    <td class="tg-0pky">0.233171</td>
    <td class="tg-0pky">1.22e+15</td>
    <td class="tg-0pky">0.120713</td>
    <td class="tg-0pky">0.240714</td>
    <td class="tg-0pky">3.32e+00</td>
    <td class="tg-0lax">0.119336</td>
    <td class="tg-0lax">0.245459</td>
    <td class="tg-0lax">2.97e+00</td>
    <td class="tg-0lax">0.123216</td>
    <td class="tg-0lax">0.23548</td>
    <td class="tg-0lax">2.13e+00</td>
    <td class="tg-0lax">0.100667</td>
    <td class="tg-0lax">0.209792</td>
    <td class="tg-0lax">8.76e-01</td>
  </tr>
</tbody>
</table>


### Classification performance over varying missingness rate

<table class="tg">
<thead>
  <tr>
    <th class="tg-fymr" rowspan="2"></th>
    <th class="tg-1wig" colspan="2">BRITS Imputation</th>
    <th class="tg-1wig" colspan="2">SAITS Imputation</th>
  </tr>
  <tr>
    <th class="tg-1wig">Acc.</th>
    <th class="tg-1wig">F1-Score</th>
    <th class="tg-1wig">Acc.</th>
    <th class="tg-1wig">F1-Score</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">10%</td>
    <td class="tg-0lax">91.17%</td>
    <td class="tg-0lax">0.94</td>
    <td class="tg-0lax">92.52%</td>
    <td class="tg-0lax">0.95</td>
  </tr>
  <tr>
    <td class="tg-fymr">20%</td>
    <td class="tg-0lax">90.73%</td>
    <td class="tg-0lax">0.92</td>
    <td class="tg-0lax">91.65%</td>
    <td class="tg-0lax">0.94</td>
  </tr>
  <tr>
    <td class="tg-fymr">30%</td>
    <td class="tg-0lax">82.62%</td>
    <td class="tg-0lax">0.81</td>
    <td class="tg-0lax">86.67%</td>
    <td class="tg-0lax">0.87</td>
  </tr>
  <tr>
    <td class="tg-fymr">40%</td>
    <td class="tg-0lax">76.86%</td>
    <td class="tg-0lax">0.74</td>
    <td class="tg-0lax">81.37%</td>
    <td class="tg-0lax">0.79</td>
  </tr>
  <tr>
    <td class="tg-fymr">50%</td>
    <td class="tg-0lax">68.43%</td>
    <td class="tg-0lax">0.66</td>
    <td class="tg-0lax">74.27%</td>
    <td class="tg-0lax">0.75</td>
  </tr>
  <tr>
    <td class="tg-fymr">60%</td>
    <td class="tg-0lax">59.14%</td>
    <td class="tg-0lax">0.56</td>
    <td class="tg-0lax">67.23%</td>
    <td class="tg-0lax">0.65</td>
  </tr>
  <tr>
    <td class="tg-fymr">70%</td>
    <td class="tg-0lax">48.22%</td>
    <td class="tg-0lax">0.46</td>
    <td class="tg-0lax">56.21%</td>
    <td class="tg-0lax">0.55</td>
  </tr>
  <tr>
    <td class="tg-fymr">80%</td>
    <td class="tg-0lax">43.86%</td>
    <td class="tg-0lax">0.39</td>
    <td class="tg-0lax">50.49%</td>
    <td class="tg-0lax">0.48</td>
  </tr>
  <tr>
    <td class="tg-fymr">90%</td>
    <td class="tg-0lax">39.45%</td>
    <td class="tg-0lax">0.37</td>
    <td class="tg-0lax">45.68%</td>
    <td class="tg-0lax">0.43</td>
  </tr>
</tbody>
</table>

## Results PAMAPS2 Dataset

### Imputation performance for MCAR, MAR, and MNAR missingness type

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky" rowspan="2"></th>
    <th class="tg-fymr" colspan="3">MCAR</th>
    <th class="tg-fymr" colspan="3">MAR</th>
    <th class="tg-fymr" colspan="3">MNAR</th>
  </tr>
  <tr>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MRE</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MRE</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MRE</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">Zero Imputation</td>
    <td class="tg-0pky">43.001326</td>
    <td class="tg-0pky">296.209078</td>
    <td class="tg-0pky">1.27e+18</td>
    <td class="tg-0pky">44.795440</td>
    <td class="tg-0pky">302.214721</td>
    <td class="tg-0pky">1.32e+18</td>
    <td class="tg-0pky">43.000029</td>
    <td class="tg-0pky">296.078032</td>
    <td class="tg-0pky">1.26e+18</td>
  </tr>
  <tr>
    <td class="tg-fymr">Mean Imputation</td>
    <td class="tg-0pky">1827.534261</td>
    <td class="tg-0pky">2135.402027</td>
    <td class="tg-0pky">1.00e+00</td>
    <td class="tg-0pky">1843.997157</td>
    <td class="tg-0pky">2148.611512</td>
    <td class="tg-0pky">1.00e+00</td>
    <td class="tg-0pky">1824.700344</td>
    <td class="tg-0pky">2132.157724</td>
    <td class="tg-0pky">1.00e+00</td>
  </tr>
  <tr>
    <td class="tg-fymr">Median Imputation</td>
    <td class="tg-0pky">1827.516164</td>
    <td class="tg-0pky">2135.420835</td>
    <td class="tg-0pky">1.00e+00</td>
    <td class="tg-0pky">1843.981177</td>
    <td class="tg-0pky">2148.633080</td>
    <td class="tg-0pky">1.00e+00</td>
    <td class="tg-0pky">1824.687548</td>
    <td class="tg-0pky">2132.176473</td>
    <td class="tg-0pky">1.00e+00</td>
  </tr>
  <tr>
    <td class="tg-fymr">BRITS Imputation</td>
    <td class="tg-0pky">30.418686</td>
    <td class="tg-0pky">147.324833</td>
    <td class="tg-0pky">4.02e-01</td>
    <td class="tg-0pky">31.762073</td>
    <td class="tg-0pky">151.236273</td>
    <td class="tg-0pky">3.68e-01</td>
    <td class="tg-0pky">36.282232</td>
    <td class="tg-0pky">150.060937</td>
    <td class="tg-0pky">4.00e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">SAITS Imputation</td>
    <td class="tg-0pky">18.222896</td>
    <td class="tg-0pky">61.980596</td>
    <td class="tg-0pky">4.2e-01</td>
    <td class="tg-0pky">17.388033</td>
    <td class="tg-0pky">53.826534</td>
    <td class="tg-0pky">2.33e-01</td>
    <td class="tg-0pky">26.891733</td>
    <td class="tg-0pky">70.600211</td>
    <td class="tg-0pky">3.65e-01</td>
  </tr>
</tbody>
</table>


# 5. Discussion and Conclusions
## 5.1 Conclusion
From our evaluations, we conclude the following:
* SAITS **outperforms** BRITS by ~ 31% in MAE and achieves 2 ∼ 3 times faster training speed. Furthermore, SAITS outperforms baseline imputation approaches by ~ 400% in MAE.
* SAITS is **robust** to different types of missingness - namely tested on MCAR, MAR, and MNAR with varying missingness rate  
* SAITS is **multiutility** - it not only outperforms other methods on imputation metrics but also does well on downstream task of HAR classification. 
* SAITS **generalizes** well as we have tested it on two popular - UCI HAR and PAMAPS2 dataset.

## 5.2 Future Work
* Our best classifier (CNN-based) on SAIT imputed data achieved ~92.5 % for UCI HAR, and ~91 % for PAMAPS2 (with 10% MCAR); however their existing SOTA models have achieved ~98 %  test accuracy. Therefore we see a new direction of future research in experimenting with SOTA/building better classifiers.
* IMU signals from smartphones and smartwatches are also used for various other applications like gait classification, step counting, and gesture control; therefore, the reconstructed signals from our imputation method can be utilized to improve the performance of the above mentioned tasks.



# 6. References
[1] Z. C. Lipton et al., “Directly modeling missing data in sequences with RNNs: Improved classification of clinical time series,” Mach. Learning Healthcare conf., pp. 253–270, 2016. (https://proceedings.mlr.press/v56/Lipton16.html)

[2] Zhengping Che, S. Purushotham, Kyunghyun Cho, D. Sontag, and Y. Liu. Recurrent neural networks for multivariate time series with missing values. Scientific Reports, 8, 2018. (https://www.nature.com/articles/s41598-018-24271-9)

[3] W. Cao, D. Wang, J. Li, H. Zhou, L. Li, και Y. Li, ‘BRITS: Bidirectional Recurrent Imputation for Time Series’, στο Advances in Neural Information Processing Systems, 2018, τ. 31. (https://papers.nips.cc/paper/2018/hash/734e6bfcd358e25ac1db0a4241b95651-Abstract.html)

[4] Yonghong Luo, Xiangrui Cai, Ying ZHANG, Jun Xu, and Yuan xiaojie. Multivariate time series imputation with generative adversarial networks. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018. (https://papers.nips.cc/paper/2018/hash/96b9bff013acedfb1d140579e2fbeb63-Abstract.html)

[5] Yonghong Luo, Ying Zhang, Xiangrui Cai, and Xiaojie Yuan. E2GAN: End-to-end generative adversarial network for multivariate time series imputation. In Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI-19, pages 3094–3100. International Joint Conferences on Artificial Intelligence Organization, 7 2019. (https://www.ijcai.org/proceedings/2019/429)

[6] Yukai Liu, Rose Yu, Stephan Zheng, Eric Zhan, and Yisong Yue. NAOMI: Non-autoregressive multiresolution sequence imputation. In Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019 (https://proceedings.neurips.cc/paper/2019/file/50c1f44e426560f3f2cdcb3e19e39903-Paper.pdf)

[7] Vincent Fortuin, Dmitry Baranchuk, Gunnar Raetsch, and Stephan Mandt. GP-VAE: Deep probabilistic time series imputation. In Silvia Chiappa and Roberto Calandra, editors, Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics, volume 108 of Proceedings of Machine Learning Research, pages 1651–1661. PMLR, 26–28 Aug 2020. (https://proceedings.mlr.press/v108/fortuin20a.html)

[8] W. Du, D. Côté, και Y. Liu, ‘SAITS: Self-Attention-based Imputation for Time Series’. arXiv, 2022. (https://arxiv.org/abs/2202.08516)

[9] Davide Anguita, Alessandro Ghio, Luca Oneto, Xavier Parra and Jorge L. Reyes-Ortiz. A Public Domain Dataset for Human Activity Recognition Using Smartphones. 21th European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning, ESANN 2013. Bruges, Belgium 24-26 April 2013. (https://archive.ics.uci.edu/ml/machine-learning-databases/00240/)

[10] A. Reiss and D. Stricker. Introducing a New Benchmarked Dataset for Activity Monitoring. The 16th IEEE International Symposium on Wearable Computers (ISWC), 2012. (https://www.computer.org/csdl/proceedings-article/iswc/2012/4697a108/12OmNzwZ6pa)

[11] A. Reiss and D. Stricker. Creating and Benchmarking a New Dataset for Physical Activity Monitoring. The 5th Workshop on Affect and Behaviour Related Assistance (ABRA), 2012. (http://archive.ics.uci.edu/ml/datasets/pamap2%20physical%20activity%20monitoring)
