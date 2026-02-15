# Data Profiling Report – Superstore Dataset

## Dataset Overview
- Total Rows: 9,994
- Total Columns: 21
- File Format: CSV
- Encoding: latin1 (handled during ingestion)

## Grain Analysis
Each row represents one order line item.
An order can contain multiple products, meaning the same Order ID can appear multiple times.

Grain:
One row per Order ID + Product ID

## Data Quality Assessment

- Missing Values: 0
- Duplicate Rows: 0
- Data appears structurally clean.

## Observations

1. Customer, product, and region attributes are stored in a single flat file.
2. Fact and dimension attributes are mixed.
3. Order Date and Ship Date require date dimension creation.
4. Numeric columns:
   - Sales
   - Quantity
   - Discount
   - Profit

These are candidate measures for the fact table.

## Modeling Implication

The dataset requires dimensional modeling (star schema) to:
- Improve analytical performance
- Separate descriptive and measurable data
- Enable scalable reporting
