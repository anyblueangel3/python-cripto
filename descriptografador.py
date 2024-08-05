import os
import pyaes

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.ransomwaretroll"

# Verificar se o arquivo criptografado existe
if os.path.exists(encrypted_file_name):
    # Abrir o arquivo criptografado
    with open(encrypted_file_name, "rb") as file:
        encrypted_data = file.read()

    # Chave de descriptografia (mesma usada para criptografar)
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar o arquivo
    decrypted_data = aes.decrypt(encrypted_data)

    # Salvar o arquivo descriptografado
    original_file_name = "teste.txt"
    with open(original_file_name, 'wb') as new_file:
        new_file.write(decrypted_data)

    # Remover o arquivo criptografado
    os.remove(encrypted_file_name)

    print(f"O arquivo {original_file_name} foi descriptografado e o arquivo criptografado foi removido com sucesso.")
else:
    print(f"Arquivo {encrypted_file_name} não encontrado.")