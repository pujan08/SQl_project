from sqlalchemy import create_engine, inspect

# Define MySQL connection parameters
mysql_host = 'localhost'        # Hostname for the MySQL server
mysql_user = 'root'              # Replace with your MySQL username
mysql_password = 'Winter_2024'   # Replace with your MySQL password
mysql_db = 'superstore'          # Replace with your MySQL database name

# Create SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}')

# Connect to the MySQL database
connection = engine.connect()

# Get the database name
print(f"Database Name: {mysql_db}")

# Use SQLAlchemy inspect to get table names
inspector = inspect(engine)
table_names = inspector.get_table_names()
print("Table Names:")
for table_name in table_names:
    print(f"Table: {table_name}")
    print("Columns:")
    for column in inspector.get_columns(table_name):
        print(f"Name: {column['name']}, Type: {column['type']}")
    print("\n")

# Close the connection
connection.close()
