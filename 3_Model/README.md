# Model Definition & Evaluation

This folder contains the final models evaluated for the sales forecasting task.  
Performance is reported using **MAPE (Mean Absolute Percentage Error)** on both **validation data** and the **Kaggle public leaderboard** (21% of the test set).

---

## Tree-Based Models

### 1. Random Forest

**Kaggle Public Leaderboard (21% test):** 0.18380

**Kaggle Private Leaderboard (79% test):** 0.17292

**Best Validation MAPE:** 0.20232

**Best Hyperparameters**
```
n_estimators: 600
max_depth: 20
min_samples_split: 20
min_samples_leaf: 2
max_features: 1.0
bootstrap: True
```

Warengruppe	MAPE
| Warengruppe | MAPE   |
|------------|--------|
| 1          | 0.1991 |
| 2          | 0.1629 |
| 3          | 0.1968 |
| 4          | 0.2455 |
| 5          | 0.1792 |
| 6          | 0.3815 |


*Notes*
- Demonstrates strong generalization, with improved performance from validation (MAPE 0.20232) to both Kaggle leaderboards.
- Achieves solid and consistent results across most product groups, particularly Warengruppe 2 and 5.
- Warengruppe 6 shows substantially higher error, indicating difficulty modeling this category compared to others.
- Lower Private Leaderboard MAPE (0.17292) compared to Public suggests robust performance on unseen data.


### 2. XGBoost

**Kaggle Public Leaderboard (21% test): 0.19987**

**Kaggle Private Leaderboard (79% test): 0.17033**

**Best Validation MAPE: 0.20016**


**Best Hyperparameters**


```
n_estimators: 1000
max_depth: 7
subsample: 1.0
reg_lambda: 5.0
reg_alpha: 0.0001
min_child_weight: 10
learning_rate: 0.01
gamma: 0.0
colsample_bytree: 0.8
```

Validation MAPE by Product Group (Warengruppe)

Warengruppe	MAPE
| Warengruppe | MAPE   |
|------------|--------|
| 1          | 0.2024 |
| 2          | 0.1564 |
| 3          | 0.1867 |
| 4          | 0.2465 |
| 5          | 0.1801 |
| 6          | 0.3827 |


Notes
- Shows competitive private leaderboard performance (MAPE 0.17033), outperforming Random Forest on the private split.
- Validation MAPE (0.20016) is close to Random Forest, but category-level errors are more polarized.
- Performs well for Warengruppe 2 and 3, while Warengruppe 6 remains a major source of error, similar to Random Forest.
- The gap between Public and Private leaderboard scores suggests better generalization than initial public performance indicates.


## Neural Network Models
### 3. Dense Neural Network
Architecture: 3 Dense layers + 2 Dropout layers

**Kaggle Public Leaderboard (21% test): 0.20713**
**Kaggle Private Leaderboard (79% test): 0.19180**
**Best Validation MAPE: 0.1877**

Validation MAPE by Product Group (Warengruppe)

| Warengruppe | MAPE   |
|------------|--------|
| 1          | 0.1906 |
| 2          | 0.1242 |
| 3          | 0.1798 |
| 4          | 0.2239 |
| 5          | 0.1503 |
| 6          | 0.4245 |


Notes
- Achieves the best validation performance among all models (MAPE 0.1877).
- Exhibits strong performance on specific categories, especially Warengruppe 2 and 5.
- However, shows weaker generalization, with higher error on both Public (0.20713) and Private (0.19180) leaderboards.
- Very high error on Warengruppe 6 indicates sensitivity to data sparsity or volatility in this category.

## Summary

**Best validation performance:** Dense Neural Network

**Best private leaderboard performance:** XGBoost

**Most stable across splits:** Random Forest

**Common challenge across all models:** Warengruppe 6
