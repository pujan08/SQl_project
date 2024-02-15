import pandas as pd
from sqlalchemy import create_engine

# Load the data
df = pd.read_csv('Superstore.csv')

# Data clean up (if needed)
df.columns = df.columns.str.strip()

# Define MySQL connection parameters
mysql_host = 'localhost'        # Hostname for the MySQL server
mysql_user = 'root'     # Replace with your MySQL username
mysql_password = 'Winter_2024' # Replace with your MySQL password
mysql_db = 'superstore'  # Replace with your MySQL database name

# Create SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}')

# Write DataFrame to MySQL
df.to_sql('mastertable', con=engine, if_exists='replace', index=False)

# Dispose of the engine
engine.dispose()
