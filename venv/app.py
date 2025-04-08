import time
from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS # thêm vào thư viện CORS


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

# if __name__ == "__main__":
#     app.run(debug=True)
    
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

# if __name__ == '__main__':
#    app.run(debug=True, port=5000)
@app.route("/")
def home():
    return "ItShops"

# if __name__ == "__main__":
#     app.run(debug=True)
# Lay sanr pham
@app.route('/cart', methods=['POST','GET'])
def add_to_cart():
    # return jsonify({"message": "Cart API"}), 200

        data = request.get_json()  # Lấy dữ liệu JSON từ request body
        if not data or 'product_id' not in data:
            return jsonify({"error": "Missing 'product_id' in request body"}), 400

        product_id = data['product_id']
        quantity = data.get('quantity', 1)

        # Giả sử bạn đã có hàm get_db_connection()
        con = get_db_connection()
        cursor = con.cursor()

        insert_query = "INSERT INTO cart (product_id, quantity) VALUES (%s, %s)"
        cursor.execute(insert_query, (product_id, quantity))
        con.commit()

        cursor.close()
        con.close()

        return jsonify({"message": "Added to cart"}), 201

if __name__ == "__main__":
    app.run(debug=True)
    