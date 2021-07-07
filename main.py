from flask import Flask, render_template, request,abort,redirect,url_for
import psycopg2
from psycopg2 import Error

app = Flask(__name__)

try:
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="lenson")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE stocks
          (ID INT PRIMARY KEY,
          item_name VARCHAR ( 100 ),
          item_supplier VARCHAR ( 100 ),
          item_quantity INT); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

    # Executing a SQL query to insert data into  table
    insert_query = """ INSERT INTO stocks (id, item_name, item_supplier, item_quantity) VALUES (1, 'Sunlight','Naivas', 100)"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 Record inserted successfully")
    # Fetch result
    cursor.execute("SELECT * from stocks`")
    record = cursor.fetchall()
    print("Result ", record)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


@app.route('/', methods=['GET', 'POST'])
def stocks():
    stock_item="sunlight"
    typeofitem="soap"
    listofitems=['bag','chair','laptop','table','dustbin','projecter','tv','book','movie']
    stockage=18
    list1=[{
    "firstname":"Lenson",
    "secondname":"N",
    "lastname":"Obuba",
    "Age":"22",
    "Gender":"M"
    }]
 
    # stock_item = "Sunlight"
    # type_of_item = "Soap"

    list_of_items = ['Sunlight', 'Harpic', 'Cadburys', 'Ketepa','Books', 'Bags', 'Curtains','Chairs', 'Projectors', 'Denim', 'WhiteChairs']

    stock_age = 17

    return render_template('index.html', list_of_items = list_of_items, stock_age = stock_age )


@app.route('/inheritance')
def inheritance():
    return render_template('inheritance.html')

@app.route('/requests', methods=['GET','POST'])
def requests():
    if request.method == 'POST':        
        item_name = request.form['item_name']
        item_supplier = request.form['item_supplier']
        item_quantity = request.form['item_quantity']
        print(item_name, item_supplier, item_quantity)

        return redirect(url_for('inheritance'))

    return render_template('requests.html')