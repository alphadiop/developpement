
pip show module sqlalchemy : obtenir la version


from sqlalchemy import text
query = text("SELECT * FROM some_table WHERE column1 > 1")

sinon
python3 -m pip install --upgrade 'sqlalchemy<2.0'