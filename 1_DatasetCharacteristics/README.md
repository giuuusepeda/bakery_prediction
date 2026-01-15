# Dataset Characteristics

After importing the data and preprocessing it. We will look explore the dataset, highlighting possible patterns and performing some descriptive statistical analysis.

## Exploratory Data Analysis

These are some of the exploratory data analysis performed on the merged dataset

- Total revenue by product groups
- Avg sales by weekdays
- Top 3 performing products on week days
- Saisonbrot sales on weekdays



### Notebooks

#### 1 `exploratory_data_analysis.ipynb`
**Goal:** General EDA of the merged dataset.  
**What it covers:**
- Dataset overview (basic structure, types)
- Missing values checks
- Feature distributions
- Possible biases
- Correlation exploration


#### 2 `sm_eda_bakery_sales.ipynb`
**Goal:** EDA + time-series oriented analysis with calendar features and product/category views.  
**What it covers:**
- Import & initial exploration
- Calendar features (weekday, month, year, etc.)
- Product table creation / merging (if applicable in your pipeline)
- Filtering by date ranges
- Total sales by product categories
- “Top products by weekday”
- Monthly patterns and sales trends
- Distribution of daily sales

---

#### 3 `sales_by_product_groups_bw.ipynb`
**Goal:** Sales analysis by product group with smoothing/rolling metrics.  
**What it covers:**
- Grouping by `Warengruppe`
- Rolling averages (e.g., `Umsatz_rolling`)
- Time-based comparison plots per product group

---

### Scripts

#### `sales_and_temperatures.py`
**Goal:** Create yearly plots of **sales vs. temperature** using a two-axis chart + 30-day rolling mean trends.  
**Main idea:**
- Filter data by year (`df["Datum"].dt.year == year`)
- Compute rolling means for `Umsatz` and `Temperatur` (30-day window, centered)
- Plot both series with trends and export as PNG


### Generated Plots (PNGs)
Yearly plots showing:
- **Umsatz (sales)** (raw + 30-day trend)
- **Temperatur (°C)** (raw + 30-day trend)

Files include:
- `sales_temperature_2013.png`
- `sales_temperature_2014.png`
- `sales_temperature_2015.png`
- `sales_temperature_2016.png`
- `sales_temperature_2017.png`
- `sales_temperature_2018.png`

---

## Outputs & Interpretation

- **Rolling means (30-day)** help reveal seasonal trends by smoothing daily volatility.
- Overlaying **temperature** and **sales** helps visually assess co-movement (e.g., higher sales during warmer periods depending on product mix).
- Group-based notebooks help identify which `Warengruppe` contributes most to overall seasonality and weekday effects.

# Additional Visualizations

- `distributions.png`  
  Histograms of all main features (sales, weather, calendar, and categorical encodings) to assess distributions, skewness, class imbalance, and potential preprocessing needs.

- `corr_heatmap.png`  
  Pearson correlation heatmap of numerical features highlighting relationships between sales, weather variables, and calendar features, as well as strong multicollinearity among time-based variables.





