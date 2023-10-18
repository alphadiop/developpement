import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os
from path import Path

def generate_csv_file(data,path,file_name):
    return data.to_csv(os.path.join(path,'{0}.csv'.format(file_name)), sep=',', encoding='utf-8',index=False)


if __name__=="__main__":
    # path = Path(os.path.dirname(__file__)).parent
    # file_name = 'variable_environnement'
    # data = pd.read_json('variable_environnement.json')
    # generate_csv_file(data, path, file_name)
    # print(f"path : {path}")
    #print(data.head(30))
    import pyodbc
    server = [x for x in pyodbc.drivers()]
    print(f"server : {server}")




#df.to_csv("../variable_environnement.csv", sep=',', encoding='utf-8',index=False)

