
import time
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os


app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Đặt bí mật thật an toàn
jwt = JWTManager(app)

# Cấu hình cơ sở dữ liệu
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{os.getenv('MYSQL_USER', 'root')}:"
    f"{os.getenv('MYSQL_PASSWORD', '2002')}@"
    f"{os.getenv('MYSQL_HOST', 'localhost')}/"
    f"{os.getenv('MYSQL_DATABASE', 'itshopsdata')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image = db.Column(db.String(255))
    details = db.Column(db.Text)
    price = db.Column(db.Float)

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quantity = db.Column(db.Integer)
    product = db.relationship('Product')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    full_name = db.Column(db.String(255))

# Hàm convert object -> dict
def product_to_dict(product):
    return {
        "id": product.id,
        "name": product.name,
        "image": product.image,
        "details": product.details,
        "price": product.price
    }

# Route
@app.route("/")
def home():
    return "ItShops"

@app.route("/time")
def get_current_time():
    return {"time": time.time()}

@app.route('/getproducts', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify({"products": [product_to_dict(p) for p in products]}), 200

@app.route('/getproducts/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({"product": product_to_dict(product)}), 200
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Thiếu tham số 'query'"}), 400
    results = Product.query.filter(Product.name.like(f"%{query}%")).all()
    return jsonify({"products": [product_to_dict(p) for p in results]}), 200

@app.route('/cart', methods=['POST'])
@jwt_required()
def add_to_cart():
    try:
        user_id = int(get_jwt_identity())

        data = request.get_json()
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        if not product_id:
            return jsonify({"error": "Thiếu 'product_id'"}), 400

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            return jsonify({"error": "'quantity' phải là số nguyên"}), 400

        cart_item = Cart.query.filter_by(product_id=product_id, user_id=user_id).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            new_item = Cart(product_id=product_id, quantity=quantity, user_id=user_id)
            db.session.add(new_item)

        db.session.commit()
        return jsonify({"message": "Đã thêm vào giỏ hàng"}), 201

    except Exception as e:
        print("LỖI GIỎ HÀNG:", e)
        return jsonify({"error": "Lỗi server", "message": str(e)}), 500




@app.route('/showcart', methods=['GET'])
@jwt_required()
def show_cart():
    user_id = get_jwt_identity()

    carts = Cart.query.filter_by(user_id=user_id).all()
    result = []
    for item in carts:
        result.append({
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "name": item.product.name,
            "image": item.product.image,
            "price": item.product.price
        })
    return jsonify({"carts": result}), 200



@app.route('/deletecart', methods=['DELETE'])
def delete_cart_item():
    data = request.get_json()
    product_id = data.get('product_id')

    if not product_id:
        return jsonify({"error": "Thiếu 'product_id'"}), 400

    item = Cart.query.filter_by(product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Deleted from cart"}), 200
    else:
        return jsonify({"error": "Không tìm thấy sản phẩm trong giỏ hàng"}), 404

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    full_name = data.get('full_name')

    if not username or not password:
        return jsonify({"error": "Thiếu 'username' hoặc 'password'"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Người dùng đã tồn tại"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, email=email, full_name=full_name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "Tạo người dùng thành công",
        "user": {
            "username": username,
            "email": email,
            "full_name": full_name
        }
    }), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Thiếu 'username' hoặc 'password'"}), 400

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        # Chỉ truyền user.id làm identity
        access_token = create_access_token(identity=str(user.id))  # ép kiểu thành string


        return jsonify({
            "message": "Đăng nhập thành công",
            "access_token": access_token,
            "user": {
                "username": user.username,
                "email": user.email,
                "full_name": user.full_name
            }
        }), 200
    else:
        return jsonify({"error": "Tên người dùng hoặc mật khẩu không đúng"}), 401


# Tạo bảng nếu chưa có (chạy 1 lần đầu tiên)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
