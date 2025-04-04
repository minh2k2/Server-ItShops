import time
from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS 

app = Flask(__name__)
CORS (app)



# Hàm kết nối MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2002",
        database="itshopsdata"
    )

@app.route('/getproducts', methods=['GET'])
def get_products():
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)  # Trả về dictionary thay vì tuple
        sql = "SELECT * FROM products;"
        cursor.execute(sql)
        products = cursor.fetchall()  # Lấy toàn bộ dữ liệu

        cursor.close()
        con.close()

        return jsonify({"products": products}), 200  # Trả về JSON

    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
   app.run(debug=True, port=5000)
@app.route("/")
def home():
    return "ItShops"

if __name__ == "__main__":
    app.run(debug=True)
# Lay sanr pham
@app.route('/card', methods=['GET'])

def get_card():
    con= get_db_connection()
    coursor= con.cursor(dictionary=True)
    update="""
        SELECT cart.id, products.name, products.image, cart.quantity, products.price
        FROM cart
        JOIN products ON cart.product_id = products.id
    """
    carditem=coursor.fetchall()
    coursor.execute(update)
    coursor.close()
    return jsonify({"card":carditem})
