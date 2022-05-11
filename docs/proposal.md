# Project Proposal

## 1. Motivation & Objective

Human Activity Recognition (HAR) is the process of automatically inferring a user’s activity (e.g., walking, sitting, standing) based on sensor data (e.g., accelerometers, gyroscope) typically from devices like smartphones and smartwatches. However traditional machine learning method’s performance decreases significantly in real-life applications due to the problem of data missingness. Data Missingness in sensors typically happens due to power limitation, hardware failure, transmission packet loss, and many more. Our goal through this project is two folds, first is to investigate the data missingness distribution for Inertial Measurement Units (IMU). Secondly, it is to build robust models that not only impute the IMU signals but also successfully perform the task of activity classification.

## 2. State of the Art & Its Limitations


Human Activity Recognition (HAR) involving missing data hasn’t been thoroughly explored. There’s quality research work going particularly in the domain of imputation of time-series signals, however, it has been focused on the medical and finance domain. The most advanced and recent research for time-series imputation is ‘SAITS: Self-attention based imputation for time-series. It learns missing values from a weighted combination
of two diagonally-masked self-attention blocks. This research work is based on datasets such as PhysioNet, Electricity Load Diagram, and Beijing Multi-site air quality. The best research work focusing on Human Activity Recognition is ‘BRITS: Bidirectional Recurrent Imputation for Time-series’. SAITS has been seen to outperform BRITS by a significant margin for both imputation and classification tasks on the non-HAR datasets. Let’s look at the evolution of the time-series imputation-related research work.

**RNN(Recurrent neural network)-based**: RNN-based architectures were first established in [9], where they used a GRU-based network for the clinical time-series classification with missing data. In [7], the same research group later designed an RNN-based method targeting both imputation and classification tasks. This, later on, evolved into the state-of-the-art work (for HAR data), that’s the use of Bi-directional RNNs in BRITS which has been published at NeurIPS’18. BRITS proposes a combination of a recurrent dynamic network and regression models that simultaneously work to impute the missing values. This makes BRITS robust to multiple correlated missing values and can be applied to different settings(datasets) as a data-driven imputation procedure. The limitation of this work is that BRITS has eliminated just 10% of the time-series data randomly from the ground truth. Since BRITS’ network depends on the value of the missing variables (using them as variables for the RNN graph), an increase in the missingness will possibly lead to a quick increase in the error rate and consecutively the classification accuracy. Also, attention-based networks have performed way better than BRITS on other datasets. 

**GAN(Generative Adversarial Network)-based**: In [10], a generative adversarial network-based architecture has been introduced for the imputation task. The generator itself however consists of a GRU unit meant for imputation. Imputation is being treated as a data generation task and once the complete time-series has been obtained, it is used in downstream applications of prediction amongst others. This has been experimented with datasets in the Medical and enovironmental domain. E2GAN [11] is a better version of this network which solves the imputation task in a single stage while making use of an auto-encoder based GRU network in the generator block. There’s also a non-autoregressive model called NAOMI [12] for spatio-temporal sequence imputation which consists of a bidirectional encoder and a multiresolution decoder. These networks were tested on PhysioNet (medical) and Air-quality related datasets. 

**VAE(Variational Autoencoder Network)-based**: [13] introduces GP-VAE, a variational auto-encoder (VAE) architecture for the imputation of time series along with a Gaussian process (GP) prior defined in the latent space. This GP-prior is helps with the embedding of data into a smooth explainable representation. There are other similar VAE based works which focus on other statistical aspects of the time-series and infuse that information with the GP-Prior. 

**Self-attention-based**: SAITS- Self-attention based time-seires is currently the best research work for tim-series-imputation that outperforms the reconstruction performance of all the previous RNN/GAN/VAE based architectures. It has been implemented on the datasets of PhysioNet, Air-quality and electricity load monitoring systems. As mentioned earlier, learns missing values from a weighted combination of two diagonally-masked self-attention blocks which explicitly capture both the temporal dependencies and feature correlations for between time steps which in turn improves imputation accuracy and training speed. 

All the previous RNN based networks have memory constraints when dealing with long-term dependency in time series when the number of time-steps missing in the data sample is relatively big. There’s also susceptibility for compounding error for most of these models predicting on the basis of the recently imputated time-series. 
The GAN as well as VAE based research works involve a complex training cycle caused due to issues such as non-convergence and mode-collapse due to their respective loss formulations. 


## 3. Novelty & Rationale

We will be exploring self-attention networks, particularly SAITS for the task of imputation followed by time-series classification for Human Activity Recognition related dataset. There will be a set of analysis that we will focus on namely; 
SAITS inspired model implementation on HAR dataset.
Customizing the SAITS architecture for HAR dataset.
Exploring various randomness models such as MAR, MCAR, MNAR with varied proportions of data missing and suggest necessary improvements to the model.
If possible, develop an end-to-end system for inference of the activity class on real-time time-series signal.
It has been seen that SAITS performs exceptionally well on datasets in the medical, electricity and environmental domain. There exists a considerable similarity in between these different time-series owing to underlying patterns. Similarly, HAR data will have set of underlying patterns which can be readily identified with various ML and DL approaches. Also, BRITS has successfully made use of a reconstructed time series and identified the corresponding task with high accuracy. However, the reconstruction accuracy is not up to the mark. Hence, based on the previous research works and the performance of SAITS in other domains, we believe that it will perform better than previous approaches used for HAR.


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

We will be using two major set of evaluation metrics to determine the success of our research work. 
Metrics for imputation performance:
MAE (Mean Absolute Error), RMSE (Root Mean Square Error), and MRE (Mean Relative Error)
Metrics for classification performance:
Accuracy(percentage of correct predictions),F1-Score(to ensure all class being predicted equally well), ROC-AUC, PR-AUC 
We will develop all the associated insights and diagrams to better understand the performance of our network.


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

A brief summary of the research work mentioned in earlier sections can be found here. There are numerous publications at top conferences which focus on data imputation using architectures based on RNNs/GANs/VAEs/Self-attention. 

In this paper [1], the author developed a Multi-directional Recurrent Neural Network (M-RNN). The main difference of An M-RNN between a bi-directional RNN is that  it sequentially operates across streams.

In this paper [2], the authors construct personalized policies using logged data when there are missing values in the attributes of features as a solution to missing data. It consists of a Variational auto-encoder that predicts a posterior distribution for the missing data.

In this paper [3] the authors uses intelligent data augmentation techniques to handle the missing data. Specifically, the authors use controlled jitter in window length and add artificial misalignments in data timestamps between sensors, along with masking representations of missing data. 

In this paper [4] the authors design a noval deep network architecture using residual bidirectional long short-term memory (LSTM) cells. The main advantage of this model is that residual connections between stacked cells act as highways for gradients, which can pass underlying information directly to the upper layer, effectively avoiding the gradient vanishing problem. 

In this paper [5] proposes SAITS, a novel method based on the self-attention mechanism for missing value imputation in multivariate time series.

In this paper [6] the author proposed method directly learns the missing values in a bidirectional recurrent dynamical system, without any specific assumption.

In this paper [7] the author develop novel deep learning models, namely GRU-D, as one of the early attempts.

In this paper [8] the author propose a new approach, based on a novel deep learning architecture that we call a Multi-directional Recurrent Neural Network that interpolates within data streams and imputes across data streams.

In this paper [9] the author demonstrate a simple strategy to cope with missing data in sequential inputs, addressing the task of multilabel classification of diagnoses given clinical time series.

In this paper [10] the author propose to learn the overall distribution of a multivariate time series dataset with GAN, which is further used to generate the missing values for each sample. 

In this paper [11] the author proposes an end-to-end generative model E²GAN to impute missing values in multivariate time series. With the help of the discriminative loss and the squared error loss, E²GAN can impute the incomplete time series by the nearest generated complete time series at one stage.

In this paper [12] the author take a non-autoregressive approach and propose a novel deep generative model: Non-AutOregressive Multiresolution Imputation (NAOMI) to impute long-range sequences given arbitrary missing patterns.

In this paper [13] the author propose a new deep sequential latent variable model for dimensionality reduction and data imputation.

### 9.b. Datasets

- UCI UCI HAR Dataset

Davide Anguita, Alessandro Ghio, Luca Oneto, Xavier Parra and Jorge L. Reyes-Ortiz. A Public Domain Dataset for Human Activity Recognition Using Smartphones. 21th European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning, ESANN 2013. Bruges, Belgium 24-26 April 2013. 
(https://archive.ics.uci.edu/ml/machine-learning-databases/00240/)

- PAMAP 2 Dataset

A. Reiss and D. Stricker. Introducing a New Benchmarked Dataset for Activity Monitoring. The 16th IEEE International Symposium on Wearable Computers (ISWC), 2012.
(https://www.computer.org/csdl/proceedings-article/iswc/2012/4697a108/12OmNzwZ6pa)

A. Reiss and D. Stricker. Creating and Benchmarking a New Dataset for Physical Activity Monitoring. The 5th Workshop on Affect and Behaviour Related Assistance (ABRA), 2012.
(http://archive.ics.uci.edu/ml/datasets/pamap2%20physical%20activity%20monitoring)

### 9.c. Software

- GitHub [13] is the codebase for BRITS implementation of paper [6]
- GitHub [14] is the codebase for Robust-Deep-Learning-Pipeline
- GitHub codebase for implementation of paper [3]
- GitHub [15] is the codebase for LSTM-Human-Activity-Recognitionimplementation of paper [4]
	

## 10. References

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
(https://papers.nips.cc/paper/2018/hash/96b9bff013acedfb1d140579e2fbeb63-Abstract.html)

[11]  Yonghong Luo, Ying Zhang, Xiangrui Cai, and Xiaojie Yuan. E2GAN: End-to-end generative adversarial network for multivariate time series imputation. In Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI-19, pages 3094–3100. International Joint Conferences on Artificial Intelligence Organization, 7 2019.
(https://www.ijcai.org/proceedings/2019/429)

[12] Yukai Liu, Rose Yu, Stephan Zheng, Eric Zhan, and Yisong Yue. NAOMI: Non-autoregressive multiresolution sequence imputation. In Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019
(https://proceedings.neurips.cc/paper/2019/file/50c1f44e426560f3f2cdcb3e19e39903-Paper.pdf)

[13] Vincent Fortuin, Dmitry Baranchuk, Gunnar Raetsch, and Stephan Mandt. GP-VAE: Deep probabilistic time series imputation. In Silvia Chiappa and Roberto Calandra, editors, Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics, volume 108 of Proceedings of Machine Learning Research, pages 1651–1661. PMLR, 26–28 Aug 2020.
(https://proceedings.mlr.press/v108/fortuin20a.html)

[14] https://github.com/caow13/BRITS

[15] https://github.com/nesl/Robust-Deep-Learning-Pipeline/blob/main/README.md

[16] https://github.com/guillaume-chevalier/LSTM-Human-Activity-Recognition/blob/master/README.md

