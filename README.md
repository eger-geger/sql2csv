# sql2csv
Command-line tool which executes SQL SELECT query and saves result as CSV.

# Usage
```
usage: sql2csv [-h] [-o OUTPUT] -s SERVER [--driver DRIVER]
               [--database DATABASE] [-u UID] [-p PWD] [-t]
               query_file_path

executes SQL SELECT query and stores result to CSV file

positional arguments:
  query_file_path       file containing SQL SELECT query

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to output CSV file (default: None)

DB Connection:
  Properties for database connection string.

  -s SERVER, --server SERVER
                        DB server host name or IP address. (default: None)
  --driver DRIVER       SQL Server OBDC driver name. (default: {SQL Server})
  --database DATABASE   Database name. (default: None)
  -u UID, --uid UID     Connection username. (default: None)
  -p PWD, --pwd PWD     Connection user password. (default: None)
  -t, --trusted-connection
                        Connect without providing username and password
                        (default: None)
```

# Installation
```
git clone https://github.com/eger-geger/sql2csv.git
cd sql2csv
pip install .
```
