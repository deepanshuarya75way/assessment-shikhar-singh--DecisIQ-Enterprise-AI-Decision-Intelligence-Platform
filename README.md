# DecisIQ — Enterprise AI Decision Intelligence Platform

DecisIQ is a full-stack analytics and decision-support platform that I built to explore how data analytics, machine learning, and AI can be combined to solve common business problems.

The main idea is simple: instead of only showing what happened in the business, the platform tries to help answer why it happened, what might happen next, and what actions could be considered.

**Live Demo:** https://decisiq-enterprise-ai-decision.onrender.com/

## What the Project Does

DecisIQ brings several business analytics features together in one application:

* Executive dashboard for tracking important business KPIs
* Natural-language data analysis through the "Ask Your Data" feature
* Root-cause analysis across customers, products, regions, and pricing
* Customer 360 with RFM-based segmentation
* Customer churn prediction using machine learning
* 30, 60, and 90-day revenue forecasting
* Anomaly detection for unusual business activity
* Marketing campaign and ROAS analysis
* What-if simulations for pricing, retention, marketing budgets, and costs

## How It Works

```text
Raw Business Data
        |
        v
Star-Schema Data Warehouse
        |
        v
SQL Analytics + Machine Learning
        |
        v
AI Decision Layer
        |
        +-------------------+
        |                   |
        v                   v
What-If Simulator      Executive Dashboard
```

The data is first organized into a star-schema database. SQL is then used for business analysis and aggregations, while machine learning models are used for forecasting, churn prediction, segmentation, and anomaly detection.

The results are exposed through the backend API and displayed through the React frontend.

## Main Features

### Executive Dashboard

The dashboard provides an overview of business performance through metrics such as:

* Revenue
* Active customers
* Average Order Value
* Gross margin
* Customer churn risk
* Regional performance
* Category performance

### Ask Your Data

The Ask Your Data feature allows users to ask questions about business performance in natural language.

For example:

> Why did revenue decrease this month?

The system can break the problem down by different dimensions such as products, customers, regions, pricing, and marketing channels.

The analysis follows a simple structure:

1. What happened?
2. Why did it happen?
3. What could happen next?
4. What actions could be considered?

### Customer 360 and Churn Prediction

Customer data is analyzed using RFM (Recency, Frequency, Monetary) analysis to create customer segments such as Champions, Loyal, At-Risk, and Lost.

A Random Forest model is also used to estimate customer churn risk using behavioral features.

### Revenue Forecasting

The forecasting module generates 30, 60, and 90-day revenue projections.

The model uses historical data along with features such as:

* Lag values
* Moving averages
* Day-of-week patterns
* Monthly patterns
* Cyclical time features

### Anomaly Detection

The platform uses Isolation Forest and statistical methods to identify unusual changes in business metrics.

Examples include sudden revenue drops, changes in return rates, and unusual regional or funnel performance.

### What-If Simulator

The simulator allows users to experiment with different business scenarios before making a decision.

Some examples include:

* Changing product prices
* Estimating customer retention campaign impact
* Moving marketing budget between channels
* Testing changes in operating costs

The simulator is intended for scenario analysis rather than treating the results as guaranteed predictions.

## Data Warehouse

The project uses a star-schema structure.

### Dimension Tables

```text
dim_customers
dim_products
dim_regions
dim_marketing_campaigns
```

### Fact Tables

```text
fact_orders
fact_order_items
fact_daily_business_pulse
```

This structure makes it easier to analyze business data across customers, products, regions, campaigns, and time.

## Machine Learning

The project currently uses several machine learning and statistical techniques:

* Random Forest for churn prediction
* Isolation Forest for anomaly detection
* Ridge Regression for predictive modeling
* RFM analysis for customer segmentation
* Lag and rolling features for forecasting
* StandardScaler for feature preprocessing

## Tech Stack

| Area                  | Technologies                |
| --------------------- | --------------------------- |
| Backend               | Python, FastAPI, Uvicorn    |
| Data Analysis         | Pandas, NumPy               |
| Database              | SQLite, DuckDB, PostgreSQL  |
| Machine Learning      | Scikit-learn                |
| Analytics             | SQL, CTEs, Window Functions |
| Business Intelligence | Power BI, DAX               |
| Frontend              | React, Vite, Tailwind CSS   |
| Visualization         | Recharts                    |

## Running Locally

### Requirements

* Python 3.10+
* Node.js 18+
* npm

### Start the Backend

```bash
python backend/app.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Start the Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at:

```text
http://localhost:5173
```

On Windows, the complete application can also be started using:

```text
run_platform.bat
```

## Why I Built This

I built DecisIQ to work on a project that connects different areas of data and software development instead of focusing on just one dashboard or machine learning model.

While working on it, I worked with data modeling, SQL, Python, machine learning, APIs, React, visualization, and business intelligence.

The overall goal was to build a single system where historical analysis, predictive models, and scenario analysis can work together to support business decisions.

## Live Demo

https://decisiq-enterprise-ai-decision.onrender.com/
