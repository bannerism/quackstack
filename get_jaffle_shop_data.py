import pandas as pd


raw_customers = pd.read_csv('https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_customers.csv',index_col = 0)
raw_items = pd.read_csv('https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_items.csv', index_col = 0)
raw_orders = pd.read_csv('https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_orders.csv', index_col = 0)
raw_products = pd.read_csv('https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_products.csv', index_col = 0)
raw_stores = pd.read_csv('https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_stores.csv', index_col = 0)
raw_supplies = pd.read_csv('https://raw.githubusercontent.com/dbt-labs/jaffle-shop-data/refs/heads/main/jaffle-data/raw_supplies.csv', index_col = 0)

raw_customers.to_csv('/workspaces/quackstack/data/raw_customers.csv')
raw_items.to_csv('/workspaces/quackstack/data/raw_items.csv')
raw_orders.to_csv('/workspaces/quackstack/data/raw_orders.csv')
raw_products.to_csv('/workspaces/quackstack/data/raw_products.csv')
raw_stores.to_csv('/workspaces/quackstack/data/raw_stores.csv')
raw_supplies.to_csv('/workspaces/quackstack/data/raw_supplies.csv')
