from flask import Flask, jsonify
import mysql.connector
from flask import Flask
from flask_cors import CORS  # Import CORS


app = Flask(__name__)
CORS(app)  # Cho phép CORS cho tất cả các origin

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
@app.route("/")
def home():
    return "ItShops"

if __name__ == "__main__":
    app.run(debug=True)