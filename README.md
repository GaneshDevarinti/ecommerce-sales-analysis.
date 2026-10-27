# E-Commerce Sales Analysis Using Python and SQL

## Project Overview
This project analyzes e-commerce sales data using Python, Pandas, SQL, and SQLite. It combines customer and order data to identify customer spending, product revenue, and sales performance by city.

## Technologies Used
- Python
- Pandas
- SQL
- SQLite
- VS Code

## Project Structure
```text
ecommerce-sales-analysis/
├── customers.csv
├── orders.csv
├── main.py
├── ecommerce.db
└── README.md
```

## Workflow
1. Extract customer and order data from CSV files using Pandas.
2. Remove duplicate customer IDs and order IDs.
3. Load the data into SQLite database tables.
4. Join customer and order tables using SQL.
5. Calculate customer spending and total store revenue.
6. Analyze product revenue, order counts, and city-wise sales.

## Key SQL Concepts
- SELECT and WHERE
- JOIN
- GROUP BY
- Aggregate functions: SUM and COUNT
- ORDER BY

## How to Run
1. Install Python.
2. Install Pandas:
   `python -m pip install pandas`
3. Run the project:
   `python main.py`

The program creates `ecommerce.db` automatically and prints the analysis results in the terminal.

## Sample Dataset
The project uses sample customer and order records stored in CSV files.

## Learning Outcomes
- Reading CSV files with Python.
- Loading data into a relational database.
- Writing SQL JOIN and aggregation queries.
- Calculating revenue from order quantities and prices.
- Performing basic sales data analysis.

## Limitations
This project uses a small sample dataset and SQLite. It is a learning project and has not been deployed as a production data pipeline.