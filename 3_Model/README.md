# Model Definition and Evaluation


## Tree Models
### 1. Random Forest

**Performace on Kaggle public leaderboard (21% of test data) : 0.18380**

Best VAL MAPE: 20.232120765597696

```
Best params: {
'n_estimators': 600, 
'min_samples_split': 20, 
'min_samples_leaf': 2, 
'max_features': 1.0, 
'max_depth': 20, 
'bootstrap': True}
```


(doubbled features encoded and not)

*Mean Absolute Percentage Error: 23.6629%*

- Warengruppe: 1, MAPE: 19.907234%
- Warengruppe: 2, MAPE: 16.2921759%
- Warengruppe: 3, MAPE: 19.681718%
- Warengruppe: 4, MAPE: 24.553163%
- Warengruppe: 5, MAPE: 17.916015%
- Warengruppe: 6, MAPE: 38.147771%


### 2. XGBoost 

**Performace on Kaggle public leaderboard (21% of test data) : 0.19987**

Best VAL MAPE: 17.580237030059802

```
Best params: {
'n_estimators': 600, 
'min_samples_split': 20, 
'min_samples_leaf': 2, 
'max_features': 1.0, 
'max_depth': 20, 
'bootstrap': True}
```


(doubbled features encoded and not)

*Mean Absolute Percentage Error: 23.6629%*

- Warengruppe: 1, MAPE: 19.907234%
- Warengruppe: 2, MAPE: 16.2921759%
- Warengruppe: 3, MAPE: 19.681718%
- Warengruppe: 4, MAPE: 24.553163%
- Warengruppe: 5, MAPE: 17.916015%
- Warengruppe: 6, MAPE: 38.147771%

## Neural Network

# 3. 3 Dense layers + 2 dropout layers 
