import time
from flask import Flask

app = Flask(__name__)  # Sửa lỗi __name__

@app.route('/time')  # Thêm dấu `/` ở trước đường dẫn
def get_current_time():
    return {'time': time.time()}  # Trả về JSON hợp lệ

if __name__ == '__main__':
    app.run(debug=True)  # Chạy Flask với chế độ debug
