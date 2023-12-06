import os
from env import get_db_url
import pandas as pd
    
def acquire_data():
    '''
    This function acquires data from the 'telco_churn' codeup MySQL database, joining tables: customers, contract_types, internet_service_types, & payment_types.

    It checks if a local CSV file ('telco.csv') exists. If the file exists, it reads the data from the file into a DataFrame.
    If the file does not exist, it queries the MySQL database using the specified SQL query, saves the result to the CSV file, and returns the DataFrame.

    Returns: 
    pd.DataFrame: DataFrame containing the acquired data.
    '''
    # Filename for the local CSV file
    filename = 'telco.csv'

    # URL for connecting to the MySQL database
    url = get_db_url('telco_churn')

    # SQL query to join tables in the 'telco_churn' database
    query = '''
        SELECT * FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN payment_types USING (payment_type_id);
    '''

    # Check if the local CSV file exists
    if os.path.exists(filename):
        # Read data from the existing file into a DataFrame
        df = pd.read_csv(filename, index_col=0)
    else:
        # Query the MySQL database if the file does not exist, save to CSV, and read into a DataFrame
        df = pd.read_sql(query, url)
        df.to_csv(filename)
    
    return df
