from setuptools import setup

setup(
    name='sql2csv',
    version='1.0.0',
    description='Command-line tool executing SQL and saving result as CSV',
    url='https://github.com/eger-geger/sql2csv',
    author='Ivan Mihaylovskyy',
    author_email='ivan.mihaylovskyy@gmail.com',
    packages=['sql2csv'],
    install_requires=[
        'pypyodbc',
    ],
    entry_points = {
        'console_scripts': ['sql2csv=sql2csv.__main__:main'],
    },
    zip_safe=False
)