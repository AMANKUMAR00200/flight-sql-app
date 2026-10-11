# ✈️ Flight Analytics Dashboard

A Streamlit-based flight analytics dashboard that uses a MySQL database to explore flight routes, compare ticket prices, and visualize airline and airport traffic patterns. The project also includes a Jupyter notebook for cleaning the flight dataset and loading it into MySQL.

## Features

- **Route & Traffic Analysis:** Select a source and destination city to view matching airlines, journey dates, routes, and prices.
- **Price Analysis:** Visualize average ticket prices by journey date for a selected airline and route.
- **Flight Analytics Dashboard:** View total flights, number of airlines, number of cities, average ticket price, airline distribution, and city traffic.
- **Data cleaning:** Inspect missing values and duplicates, remove duplicate records and rows without route information, and standardize the `New Delhi` destination label to `Delhi`.
- **Interactive visualizations:** Plotly charts embedded in Streamlit.

## Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- MySQL
- PyMySQL / SQLAlchemy
- Jupyter Notebook

## Project Structure

```text
flight-analytics-dashboard/
├── st.py                              # Streamlit dashboard
├── dbhelper.py                        # MySQL queries and database helper
├── crud.py                            # Database connector import (currently minimal)
├── data_analysis_flight.ipynb         # Data cleaning and MySQL loading workflow
├── flights_cleaned - flights_cleaned.csv  # Flight dataset
├── requirements.txt                   # Python dependencies
└── README.md
```

## Prerequisites

- Python 3.10 or later
- MySQL Server
- A MySQL database named `dsmp`
- The flight dataset CSV included in this repository

## Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Start MySQL and create the database:

```sql
CREATE DATABASE dsmp;
```

The dashboard expects a table named `flight` with columns such as `Airline`, `Date_of_Journey`, `Source`, `Destination`, `Route`, and `Price`.

To prepare the data, open `data_analysis_flight.ipynb` in Jupyter Notebook and run the data-cleaning cells. The notebook includes a step that writes the cleaned DataFrame to the MySQL `flight` table. Update the database connection settings to match your local MySQL configuration before running that step.

**Database setup note:** `dbhelper.py` currently connects to a local MySQL server and expects the `dsmp` database. Update its connection settings to your own local configuration before launching the dashboard.

### 5. Run the dashboard

```bash
streamlit run st.py
```

Streamlit will print a local URL (usually `http://localhost:8501`) that you can open in your browser.

## How to Use

1. Open the dashboard and choose a section from the sidebar.
2. In **Route & Traffic Analysis**, select a source and destination, then click **Search Flights**.
3. In **Price Analysis**, select an airline, source, and destination to view the price trend.
4. In **Analytics**, explore summary KPIs and charts for airline and city traffic.

## Dataset Notes

The CSV contains flight information including airline, journey date, source, destination, route, departure time, duration, stops, and price. The notebook performs initial data-quality checks and cleaning before exporting data to MySQL.

## Security

- **Do not commit database passwords, API keys, or other secrets to GitHub.** The original project files contain a hard-coded local MySQL password. Remove it from the source code and load credentials from environment variables before making the repository public.
- If a real password has already been pushed to a public repository, change/rotate that password.
- Use parameterized SQL queries for user-provided values. Review query construction before deploying this project beyond your local machine.

## Possible Improvements

- Move database credentials into environment variables or a `.env` file excluded from Git.
- Add clearer database connection error handling and close connections safely.
- Use parameterized queries consistently.
- Add filters for journey date, number of stops, and price range.
- Deploy the dashboard with a securely configured remote database.

## Author

**Raushan Kumar** — as credited in the current dashboard footer. Update this section if the repository owner or project attribution should be different.
