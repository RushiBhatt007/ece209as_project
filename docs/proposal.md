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
- **IMUs beyond HAR**: IMU signals from smartphones and smartwatches are also used for various other applications like gait classification, step counting, and gesture control; therefore, the reconstructed signals from our imputation method can be utilized to improve the performance of the abovementioned tasks. 
- **Generalized time-series missingness**: We make very few assumptions about the signals and their missingness (experiment over multiple types of missingness); therefore, it is also possible to extend these robust models to other time-series-based problems like stock market prediction and EEG/ ECG classification, and COVID-spread forecast.


## 5. Challenges

Some of the challenges and risks associated with this research project are:

- Performing a thorough investigation and having a deep understanding of the various types of IMU data missingness distribution. Although it is easy to assume the missingness distribution to be random (MAR, MCAR, MNAR) like in most literature, it might not necessarily be the case in real-life applications.
- Making assumptions about the missingness distribution (e.g., fading channel) can also be a potential risk because it can make the model biased toward such missingness. 
- Most State of the Art implementations on data imputation deal with low-frequency biological data sets like medical records. A potential challenge would be to extend similar models and ideas for high-frequency data from IMUs for the task of HAR.   

## 6. Requirements for Success

- Access to HAR dataset
- Access to a local machine with good GPU/ Google Colab Pro
- Strong fundamental knowledge of machine learning, signal processing, and deep learning
- Thorough understanding of baseline imputation techniques and SOTA papers
- Strong programming skills in Python along with hands-on experience in working with Keras, Numpy, Tensorflow, and Pytorch
- Ability to rapidly replicate existing work as well as perform long and iterative experimentations with modifications


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
- Replicating SOTA implementation
- Performance metrics, comparative analysis, and visualizations 

## 9. Related Work

### 9.a. Papers

List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).

As our goal is to using technology to recognize human activites based on partial or missing data, therefore we will mainly focus on what kinds of technology do others use to recognize activities, specificly, the machine learning/deep learning model. And what kinds of method do other use to handle with missing data when we reading tons of papers. 

In this paper [1], the author developed a Multi-directional Recurrent Neural Network (M-RNN). The main difference of An M-RNN between a bi-directional RNN is that  it sequentially operates across streams.

In this paper [2] The author construct personalized policies using logged data when there are missing values in the attributes of features as a solution to missing data.

In this paper [3] the author uses intelligent data augmentation techniques to handle with missing data.. Specifically, the author use controlled jitter in window length and add artificial misalignments in data timestamps between sensors, along with masking representations of missing data. 

In this paper [4] the author design a noval deep network architecture using residual bidirectional long short-term memory (LSTM) cells. The main advantage of this model is that residual connections between stacked cells act as highways for gradients, which can pass underlying information directly to the upper layer, effectively avoiding the gradient vanishing problem. 

In this paper [5] proposes SAITS, a novel method based on the self-attention mechanism for missing value imputation in multivariate time series.

In this paper [6] the author proposed method directly learns the missing values in a bidirectional recurrent dynamical system, without any specific assumption.

In this paper [7] the author develop novel deep learning models, namely GRU-D, as one of the early attempts.

In this paper [8] the author propose a new approach, based on a novel deep learning architecture that we call a Multi-directional Recurrent Neural Network that interpolates within data streams and imputes across data streams.

In this paper [9] the author demonstrate a simple strategy to cope with missing data in sequential inputs, addressing the task of multilabel classification of diagnoses given clinical time series.

In this paper [10] the author propose to learn the overall distribution of a multivariate time series dataset with GAN, which is further used to generate the missing values for each sample. 
(https://papers.nips.cc/paper/2018/hash/96b9bff013acedfb1d140579e2fbeb63-Abstract.html)

In this paper [11] the author proposes an end-to-end generative model E²GAN to impute missing values in multivariate time series. With the help of the discriminative loss and the squared error loss, E²GAN can impute the incomplete time series by the nearest generated complete time series at one stage.
(https://www.ijcai.org/proceedings/2019/429)

In this paper [12] the author take a non-autoregressive approach and propose a novel deep generative model: Non-AutOregressive Multiresolution Imputation (NAOMI) to impute long-range sequences given arbitrary missing patterns.
(https://proceedings.neurips.cc/paper/2019/file/50c1f44e426560f3f2cdcb3e19e39903-Paper.pdf)

In this paper [13]] the author propose a new deep sequential latent variable model for dimensionality reduction and data imputation.
(https://proceedings.mlr.press/v108/fortuin20a.html)


### 9.b. Datasets

List datasets that you have identified and plan to use. Provide references (with full citation in the References section below).

UCI UCI HAR Dataset
(https://archive.ics.uci.edu/ml/machine-learning-databases/00240/)

[1] Davide Anguita, Alessandro Ghio, Luca Oneto, Xavier Parra and Jorge L. Reyes-Ortiz. A Public Domain Dataset for Human Activity Recognition Using Smartphones. 21th European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning, ESANN 2013. Bruges, Belgium 24-26 April 2013. 

### 9.c. Software

List softwate that you have identified and plan to use. Provide references (with full citation in the References section below).
GitHub [13] is the codebase for BRITS implementation of paper [6]
GitHub [14] is the codebase for Robust-Deep-Learning-Pipeline
implementation of paper [3]
GitHub [15] is the codebase for LSTM-Human-Activity-Recognitionimplementation of paper [4]
	

## 10. References

List references correspondign to citations in your text above. For papers please include full citation and URL. For datasets and software include name and URL.

[1] J. Yoon, W. R. Zame, και M. van der Schaar, ‘Deep Sensing: Active Sensing using Multi-directional Recurrent Neural Networks, International Conference on Learning Representations, 2018. (https://openreview.net/pdf?id=r1SnX5xCb)

[2].M. Abroshan, K. H. Yip, C. Tekin, και M. van der Schaar, ‘Conservative Policy Construction Using Variational Autoencoders for Logged Data with Missing Values’, CoRR, τ. abs/2109.03747, 2021.
Values(https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9675815)

[3]. Saha, S. S., Sandha, S. S., & Srivastava, M. (2020). Deep Convolutional Bidirectional LSTM for Complex Activity Recognition with Missing Data. Smart Innovation, Systems and Technologies, 39–53. doi:10.1007/978-981-15-8269-1_4
(https://www.researchgate.net/publication/341055525_Deep_Convolutional_Bidirectional_LSTM_for_Complex_Activity_Recognition_with_Missing_Data)

[4]. T. Hossain, M. A. R. Ahad, και S. Inoue, ‘A Method for Sensor-Based Activity Recognition in Missing Data Scenario’, Sensors, τ. 20, τχ. 14, 2020.
(https://arxiv.org/abs/1708.08989)

[5]. W. Du, D. Côté, και Y. Liu, ‘SAITS: Self-Attention-based Imputation for Time Series’. arXiv, 2022.
(https://arxiv.org/abs/2202.08516)

[6]. W. Cao, D. Wang, J. Li, H. Zhou, L. Li, και Y. Li, ‘BRITS: Bidirectional Recurrent Imputation for Time Series’, στο Advances in Neural Information Processing Systems, 2018, τ. 31.
(https://papers.nips.cc/paper/2018/hash/734e6bfcd358e25ac1db0a4241b95651-Abstract.html)

[7]. Zhengping Che, S. Purushotham, Kyunghyun Cho, D. Sontag, and Y. Liu. Recurrent neural networks for multivariate time series with missing values. Scientific Reports, 8, 2018.
(https://www.nature.com/articles/s41598-018-24271-9)

[8]  Jinsung Yoon, William R. Zame, and Mihaela van der Schaar. Estimating missing data in temporal data streams using multi-directional recurrent neural networks. IEEE Transactions on Biomedical Engineering, 66(5):1477-1490, 2019.
(https://ieeexplore.ieee.org/document/8485748)

[9] Z. C. Lipton et al., “Directly modeling missing data in sequences with RNNs: Improved classification of clinical time series,” Mach. Learning Healthcare conf., pp. 253–270, 2016.
(https://proceedings.mlr.press/v56/Lipton16.html)

[10] Yonghong Luo, Xiangrui Cai, Ying ZHANG, Jun Xu, and Yuan xiaojie. Multivariate time series imputation with generative adversarial networks. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018.

[11]  Yonghong Luo, Ying Zhang, Xiangrui Cai, and Xiaojie Yuan. E2GAN: End-to-end generative adversarial network for multivariate time series imputation. In Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI-19, pages 3094–3100. International Joint Conferences on Artificial Intelligence Organization, 7 2019.

[12] Yukai Liu, Rose Yu, Stephan Zheng, Eric Zhan, and Yisong Yue. NAOMI: Non-autoregressive multiresolution sequence imputation. In Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019

[13] Vincent Fortuin, Dmitry Baranchuk, Gunnar Raetsch, and Stephan Mandt. GP-VAE: Deep probabilistic time series imputation. In Silvia Chiappa and Roberto Calandra, editors, Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics, volume 108 of Proceedings of Machine Learning Research, pages 1651–1661. PMLR, 26–28 Aug 2020.

[14] https://github.com/caow13/BRITS
[15] https://github.com/nesl/Robust-Deep-Learning-Pipeline/blob/main/README.md
[16]https://github.com/guillaume-chevalier/LSTM-Human-Activity-Recognition/blob/master/README.md

