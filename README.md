# Tech Economy Index (TEI): Analyzing Global Digital Competitiveness
A data science project analyzing and predicting global digital competitiveness using economic and technological indicators.
## Overview

The Tech Economy Index (TEI) is a data science project that measures and predicts a country’s digital competitiveness based on economic and technological indicators.
It combines data from global organizations such as the World Bank, OECD, UNESCO, and ITU, and applies machine learning models to forecast digital growth trends.

This project was developed as part of my IBM Data Science Professional Certificate learning path and personal portfolio work to strengthen my skills in Python, SQL, and machine learning.
## Objectives

- Construct a composite Tech Economy Index (TEI) to quantify digital competitiveness.

- Explore relationships between technology adoption, innovation, and economic performance.

- Predict next-year TEI scores using ML models (Regression, Random Forest, XGBoost).

- Visualize global digital trends and key drivers of competitiveness.

  ## Data Sources
- World Bank Open Data – GDP per capita, internet users, broadband subscriptions, R&D expenditure, high-tech exports

- OECD Data – innovation, startup density, ICT investment

- ITU (International Telecommunication Union) – digital access and connectivity metrics

- UNESCO / WIPO – researchers, patents, education indicators

- Global Innovation Index (for validation)

## Tech Stack  
Category	Tools / Libraries
- Languages:	Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
- Database:	PostgreSQL / MySQL (for indicator storage and queries)
- ML Models:	Linear Regression, Ridge/Lasso, Random Forest, XGBoost
- Visualization:	Plotly / Power BI / Tableau
- Environment:	Jupyter Notebook, GitHub

## Methodology

- Data Collection & Cleaning: Download and harmonize indicators (2010–2024).

- Index Construction: Normalize indicators, assign weights, and aggregate into pillars (Connectivity, Innovation, Human Capital, Market).

- Modeling: Train ML models to predict next-year TEI using time-based train/test split.

- Explainability: Use feature importance and SHAP values to interpret key drivers.

- Visualization: Build maps and dashboards to compare countries and trends.

## Project Structure
tech-economy-index/
│
├── data/
│   ├── raw/           # Original datasets
│   ├── interim/       # Cleaned/intermediate data
│   └── processed/     # Modeling-ready datasets
│
├── notebooks/
│   ├── 01_download_clean.ipynb
│   ├── 02_index_construction.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_explainability.ipynb
│   └── 05_visualization.ipynb
│
├── src/
│   ├── clean.py
│   ├── index.py
│   ├── model.py
│   └── viz.py
│
├── sql/
│   ├── schema.sql
│   └── sample_queries.sql
│
├── docs/
│   ├── methodology.md
│   └── report.md
│
├── requirements.txt
└── README.md

## Future Work

Incorporate real-time data APIs (e.g., IMF, OECD)

Add dashboard (Plotly / Power BI) for interactive visualization

Extend ML pipeline to forecast 3–5 years ahead

Automate ETL and data updates via cloud pipeline

## Author

### Aybars Karahan
- Technical University of Munich — B.Sc. Management & Data Science
->> aybars.karahan@tum.de
