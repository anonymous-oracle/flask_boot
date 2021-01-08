import bcrypt
from flask_bcrypt import Bcrypt
from werkzeug.security import check_password_hash, generate_password_hash

# USING BCRYPT
bcrypt_ = Bcrypt()
password = 'supersecretpassword'

hashed_password = bcrypt_.generate_password_hash(password=password)
# print(hashed_password)

check = bcrypt_.check_password_hash(hashed_password, 'wrongpassword')
print(check)

check = bcrypt_.check_password_hash(hashed_password, 'supersecretpassword')
print(check)

# USING WERKZEUG
hashed_pass = generate_password_hash('mypassword')
print(hashed_pass)
check = check_password_hash(hashed_pass, 'wrong')
print(check)