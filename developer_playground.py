import bcrypt

passwd = b'rajath'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)
passwd = b'rajath'

if bcrypt.checkpw(passwd, hashed):
    print("Match")
else:
    print("Doesn't Match")


print(passwd)
print(salt)
print(hashed)
