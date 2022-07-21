from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
print(key.decode())
# Bq64GE−−93K1RVro4go1frN−8twBSvXdbCPSPLIKz9U=
encrypted_data = f.encrypt(b"This message is being encrypted and cannot be seen!")
print(encrypted_data)

# b'gAAAAABgILy91p_wqMntdT3mDkh0IBXSLjuBMQAfnGZAFkZCX1U6Q7TU2PthgFBwVz0QbKXpuNTHRzAgbdDV4zfuuzkGCXqVD--xJdkTycKH2iurC_oqHySLc9xJEXz93LkhTbKUa5HCxfJtB-Um_YkxqjclftXXZQ=='

decrypted_data = f.decrypt(encrypted_data) # f is the variable that has the value of the key.
print(decrypted_data)
# b'This message is being encrypted and cannot be seen!'
print(decrypted_data.decode())
# This message is being encrypted and cannot be seen!
