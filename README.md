# Used-Car-Price-Prediction-Model

This project builds a machine learning pipeline to predict used car prices based on historical listings data. The workflow includes data collection, cleaning, exploratory analysis, and model training.

## 📁 Project Structure

- `Data/`
  - `raw_data.csv`: Raw scraped car listings.
  - `cleaned_data.csv`: Cleaned dataset after preprocessing.
- `Scripts/`
  - `dataCollection.ipynb`: Scrapes car data from online sources.
  - `cleaningRawData.ipynb`: Cleans and preprocesses the raw data.
- `Notebooks/`
  - `sample.ipynb`: Exploratory Data Analysis (EDA) and modeling.
- `Plan.md`: Step-by-step pipeline plan.
- `requirements.txt`: Python dependencies.

## 🚗 Pipeline Overview

1. **Data Collection:**  
   Scrape car listings (brand, year, mileage, fuel type, transmission, price, etc.) from websites like bikroy.com or olx.com using Python libraries (`requests`, `BeautifulSoup`, or Selenium).

2. **Data Storage:**  
   Save scraped data to `raw_data.csv`.

3. **Data Cleaning:**

   - Remove irrelevant columns, duplicates, and outliers.
   - Standardize units (e.g., remove "km", "Tk").
   - Convert columns to numeric types.
   - Encode categorical variables.
   - Handle missing values.

4. **EDA:**

   - Visualize price trends by year, mileage, and brand.
   - Plot correlations and distributions.

5. **Model Building:**
   - Train regression models (Linear Regression, Random Forest).
   - Evaluate using RMSE, MAE, R².
   - Save the best model for deployment.

## ✅ Deliverables

- Cleaned dataset (`cleaned_data.csv`)
- EDA and modeling notebook (`sample.ipynb`)
- Trained model file

## 📦 Setup

Install dependencies:

```sh
pip install -r requirements.txt
```

## 📚 References

See [Plan.md](Plan.md) for the full pipeline
