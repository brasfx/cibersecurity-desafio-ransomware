import os
import pyaes

file_name = 'teste.txt.ransomwaretroll'

# open and read file
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# define decrypt key
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# deccrypt file
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = 'new_teste.txt'

# save decrypt file
new_file = open(f'{new_file}', 'wb')

new_file.write(decrypt_data)

new_file.close()
