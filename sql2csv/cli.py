import argparse

def parse(args=None):
    return _parser().parse_args(args)

def _parser():
    parser = argparse.ArgumentParser(
        'sql2csv', 
        description='executes SQL SELECT query and stores result to CSV file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('query_file_path', help='file containing SQL SELECT query')
    parser.add_argument('-o', '--output', help='path to output CSV file')

    dbconn = parser.add_argument_group('DB Connection', 'Properties for database connection string.');
    dbconn.add_argument('-s', '--server', help='DB server host name or IP address.', required=True)
    dbconn.add_argument('--driver', help='SQL Server OBDC driver name.', default='{SQL Server}')
    dbconn.add_argument('--database', help='Database name.')
    dbconn.add_argument('-u', '--uid', help='Connection username.')
    dbconn.add_argument('-p', '--pwd', help='Connection user password.')
    dbconn.add_argument('-t', '--trusted-connection', action='store_const', const='yes', help='Connect without providing username and password')

    return parser