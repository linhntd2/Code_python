import sqlite3


class Database:
    def __init__(self, path_db):
        self.conn = sqlite3.connect(path_db)

    # =========== TRUY XUẤT DỮ LIỆU: SELECT
    # - Lấy danh sách
    def get_all(self, chuoi_sql, bieu_thuc_dieu_kien=()):
        cursor = self.conn.execute(chuoi_sql, bieu_thuc_dieu_kien)
        danh_sach = cursor.fetchall()
        return danh_sach

    # - Lấy 1
    def get_one(self, chuoi_sql, bieu_thuc_dieu_kien=()):
        cursor = self.conn.execute(chuoi_sql, bieu_thuc_dieu_kien)
        doi_tuong = cursor.fetchone()
        return doi_tuong


    # =========== THỰC THI: INSERT, UPDATE, DELETE
    def execute(self, chuoi_sql, bieu_thuc_dieu_kien=()):
        cursor = self.conn.execute(chuoi_sql, bieu_thuc_dieu_kien)
        self.conn.commit()
        return cursor.rowcount

    def disconnect(self):
        self.conn.close()
