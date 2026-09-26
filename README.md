# DecisIQ — Enterprise AI Decision Intelligence Platform

DecisIQ is a decision intelligence platform I built to help businesses understand their performance using data analytics, machine learning, and AI-assisted analysis.

The main idea is to connect business data with analytics and predictive models so that users can understand what is happening, investigate the reasons behind it, and explore possible actions.

**Live Demo:** https://decisiq-enterprise-ai-decision.onrender.com/

## What It Includes

* Executive dashboard for monitoring business performance
* Ask Your Data AI for natural-language analysis
* Revenue and gross-margin tracking
* 30/60/90-day revenue forecasting
* Customer 360 and churn analysis
* RFM-based customer segmentation
* Anomaly detection
* Marketing attribution and campaign analysis
* What-If scenario simulation
* Regional and category performance analysis
* Power BI export
* Data workspace for business data

## Dashboard

The main dashboard provides an overview of revenue, customers, orders, churn risk, forecasts, category profitability, and regional performance.

The current demo includes:

* ₹7.87 Cr monthly net revenue
* 3,599 active customers
* ₹31,221 average order value
* 20.4% average churn risk
* ₹8.82 Cr next-month revenue forecast
* 24-month revenue and gross-margin trends

These figures are part of the project's demo dataset and are intended to demonstrate how the platform works.

## Decision Intelligence

DecisIQ is built around four questions:

```text
What happened?
      ↓
Why did it happen?
      ↓
What could happen next?
      ↓
What actions can be considered?
```

For example, the dashboard can highlight potential business issues such as high-value customer inactivity, regional performance changes, or inefficient marketing campaigns and allow the user to investigate them further using the AI analysis features.

## Machine Learning

The platform uses machine learning for different parts of the analysis, including:

* Revenue forecasting
* Customer churn prediction
* Customer segmentation
* Anomaly detection
* Predictive risk scoring

The dashboard also provides confidence intervals for forecast results where applicable.

## Data & Analytics

The project uses a star-schema approach for organizing business data and combines SQL analytics with machine learning.

The data covers areas such as:

* Customers
* Orders
* Products
* Regions
* Marketing campaigns
* Daily business performance

## Tech Stack

| Area                  | Technologies                |
| --------------------- | --------------------------- |
| Backend               | Python, FastAPI, Uvicorn    |
| Database              | DuckDB, SQLite              |
| Data Analysis         | Pandas, NumPy               |
| Machine Learning      | Scikit-learn                |
| Analytics             | SQL, CTEs, Window Functions |
| Business Intelligence | Power BI, DAX               |
| Frontend              | React, Vite, Tailwind CSS   |
| Visualization         | Recharts                    |

## Project Structure

```text
DecisIQ/
├── backend/
├── frontend/
├── powerbi_export_pack/
├── sql_analytics/
├── db.py
├── requirements.txt
├── Dockerfile
├── render.yaml
├── Procfile
└── run_platform.bat
```

## Running Locally

### Requirements

* Python 3.10+
* Node.js 18+
* npm

### Backend

```bash
python backend/app.py
```

API:

```text
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

On Windows, `run_platform.bat` can be used to start the platform.

## Why I Built It

I built DecisIQ as a way to work on a project that combines the different parts of a real analytics application instead of building only a dashboard or only a machine learning model.

It gave me hands-on experience with data modeling, SQL, Python, machine learning, backend APIs, React, visualization, and business intelligence.

## Deployment

The project is currently deployed on Render.

**Live Demo:**
https://decisiq-enterprise-ai-decision.onrender.com/

The complete frontend and backend source code are included in this repository.
