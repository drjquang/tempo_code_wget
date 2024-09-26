import pyodbc


def read_latest_record():
    # Define connection parameters
    server = '192.168.1.10'  # Replace with your server name or IP address
    database = 'master'  # Replace with your database name
    username = 'sa'
    password = 'abc12345'

    # Create a connection string
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};" \
                        f"SERVER={server};" \
                        f"DATABASE={database};" \
                        f"UID={username};" \
                        f"PWD={password};" \
                        f"Trusted_Connection=yes;"

    # Establish the connection
    conn = pyodbc.connect(connection_string)

    # Create a cursor object
    cursor = conn.cursor()
    # MAIN QUERY JOB -------------------------------------------------------------------------------------------------------
    # Define the data to be inserted
    table_name = 'gameplay.record'  # You can customize the table name
    order_column = "id"

    # Read the latest record
    select_query = f"""
        SELECT TOP 1 * FROM {table_name} ORDER BY {order_column} DESC
    """

    # Execute the query and fetch the new ID
    cursor.execute(select_query)
    row = cursor.fetchone()  # data type = <class 'pyodbc.Row'>
    data_list = list(row) if row is not None else None
    # print(data_list)

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

    return data_list


# Run test the function
if __name__ == "__main__":
    latest_record = read_latest_record()
    print(latest_record)
