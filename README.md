# Retail Sales ETL Pipeline (Stage 1)

## Business Problem

A retail company receives daily sales data in CSV format.
The data contains customer, product, and transaction information in a single flat file.

The objective is to:

- Clean and transform the data
- Design a star schema data model
- Load structured data into SQL Server
- Enable analytical reporting using Power BI
- Implement logging and incremental load logic

This project simulates a production-grade ETL pipeline.

## Data Modeling Approach

The grain of the fact table is one row per order line item.

Fact Table:
- fact_sales
    - order_id
    - product_id
    - customer_id
    - order_date_key
    - sales
    - quantity
    - discount
    - profit

Dimension Tables:
- dim_customer
- dim_product
- dim_region
- dim_date

A star schema design was chosen to optimize analytical query performance.

