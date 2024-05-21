# -*- coding: utf-8 -*-
import requests

def download_file(url):
    response = requests.get(url)
    if "content-disposition" in response.headers:
        content_disposition = response.headers["content-disposition"]
        filename = content_disposition.split("filename=")[1]
    else:
        filename = url.split("/")[-1]
    with open(filename, mode="wb") as file:
        file.write(response.content)
        print(f"Downloaded file {filename}")


def get_data_from_web2():
    url = "https://databank.worldbank.org/data/download/WDI_CSV.zip"
    response = requests.get(url, stream=True)
    print(f"response : {response}")
    with open("gdp_by_country.zip", mode="wb") as file:
        file.write(response.content)


def get_data():
    url = "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD"
    query_parameters = {"downloadformat": "csv"}
    response = requests.get(url, params=query_parameters)
    with open("gdp_by_country.zip", mode="wb") as file:
        file.write(response.content)



if __name__ == "__main__":
    print('-'*121)
    get_data_from_web2()