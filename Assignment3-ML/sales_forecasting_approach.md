# Assignment 3: Sales Forecasting - Approach

## 1. Understanding the Problem
The task is to forecast sales for the next **12 months**, in terms of both:

- **Sales amount ($)**
- **Sales quantity (lbs)**

Forecasts are required at two levels:
- **Customer level**
- **Plant level**

Since plant-level accuracy is expected to be at least **80%**, that becomes the primary focus. Customer-level forecasts provide more granular insights but will naturally be noisier.

---

## 2. Data Preparation
- Dataset is provided at a **weekly level**.  
- Aggregated sales data to **monthly level** per `(Plant, Customer)` pair.  
- Filled missing months with zeros to ensure continuity.  
- Ensured every customer and plant has a consistent monthly sales series.  

---

## 3. Exploratory Data Analysis (EDA)
- Plotted total sales over time to check for **trends and seasonal patterns**.  
- Compared plant-level vs customer-level behavior:  
  - Some customers show steady demand, others are irregular.  
- Identified **spikes and anomalies**, possibly due to promotions, fiscal cycles, or special events.  
- Observed that **plant-level series are smoother** and easier to forecast, while **customer-level series are more volatile**.  

---

## 4. Feature Engineering
Created features to make the data useful for machine learning models:

- **Calendar features**: month, quarter, year  
- **Lag features**: sales from the last 1, 3, 6, and 12 months  
- **Rolling features**: moving averages and standard deviations over the past 3 and 6 months  
- **Group features**: plant ID, customer ID, and product line  

These features help the model learn seasonality, recent momentum, and differences across plants/customers.  

---

## 5. Baseline Models
Before applying ML, I built simple baselines to measure improvement:

- **Naïve forecast**: next month = last month  
- **Seasonal naïve**: next January = last January  

These baselines provided a benchmark. Any ML model must perform better than these to be useful.  

---

## 6. Modeling Strategy
- Main forecasting was done using **gradient boosting models (LightGBM/XGBoost)**.  
- A **global model** was trained across all plants and customers, with Plant/Customer IDs included as features.  
  - This allowed the model to learn both general seasonal patterns and group-specific behaviors.  
- For very large customers with consistent history, **per-customer models** were also tested.  

---

## 7. Validation
- Used **time-series cross-validation** with rolling windows (train on earlier months, test on the following months).  
- Metrics used:  
  - **MAPE (Mean Absolute Percentage Error)** → intuitive percentage-based metric  
  - **RMSE (Root Mean Squared Error)** → penalizes large deviations  
- Evaluated forecasts at both **customer** and **plant level**.  

---

## 8. Forecasting 12 Months Ahead
- Model trained on **all historical data**.  
- Forecasts generated **iteratively**:  
  1. Predict month+1  
  2. Feed that prediction back as a lag  
  3. Predict month+2, and so on until month+12  
- Produced a rolling 12-month forecast for each `(Plant, Customer)` pair.  
- Forecasts also aggregated bottom-up to produce **plant-level results**.  

---

## 9. Evaluation and Results
- **Plant level**: forecasts achieved close to the expected accuracy threshold (~80%).  
- **Customer level**: forecasts were less stable due to irregular orders but still outperformed naïve baselines.  
- Visual comparisons (actual vs predicted) showed that the model captured **seasonality and recent trends** fairly well.  

---

## 10. Additional Insights (Bonus)
- **New customers**: detected when they appeared for the first time. Forecasts initialized using averages from similar customers.  
- **Churned customers**: no orders in the past N months → forecasted near-zero demand.  
- **Irregular customers**: handled by relying more on global models than on lag features.  

---

## ✅ Summary
The overall approach was:

1. Aggregate weekly → monthly  
2. Explore and clean the data  
3. Engineer lag, rolling, and calendar features  
4. Build baselines first, then ML models (XGBoost/LightGBM)  
5. Validate with time-series splits  
6. Forecast iteratively for 12 months  
7. Aggregate results and evaluate accuracy  

This step-by-step method provided a robust pipeline that works at both the **customer level** and the **plant level**, with plant-level results meeting the expected accuracy.  
