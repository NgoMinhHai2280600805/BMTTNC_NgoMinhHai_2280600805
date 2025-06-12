import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()  # Tạo đối tượng hash SHA-256
    sha256_hash.update(data.encode('utf-8'))  # Mã hóa dữ liệu thành bytes và cập nhật
    return sha256_hash.hexdigest()  # Trả về chuỗi hex

data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)
print("Giá trị hash SHA-256:", hash_value)
