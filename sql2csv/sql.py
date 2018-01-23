import pypyodbc
import contextlib

def to_connection_string_args(attributes, args_dict):
    return { attr: args_dict.get(attr) for attr in attributes if args_dict.get(attr) }

def execute_sql_from_file(filepath, **kwargs):
    with open(filepath, 'r', encoding='utf-8') as f:
        return execute_sql(f.read(), **kwargs)

@contextlib.contextmanager
def execute_sql(query, **kwargs):
    with _connect(**kwargs) as conn, conn.cursor() as cursor:
        yield _read_columns_and_rows(cursor.execute(query))

def _read_columns_and_rows(cursor):
    return (_read_columns(cursor), _read_rows(cursor))

def _read_columns(cursor):
    return [desc[0] for desc in cursor.description]

def _read_rows(cursor):
    while True:
        row = cursor.fetchone()

        if not row:
            break

        yield row

def _connect(**kwargs):
    return pypyodbc.connect(**kwargs)