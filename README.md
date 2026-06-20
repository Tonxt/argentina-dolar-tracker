# Argentina Dolar Tracker

🔗 **[Live Dashboard](https://dolar-tracker-lisandro.streamlit.app)** — view real-time Argentine exchange rates

## Overview
An automated ETL pipeline that tracks Argentine peso to US dollar exchange rates. The system fetches live data daily from a public API, stores it in a SQLite database, and analyzes the accumulated history to reveal exchange rate trends across different dollar types (official, blue, MEP, CCL, crypto, wholesale, and card rate).

## What It Does
1. **Extract**: Calls the [DolarAPI](https://dolarapi.com) to fetch current exchange rates for all dollar types
2. **Transform**: Selects relevant fields (rate type, buy/sell price, update timestamp) and tags each record with the execution timestamp
3. **Load**: Inserts the records into a local SQLite database, building a historical dataset over time
4. **Automate**: Runs once a day via Windows Task Scheduler, requiring no manual execution
5. **Analyze**: A separate script reads the accumulated data, deduplicates same-day entries, pivots it into a time series, and visualizes the trend for each dollar type
6. **Visualize**: An interactive Streamlit dashboard displays live exchange rates, deployed publicly so anyone can check current prices without running any code

## Key Findings (June 10–16, 2026)
- **Dolar Blue had the sharpest movement**, rising from R$1,450 to R$1,470 — the largest change among all tracked rate types in this period.
- **CCL (Contado con Liqui) and Crypto dollar rates crossed paths**: CCL declined from R$1,509.7 to R$1,498.1, while the Crypto rate rose slightly from R$1,500.9 to R$1,501.2.
- **Most other rate types** (official, wholesale, card) remained relatively stable across the 6-day window.

## Technologies Used
- **Python** — pipeline and analysis logic
- **Requests** — API consumption
- **SQLite3** — local data storage
- **Pandas** — data cleaning, deduplication, and pivoting
- **Matplotlib** — time series visualization
- **Streamlit** — interactive dashboard and public deployment
- **Windows Task Scheduler** — daily automation
- **Git / GitHub** — version control and portfolio hosting

## Project Structure
```
argentina-dolar-tracker/
├── src/
│   ├── pipeline.py        # ETL: fetches and stores exchange rate data
│   ├── analisis.py         # Reads, cleans, and visualizes historical data
│   ├── ver_datos.py        # Utility script to inspect database contents
│   ├── dashboard.py        # Streamlit dashboard (local, reads from SQLite)
│   └── dashboard_deploy.py # Streamlit dashboard (production, reads from API)
├── data/                  # SQLite database (excluded from version control)
├── run_pipeline.bat       # Batch script used by Task Scheduler
├── requirements.txt
└── README.md
```

## Data Source
[DolarAPI](https://dolarapi.com) — free public API for Argentine exchange rates, no authentication required.

## How to Run
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the pipeline: `python src/pipeline.py`
6. After running it on multiple days, generate the analysis: `python src/analisis.py`
7. To view the local dashboard: `streamlit run src/dashboard.py`

> To automate daily runs, schedule `run_pipeline.bat` using Windows Task Scheduler.
> The production dashboard (`dashboard_deploy.py`) is deployed live and requires no local setup — see the link at the top of this README.