
import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 1. Extract data from CSV files
customers = pd.read_csv(BASE_DIR / "customers.csv")
orders = pd.read_csv(BASE_DIR / "orders.csv")

# 2. Basic data cleaning
customers = customers.drop_duplicates(
    subset=["customer_id"]
)
orders = orders.drop_duplicates(
    subset=["order_id"]
)

# 3. Load the data into SQLite
db_path = BASE_DIR / "ecommerce.db"

with sqlite3.connect(db_path) as conn:
    customers.to_sql(
        "customers", conn, if_exists="replace", index=False
    )
    orders.to_sql(
        "orders", conn, if_exists="replace", index=False
    )

    # 4. Analyze total revenue by customer
    query = """
    SELECT
        c.customer_name,
        c.city,
        SUM(o.quantity * o.price) AS total_spent
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name, c.city
    ORDER BY total_spent DESC;
    """

    result = pd.read_sql_query(query, conn)

    print("\nCustomer Sales Analysis:")
    print(result.to_string(index=False))

    # 5. Calculate total store revenue
    revenue_query = """
    SELECT SUM(quantity * price) AS total_revenue
    FROM orders;
    """

    revenue = pd.read_sql_query(revenue_query, conn)

    print("\nTotal Store Revenue:")
    print(revenue.to_string(index=False))