import pandas as pd
from ydata_profiling import ProfileReport

# File paths and function
df_engagement_data = pd.read_csv(r'C:\Users\PC\Dropbox\Data Science\Data Science\Marketing Analysis Portfolio Project\Marketing_Analytics_Engagement_Data.csv')
df_customers = pd.read_csv(r'C:\Users\PC\Dropbox\Data Science\Data Science\Marketing Analysis Portfolio Project\Marketing_Analytics_Customers.csv')
df_customer_journey = pd.read_csv(r'C:\Users\PC\Dropbox\Data Science\Data Science\Marketing Analysis Portfolio Project\Marketing_Analytics_Customer_Journey.csv')
df_customer_reviews = pd.read_csv(r'C:\Users\PC\Dropbox\Data Science\Data Science\Marketing Analysis Portfolio Project\Marketing_Analytics_Customer_Reviews.csv')
df_geography = pd.read_csv(r'C:\Users\PC\Dropbox\Data Science\Data Science\Marketing Analysis Portfolio Project\Marketing_Analytics_Geography.csv')
df_products = pd.read_csv(r'C:\Users\PC\Dropbox\Data Science\Data Science\Marketing Analysis Portfolio Project\Marketing_Analytics_Products.csv')
df_sentiments = pd.read_csv(r'C:\Users\PC\Dropbox\Data Science\Data Science\Marketing Analysis Portfolio Project\fact_customer_reviews_with_sentiments.csv')

# Combine the dataframes if needed (optional)
df = pd.concat([df_engagement_data, df_customer_journey, df_customers, df_customer_reviews, df_products, df_sentiments, df_geography], axis=0)

# Generate the profiling report
profile = ProfileReport(df, title="ArchAngel Sports Marketing Analysis Pandas Profiling Report")
profile.to_file("C:\\Users\\PC\\Dropbox\\Data Science\\Data Science\\Marketing Analysis Portfolio Project\\profiling_report.pdf")
