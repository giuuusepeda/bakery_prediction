# Baseline Model - Multiple Linear Regression

For building a baseline model we wanted to begin with simpler assumptions and come up with a model that is low on computational cost. After multiple trial and error we have choosen *Multiple Linear Regression* with interaction among variables and harmonic features (Fourier Terms to capture the cyclic pattern of Weekdays and Months).

## Feature Selection
 
**Interaction Variables** : Warengruppe (Categorical Variable) has 6 unique categories. Each category interacted with -

> KielerWoche,  is_weekend,  Temperatur,  Ferien,  Feiertag

**Fourier Terms** : We also captured the global seasonality with - 

> sin_Monat, cos_Monat, sin_Wochentag, cos_Wochentag

The implementation of this model is discussed in detail inside the **04_sm_lin_reg_extended.ipynb** notebook.

## Model Evaluation

The performance comparison on training set and validation set is shown below.

| Metric | Training Set Performance | Validation Set Performance |
| :--- | :--- | :--- |
| **R² Score** | 0.8142 | 0.8071 |
| **MAE** | 38.3755 | 38.3217 |
| **MSE** | 4055.4493 | 3263.3488 |
| **RMSE** | 63.6824 | 57.1257 |
| **MAPE (Overall)** | 22.7875% | 23.6629% |

The MAPEs across the Product Groups (Warengruppe) were as follows - 

| Warengruppe | Training Set MAPE | Validation Set MAPE |
| ----------- | ----------- | ----------- |
| **1** | 26.1456% | 23.9122% |
| **2** | **15.0560%** | **18.5609%** |
| **3** | 22.7948% | 23.3061% |
| **4** | 29.3436% | 26.0139% |
| **5** | 15.9847% | 19.9829% |
| **6** | **52.8359%** | **65.3472%** |

So the model performed best on Warengruppe 2 and worst on Warengruppe 6.

## Performance on Kaggle

After Kaggle submission, we got the following result -

Private score (79% of test data) :    **0.21096**

Public score (21% of test data) :     **0.21517**



