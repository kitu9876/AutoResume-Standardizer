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
- Plot total sales over time to check for **trends and seasonal patterns**.  
- Compared plant-level vs customer-level behavior:  
  - Some customers show steady demand, others are irregular.  
- Identified **spikes and anomalies**, possibly due to promotions, fiscal cycles, or special events.  
- Observed that **plant-level series are smoother** and easier to forecast, while **customer-level series are more volatile**.  

---

## 4. Feature Engineering
Created features to make the data useful for machine learning models:
As if we use the models like GBM(Gradient-Boost),XG Boost, Random Forest, they can't see the future directly like ARIMA does.
So, we need to teach them patterns from the past by creating features that describes the time series.

- **Calendar features**: month, quarter, year  
- **Lag features**: sales from the last 1, 3, 6, and 12 months  
- **Rolling features**: moving averages and standard deviations over the past 3 and 6 months  
- **Group features**: plant ID, customer ID, and product line  

Thus, these features will help the model learn seasonality, recent momentum, and differences across plants/customers.  

---

## 5. Baseline Models
Before applying ML, simple baselines can be built to measure improvement:

Type: Simple heuristic / baseline method
Concept:
1. The simplest possible forecast.
2. Assumes that the next month’s sales will be exactly the same as the previous month.

Idea: Predict the next value as exactly the same as the last observed value.

Formula:  𝑦^t+1=y^t
	​
Characteristics:

1. No training, no parameters, no learning from data.
2. Extremely simple, only works “as-is” from the observed series.
3. Serves as a benchmark for other models.

- **Naïve forecast**: next month = last month  
- **Seasonal naïve**: next January = last January  

These baselines provided a benchmark. Any ML model must perform better than these to be useful.  

---

## 6. Modeling Strategy
- Main forecasting can be done using **gradient boosting models (LightGBM/XGBoost)**.  
- A **global model** can be trained across all plants and customers, with Plant/Customer IDs included as features.  
  - This allowed the model to learn both general seasonal patterns and group-specific behaviors.  
- For very large customers with consistent history, **per-customer models** can also be tested.  

---

## 7. Validation
- Should be used the **time-series cross-validation** with rolling windows (train on earlier months, test on the following months).  
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
- **Plant level**: forecasts can be achieved close to the expected accuracy threshold (~80%).  
- **Customer level**: forecasts can be less stable due to irregular orders but still it should  outperformed naïve baselines.  
- Visual comparisons (actual vs predicted) scan be shown that the model captured **seasonality and recent trends** fairly well.  

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

This step-by-step method provides a robust pipeline that works at both the **customer level** and the **plant level**, with plant-level results meeting the expected accuracy.  
