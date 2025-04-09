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
@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    if not data or 'product_id' not in data:
        return jsonify({"error": "Missing 'product_id' in request body"}), 400

    product_id = data['product_id']
    quantity = data.get('quantity', 1)

    con = get_db_connection()
    cursor = con.cursor()

    # Kiểm tra xem sản phẩm đã có trong giỏ hàng chưa
    check_query = "SELECT * FROM cart WHERE product_id = %s"
    cursor.execute(check_query, (product_id,))
    result = cursor.fetchone()

    if result:
        update_query = "UPDATE cart SET quantity = quantity + %s WHERE product_id = %s"
        cursor.execute(update_query, (quantity, product_id))
    else:
        insert_query = "INSERT INTO cart (product_id, quantity) VALUES (%s, %s)"
        cursor.execute(insert_query, (product_id, quantity))

    con.commit()
    cursor.close()
    con.close()

    return jsonify({"message": "Added to cart"}), 201

@app.route('/showcart', methods=['GET'])
def show_cart():
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)  # Trả về dictionary thay vì tuple
        sql = """           SELECT 
                cart.id,
                products.name,
                products.image,
                products.price,
                cart.quantity,
                cart.product_id
            FROM cart
            JOIN products ON cart.product_id = products.id
            """
        cursor.execute(sql)
        cart_items = cursor.fetchall()  # Lấy toàn bộ dữ liệu

        cursor.close()
        con.close()

        return jsonify({"carts": cart_items}), 200  # Trả về JSON

    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500
@app.route('/deletecart', methods=['DELETE'])
def delete_cart_item():
    data = request.get_json()
    if not data or 'product_id' not in data:
        return jsonify({"error": "Missing 'product_id' in request body"}), 400

    product_id = data['product_id']

    con = get_db_connection()
    cursor = con.cursor()

    # Xóa sản phẩm khỏi giỏ hàng
    delete_query = "DELETE FROM cart WHERE product_id = %s"
    cursor.execute(delete_query, (product_id,))

    con.commit()
    cursor.close()
    con.close()

    return jsonify({"message": "Deleted from cart"}), 200

if __name__ == "__main__":
    app.run(debug=True)
    