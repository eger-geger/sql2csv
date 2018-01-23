import sys
from sql2csv import cli, sql2csv

def main():
    sql2csv(cli.parse())

if __name__ == '__main__':
    main()