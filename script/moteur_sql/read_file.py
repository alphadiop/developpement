path = r"D:\data_figees\weather.csv"
with open(path, "r", encoding='utf-8-sig') as f:
    data = f.read()
    f.close()
    print(f"string : {data}")