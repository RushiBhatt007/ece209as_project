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
    <td class="tg-0pky">0.431289</td>
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
    <td class="tg-0pky">40.42%.0</td>
    <td class="tg-0pky">0.42</td>
  </tr>
  <tr>
    <td class="tg-fymr">BRITS Imputation</td>
    <td class="tg-0pky">91.17%</td>
    <td class="tg-0pky">0.94</td>
    <td class="tg-0pky">86.62%.0</td>
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
    <td class="tg-0pky">10.514203</td>
    <td class="tg-0pky">89.759356</td>
    <td class="tg-0pky">0.351535</td>
    <td class="tg-0pky">37.548802</td>
    <td class="tg-0pky">389.854345</td>
    <td class="tg-0pky">0.789765</td>
    <td class="tg-0pky">39.749156</td>
    <td class="tg-0pky">319.851974</td>
    <td class="tg-0pky">1.00e+00</td>
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
