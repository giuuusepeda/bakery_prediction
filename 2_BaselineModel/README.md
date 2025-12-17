# Baseline Model
---

We have made 2 baseline models. The first one is a modified regression and the second one utilizes the random forest algorithm.

## 1. Linear regression with the cylindrical functions for temporal features

**Performace on Kaggle public leaderboard (21% of test data) : 0.21517**

*Mean Absolute Percentage Error (On entire dataset): 23.6629%*
- Warengruppe: 1, MAPE: 23.9122%
- Warengruppe: 2, MAPE: 18.5609%
- Warengruppe: 3, MAPE: 23.3061%
- Warengruppe: 4, MAPE: 26.0139%
- Warengruppe: 5, MAPE: 19.9829%
- Warengruppe: 6, MAPE: 65.3472%

## 2. Random Forest

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

> **Features:** 
Warengruppe (not encodded - worked better then encodded)-
Umsatz - KielerWoche- Bewoelkung-	Temperatur-	Windgeschwindigkeit- Woche-	Monat-
Ferien-	sunny-	cloudy-	rainy-	thunderstorm-	is_weekend-	sin_Monat-	cos_Monat-	
sin_Wochentag-	cos_Wochentag- 
(doubbled features encoded and not)

*Mean Absolute Percentage Error: 23.6629%*

- Warengruppe: 1, MAPE: 19.907234%
- Warengruppe: 2, MAPE: 16.2921759%
- Warengruppe: 3, MAPE: 19.681718%
- Warengruppe: 4, MAPE: 24.553163%
- Warengruppe: 5, MAPE: 17.916015%
- Warengruppe: 6, MAPE: 38.147771%
