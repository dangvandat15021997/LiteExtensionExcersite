import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

user = "dat"
host = "localhost"
password = "Lma05003624958!@#"
schema = "test_db"
port = 3306

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{schema}', echo=False)

conn = engine.raw_connection()

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS customer(customerid int NOT NULL PRIMARY KEY,
                firstname varchar(100),
                lastname varchar(100),
                companyname varchar(100),
                billingaddress1 varchar(100),
                billingaddress2 varchar(100),
                city varchar(100),
                state varchar(100),
                postalcode varchar(100),
                country varchar(100),
                phonenumber varchar(100),
                emailaddress varchar(100),
                createddate timestamp); """)



csv_file = pd.read_csv('./customer.csv')
csv_file.to_sql(con=engine, name='customer', if_exists='replace')

conn.close()