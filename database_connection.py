from sqlalchemy import create_engine, text
from sqlalchemy.sql import select

engine = create_engine("mssql+pyodbc://sa:Passw0rd@localhost:1433/TRADAPP?driver=ODBC+Driver+17+for+SQL+Server")


def login_validate(uname, pword):
    with engine.connect() as conn:
        sql = "select count(user_id) from TRADAPP.dbo.[user] where user_name ='"+uname+"' and password='"+pword+"'"
        result = conn.execute(text(sql))
        for row in result.all():
            id_count = row[0]
    if id_count > 0:
        page = 'home.html'
    else:
        page = 'login.html'
    return page


def save_stock_details(farmer_details, stock_data):
    print(farmer_details['farmer_name'])
    print(stock_data)


