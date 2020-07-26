# TEAL_webapp


## Installation and Setup:

Python:
```
python >= 3.7
django >  3.0
# For Azure SQL Server connection:
pyodbc >= 3.0
django-mssql-backend >= 2.8.1
```

Update: these have been moved into requirements.txt for prod, they can be installed with `pip`

On top of this, pyodbc requires `Microsoft ODBC Driver for SQL Server` to be installed, see [here](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15) for installation instructions.


