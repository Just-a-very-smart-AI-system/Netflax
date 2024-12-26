import pymysql

def connect_to_db():
    try:
        # print("Bắt đầu kiểm tra kết nối MySQL.")
        connection = pymysql.connect(
            host="localhost",
            user="root", 
            password="Htctran12#",
            database="netflax"
        )
        if connection:
            print("Kết nối thành công.")
            return connection
        else:
            print("Khong thanh cong")
    except pymysql.MySQLError as e:
        print(f"Lỗi khi kết nối MySQL: {e}")
    except Exception as ex:
        print(f"Lỗi không xác định: {ex}")
