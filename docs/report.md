# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

Provide a brief overview of the project objhectives, approach, and results.

# 1. Introduction

This section should cover the following items:

* Motivation & Objective: What are you trying to do and why? (plain English without jargon)
* State of the Art & Its Limitations: How is it done today, and what are the limits of current practice?
* Novelty & Rationale: What is new in your approach and why do you think it will be successful?
* Potential Impact: If the project is successful, what difference will it make, both technically and broadly?
* Challenges: What are the challenges and risks?
* Requirements for Success: What skills and resources are necessary to perform the project?
* Metrics of Success: What are metrics by which you would check for success?

# 2. Related Work

# 3. Technical Approach

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
    <th class="tg-fymr">MAR</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MAR</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MAR</th>
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
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">SAITS Imputation</td>
    <td class="tg-0pky">0.025206</td>
    <td class="tg-0pky">0.068027</td>
    <td class="tg-0pky">2.19e-01</td>
    <td class="tg-0pky">0.164979</td>
    <td class="tg-0pky">0.308052</td>
    <td class="tg-0pky">1.00e+00</td>
    <td class="tg-0pky">0.142454</td>
    <td class="tg-0pky">0.268954</td>
    <td class="tg-0pky">1.03e+00</td>
  </tr>
</tbody>
</table>


### Classification performance for MCAR, MAR, and MNAR missingness type

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky" rowspan="2"></th>
    <th class="tg-fymr" colspan="3">MCAR</th>
    <th class="tg-fymr" colspan="3">MAR</th>
    <th class="tg-fymr" colspan="3">MNAR</th>
  </tr>
  <tr>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">Zero Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">Mean Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">Median Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">BRITS Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">SAITS Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
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
    <th class="tg-fymr">MAR</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MAR</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MAR</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MAR</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MAR</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">10 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">20 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">30 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">40 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">50 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">60 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">70 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">80 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">90 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
</tbody>
</table>


### Classification performance over varying missingness rate

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
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
    <th class="tg-1wig">Acc.</th>
    <th class="tg-1wig">F1-Score</th>
    <th class="tg-1wig">AU-ROC</th>
    <th class="tg-1wig">Acc.</th>
    <th class="tg-1wig">F1-Score</th>
    <th class="tg-1wig">AU-ROC</th>
    <th class="tg-1wig">Acc.</th>
    <th class="tg-1wig">F1-Score</th>
    <th class="tg-1wig">AU-ROC</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">10 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">20 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">30 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">40 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">50 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">60 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">70 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">80 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">90 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
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
    <th class="tg-fymr">MAR</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MAR</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MAR</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">Zero Imputation</td>
    <td class="tg-0pky">43.028692</td>
    <td class="tg-0pky">296.359563</td>
    <td class="tg-0pky">1.27e+18</td>
    <td class="tg-0pky">60.803443</td>
    <td class="tg-0pky">403.765697</td>
    <td class="tg-0pky">9.00e+17</td>
    <td class="tg-0pky">51.914366</td>
    <td class="tg-0pky">354.229207</td>
    <td class="tg-0pky">1.53e+18</td>
  </tr>
  <tr>
    <td class="tg-fymr">Mean Imputation</td>
    <td class="tg-0pky">1790.0171816</td>
    <td class="tg-0pky">2112.776316</td>
    <td class="tg-0pky">9.79e-01</td>
    <td class="tg-0pky">2685.414685</td>
    <td class="tg-0pky">2879.954673</td>
    <td class="tg-0pky">9.80e-01</td>
    <td class="tg-0pky">2237.756880</td>
    <td class="tg-0pky">2525.974987</td>
    <td class="tg-0pky">9.8e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">Median Imputation</td>
    <td class="tg-0pky">1789.995646</td>
    <td class="tg-0pky">2112.789127</td>
    <td class="tg-0pky">9.79e-01</td>
    <td class="tg-0pky">2685.422465</td>
    <td class="tg-0pky">2879.988146</td>
    <td class="tg-0pky">9.80e-01</td>
    <td class="tg-0pky">2237.775494</td>
    <td class="tg-0pky">2526.036182</td>
    <td class="tg-0pky">9.80e-01</td>
  </tr>
  <tr>
    <td class="tg-fymr">BRITS Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">SAITS Imputation</td>
    <td class="tg-0pky">2.552372</td>
    <td class="tg-0pky">17.20966</td>
    <td class="tg-0pky">0.059293</td>
    <td class="tg-0pky">17.135756</td>
    <td class="tg-0pky">130.071705</td>
    <td class="tg-0pky">0.281622</td>
    <td class="tg-0pky">24.881084</td>
    <td class="tg-0pky">176.31499</td>
    <td class="tg-0pky">0.478812</td>
  </tr>
</tbody>
</table>


### Classification performance for MCAR, MAR, and MNAR missingness type

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky" rowspan="2"></th>
    <th class="tg-fymr" colspan="3">MCAR</th>
    <th class="tg-fymr" colspan="3">MAR</th>
    <th class="tg-fymr" colspan="3">MNAR</th>
  </tr>
  <tr>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">Zero Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">Mean Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">Median Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">BRITS Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">SAITS Imputation</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
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
    <th class="tg-fymr">MAR</th>
    <th class="tg-fymr">MAE</th>
    <th class="tg-fymr">RMSE</th>
    <th class="tg-fymr">MAR</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MAR</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MAR</th>
    <th class="tg-1wig">MAE</th>
    <th class="tg-1wig">RMSE</th>
    <th class="tg-1wig">MAR</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">10 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">20 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">30 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">40 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">50 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">60 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">70 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">80 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">90 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
</tbody>
</table>


### Classification performance over varying missingness rate

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
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
    <th class="tg-fymr">Acc.</th>
    <th class="tg-fymr">F1-Score</th>
    <th class="tg-fymr">AU-ROC</th>
    <th class="tg-1wig">Acc.</th>
    <th class="tg-1wig">F1-Score</th>
    <th class="tg-1wig">AU-ROC</th>
    <th class="tg-1wig">Acc.</th>
    <th class="tg-1wig">F1-Score</th>
    <th class="tg-1wig">AU-ROC</th>
    <th class="tg-1wig">Acc.</th>
    <th class="tg-1wig">F1-Score</th>
    <th class="tg-1wig">AU-ROC</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">10 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">20 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">30 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">40 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">50 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">60 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">70 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">80 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
  <tr>
    <td class="tg-fymr">90 %</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0pky">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
    <td class="tg-0lax">0.0</td>
  </tr>
</tbody>
</table>


# 5. Discussion and Conclusions

# 6. References
