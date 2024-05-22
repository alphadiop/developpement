import os
import sys

import requests

from tabulate_dataframe import tabulate_dataframe


def utilisation_lambda():
    nums = [9, 4, 5, 6, 11]
    resultat_map = list(map(lambda num: num * num, nums))
    resultat_float = list(map(lambda num: float(3 * num), nums))
    resultat_filtre = list(filter(lambda num: num % 2 == 0, nums))
    print('\n')
    print(f"resultat_map : {resultat_map}")
    print(f"resultat_float : {resultat_float}")
    print(f"resultat_filtre : {resultat_filtre}")


def test_fonction():
    format = dict()
    json_schema = {"location":{"sql_type":"VARCHAR(100)","nullable":"NOT NULL"},"weather":{"sql_type":"VARCHAR(100)","nullable":"NOT NULL"}}
    schema = [(column.format(**format), info['sql_type'], info['nullable']) for column, info in json_schema.items()]
    columns = [tp[0] for tp in schema]
    columns_lambda = list(filter(lambda tp: tp[0] in columns,schema))
    schema_fil = list(filter(lambda tp: tp[0] in columns, schema))
    print(f" json_schema : {json_schema.items()}")
    print(f"schema  : {schema}")
    print(f"columns : {columns}")
    print(f"columns_lambda : {columns_lambda}")
    print(f"schema_fil : {schema_fil}")


def get_directory_file():
    print(f"path : {os.path.dirname(__file__)}")
    print(f"int_info : {sys.int_info}")


def get_data_from_web2():
    url = "https://databank.worldbank.org/data/download/WDI_CSV.zip"
    response = requests.get(url, stream=True)
    print(response)
def get_data_from_web():
    import requests
    download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
    target_csv_path = r"D:\data_figees\nba_all_elo.csv"

    response = requests.get(download_url)
    response.raise_for_status()  # Check that the request was successful
    with open(target_csv_path, "wb") as f:
        f.write(response.content)
    print("Download ready.")


def get_data():
    import pandas as pd
    path = r"D:\data_figees\nba_all_elo.csv"
    nba = pd.read_csv(path)
    print(f"nba : {tabulate_dataframe(nba.head())}")
    print()

def get_set():
    fruits = {"apple","banana","tomato"}
    verggis = {"egglant","tomato"}
    print(f"fruits  : {fruits}")
    print(f"verggis : {verggis}")
    print('\n')


    print(f"fruits^verggis : {fruits ^ verggis}")
    print(f"fruits-verggis : {fruits - verggis}")
    print('\n')
    print(f"union 2        : {fruits.union(verggis)}")
    print(f"fruits|verggis : {fruits | verggis}")
    print('\n')
    print(f"intersection       : {fruits.intersection(verggis)}")
    print(f"fruits & verggis   : {fruits & verggis}")
    print(f"intersection_update: {fruits.intersection_update(verggis)}")
    print('\n')
    print(f"symmetric_difference       : {fruits.symmetric_difference(verggis)}")
    print(f"symmetric_difference_update: {fruits.symmetric_difference_update(verggis)}")
    print('\n')
    print(f"update : {fruits.update(verggis)}")







if __name__ == "__main__":
    print('-'*121)
    get_data_from_web2()
    #get_data()
    #get_data_from_web()
    # get_set()
    # get_directory_file()
    # test_fonction()
    # utilisation_lambda()