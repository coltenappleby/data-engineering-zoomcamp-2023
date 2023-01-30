import pandas as pd
import pyarrow.parquet as pq
import argparse
from sqlalchemy import create_engine
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database_name = params.database_name
    table_name = params.table_name
    file_location = params.file_location


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database_name}')

    engine.connect()

    # If getting the file from the internet
    parquet_name = 'output.parquet'
    # os.system(f'wget {url} -O {parquet_name}')

    df = pd.read_parquet(f'{file_location}',
                            engine='pyarrow') 

    df.to_sql(
            name=f'{table_name}',
            con=engine,
            if_exists='replace',
            chunksize=150000
        )

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Injest Parquet data to Postgres')

    # user
    # password
    # host
    # port
    # database
    # table name
    # url of the parquet file

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--database_name', help='database_name for postgres')
    parser.add_argument('--table_name', help='table name for postgres')
    parser.add_argument('--file_location', help='url for parquet file')

    args = parser.parse_args()

    main(args)



