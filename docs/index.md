# Abstract

Traditional machine learning methods for Human Activity Recognition (HAR) are significantly impacted due to data missingness. Our goal through this project is to build robust models that not only impute these signals but also build robust classifiers that can infer HAR classes from these imputed signals. Recurrent Neural Networks (RNN) have been proven to work well with time-series data due to their ability to learn temporal features and dependencies. Therefore, one of the SOTA imputation architectures we have implemented for HAR is a Bidirectional RNN based on the BRITS architecture. Also, recently self-attention mechanism-based imputation models have been used in missing value imputation for multivariate time series. Therefore, another SOTA imputation architecture we have implemented is a self-attention mechanism-based SAITS architecture. Our overall goal is to perform a comparative study between baseline models like zero-filling, mean, and median imputation, and SOTA models like BRITS and SAITS, not just for missing value imputation; but also for the downstream task of HAR classification. Most research on imputation only focuses on random Missingness, also known as Missingness Completely at Random (MCAR); but IMU signals encounter other types of Missingness too, namely Missingness at Random (MAR) and Missingness Not at Random (MNAR). Therefore, through this project, we have also extensively evaluated these models on various missingness types, as well as varying missingness rates, all performed on two popular publicly available HAR datasets: UCI HAR and PAMAPS2.

# Team

* Rushi Yogeshkumar Bhatt
* Ronak Kaoshik
* Jinru Cai

# Required Submissions

* [Proposal](https://github.com/RushiBhatt007/ece209as_project/blob/main/docs/proposal.md)
* [Midterm Checkpoint Presentation Slides](https://github.com/RushiBhatt007/ece209as_project/blob/main/docs/Midterm_checkpoint_presentation.pdf)
* [Final Presentation Slides](https://github.com/RushiBhatt007/ece209as_project/blob/main/docs/Final%20Presentation%20Slides.pdf)
* [Final Report](https://github.com/RushiBhatt007/ece209as_project/blob/main/docs/report.md)
