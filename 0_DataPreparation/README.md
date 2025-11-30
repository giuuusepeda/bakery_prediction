# Data Preparation

ToDO

Add the steps 

Notebook 01:
1. pre-processing unsatz adding test dates and dates that where missing (considered null faturing-Umsatz)
Notbook 02:
2. Merged 3 dataset - left(left(New_Umsatz, Kiwo), Wetter)
3. inputation 
    a. Kiwo - 0 for days with not kiwo(1)
    b. weather - for missing  variables "Bewoelkung", "Temperatur" and/or "Windgeschwindigkeit" Inputated with mean of day after and before

All missing values were between 2016-12-11 and 2017-11-08
Means for that period Before and After Inputation
Mean Bewoelkung before imputation: 4.945510835913312
Mean Bewoelkung after imputation: 4.887049083382614
Mean Temperatur before imputation: 12.10357675761194
Mean Temperatur after imputation: 11.987884596514277
Mean Windgeschwindigkeit before imputation: 11.042603863455941
Mean Windgeschwindigkeit after imputation: 11.038623226484498

    c. For some days, that were discrepancies for weather variables between "Warengruppe"1-5 and 6. Problem was solved replicating values for group 1 for all groups.
