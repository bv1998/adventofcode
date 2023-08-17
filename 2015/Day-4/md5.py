import hashlib
secret_key = "yzbqklnj"
target_prefix = "000000" #This is changed based o nthe amount of zeros
number = 0
while not hashlib.md5(f"{secret_key}{number}".encode()).hexdigest().startswith(target_prefix):
    number += 1
print(number)