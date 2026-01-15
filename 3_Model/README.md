# Model Definition and Evaluation


## Tree Models
### 1. Random Forest

**Performace on Kaggle public leaderboard (21% of test data) : 0.18380**

Best VAL MAPE: 0.20232120765597696

```
Best params: 
n estimators: 600
max depth: 20
min samples split: 20
min samples leaf: 2
max features: 1.0
bootstrap: True

```


(doubbled features encoded and not)

*Mean Absolute Percentage Error: 0.236629*

- Warengruppe: 1, MAPE: 0.19907234
- Warengruppe: 2, MAPE: 0.162921759
- Warengruppe: 3, MAPE: 0.19681718
- Warengruppe: 4, MAPE: 0.24553163
- Warengruppe: 5, MAPE: 0.17916015
- Warengruppe: 6, MAPE: 0.38147771


### 2. XGBoost 

**Performace on Kaggle public leaderboard (21% of test data) : 0.19987**

Best VAL MAPE: 0.17580237030059802

```
Best params: 
n_estimators: 1000 
max_depth: 7
subsample: 1.0 
reg lambda: 5.0
reg alpha: 0.0001
min child weight: 10
learning rate: 0.01
gamma: 0.0
col sample by tree: 0.8

```


(doubbled features encoded and not)

*Mean Absolute Percentage Error: 0.236629*

- Warengruppe: 1, MAPE: 0.19907234
- Warengruppe: 2, MAPE: 0.162921759
- Warengruppe: 3, MAPE: 0.19681718
- Warengruppe: 4, MAPE: 0.24553163
- Warengruppe: 5, MAPE: 0.17916015
- Warengruppe: 6, MAPE: 0.38147771

## Neural Network

# 3. 3 Dense layers + 2 dropout layers 

**Performace on Kaggle public leaderboard (21% of test data) : 0.18380**

Best VAL MAPE: 0.20232120765597696

- Warengruppe: 1, MAPE: 0.19058673
- Warengruppe: 2, MAPE: 0.12424456
- Warengruppe: 3, MAPE: 0.17984806
- Warengruppe: 4, MAPE: 0.22388828
- Warengruppe: 5, MAPE: 0.15028076
- Warengruppe: 6, MAPE: 0.42447279