import pandas as pd

file_path = "../data/raw/Superstore.csv"
df = pd.read_csv(file_path, encoding = 'latin1')

print(len(df))
print('-' * 65)

#---------------------------------------------------------------------------------

#create dim_customer Table

dim_customer = df[[
    "Customer ID",
    "Customer Name",
    "Segment"
]].drop_duplicates().reset_index(drop=True)

#create surrogate key

dim_customer["customer_key"] = dim_customer.index + 1

#Reorder columns

dim_customer = dim_customer[[
    "customer_key",
    "Customer ID",
    "Customer Name",
    "Segment"
]]

print(f"Unique Customer_data: {len(dim_customer)}")
print('-' * 65)

#---------------------------------------------------------------------------------

# Create dim_product
dim_product = df[[
    "Product ID",
    "Product Name",
    "Category",
    "Sub-Category"
]].drop_duplicates().reset_index(drop=True)

#product surrogate key

dim_product["product_key"] = dim_product.index + 1

dim_product = dim_product[[
    "product_key",
    "Product ID",
    "Product Name",
    "Category",
    "Sub-Category"
]]

print(f"Unique product_data: {len(dim_product)}")
print('-' * 65)

#---------------------------------------------------------------------------------
# create dim_region
dim_region = df[[
    "Region",
    "Country",    
    "State",
    "City",
    "Postal Code"
    
]].drop_duplicates().reset_index(drop = True)

#region surrogate key
dim_region["region_key"] = dim_region.index + 1

dim_region = dim_region[[
    "region_key",
    "Region",
    "Country",    
    "State",
    "City",
    "Postal Code"
]]

print(f"Unique regions: {len(dim_region)}")
print('-' * 65)



