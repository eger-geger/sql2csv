import os
import sys
import csv
from .sql import *

def sql2csv(args):
    if not 'query_file_path' in args:
        raise ValueError('Query file path missing')

    if not os.path.isfile(args.query_file_path):
        raise ValueError('Invalid query file path')

    conn_args = to_connection_string_args(
        ['driver', 'database', 'uid', 'pwd', 'server', 'trusted_connection', 'app'], vars(args)
    )

    with execute_sql_from_file(args.query_file_path, **conn_args) as (cols, rows):
        if args.output:
            write_csv(args.output, cols, rows)
        else:
            print_rows(cols, rows)

def write_csv(filepath, columns, rows):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)

def print_rows(columns, rows):
    for row in rows:
        print(dict(zip(columns, row)))