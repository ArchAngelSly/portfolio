import pandas as pd
import pyodbc

def download_table(server, database, table_name, username, password, output_file):
# Load data from SQL Server
 
    conn_str = (
        "Data Source Name=D1;"  # Specify the driver for SQL Server
        "Driver={SQL Server};"  # Specify the driver for SQL Server
        "Server=localhost\\SQLEXPRESS;"  # Specify your SQL Server instance
        "Database=PortfolioProject_MarketingAnalytics;"  # Specify the database name
        "Trusted_Connection=yes;"  # Use Windows Authentication for the connection
    )

 
    # Establishing the connection
    conn = pyodbc.connect(conn_str)

    # Query to select the table
    query = f'SELECT * FROM {table_name}'  
    
    # Reading the table into a DataFrame
    df = pd.read_sql(query, conn)
    
    # Saving the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    
    # Closing the connection
    conn.close()
    print(f'Table {table_name} downloaded successfully to {output_file}')  # Corrected file path handling

# Example usage
download_table('localhost\\SQLEXPRESS', 'PortfolioProject_MarketingAnalytics', 'dbo.customer_journey', 'PC', 'SlyPC2024', 'C:/Users/PC/Dropbox/Data Science/Data Science/Marketing Analysis Portfolio Project/Marketing_Analytics_Customer_Journey.csv')
download_table('localhost\\SQLEXPRESS', 'PortfolioProject_MarketingAnalytics', 'dbo.customers', 'PC', 'SlyPC2024', 'C:/Users/PC/Dropbox/Data Science/Data Science/Marketing Analysis Portfolio Project/Marketing_Analytics_Customers.csv')
download_table('localhost\\SQLEXPRESS', 'PortfolioProject_MarketingAnalytics', 'dbo.products', 'PC', 'SlyPC2024', 'C:/Users/PC/Dropbox/Data Science/Data Science/Marketing Analysis Portfolio Project/Marketing_Analytics_Products.csv')
download_table('localhost\\SQLEXPRESS', 'PortfolioProject_MarketingAnalytics', 'dbo.customer_reviews', 'PC', 'SlyPC2024', 'C:/Users/PC/Dropbox/Data Science/Data Science/Marketing Analysis Portfolio Project/Marketing_Analytics_Customer_Reviews.csv')
download_table('localhost\\SQLEXPRESS', 'PortfolioProject_MarketingAnalytics', 'dbo.engagement_data', 'PC', 'SlyPC2024', 'C:/Users/PC/Dropbox/Data Science/Data Science/Marketing Analysis Portfolio Project/Marketing_Analytics.Engagement_Data.csv')
download_table('localhost\\SQLEXPRESS', 'PortfolioProject_MarketingAnalytics', 'dbo.geography', 'PC', 'SlyPC2024', 'C:/Users/PC/Dropbox/Data Science/Data Science/Marketing Analysis Portfolio Project/Marketing_Analytics_Geography.csv')
