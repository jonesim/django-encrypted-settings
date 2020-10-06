from os import path
from cryptography.fernet import Fernet


def get_decrypted_file(settings_key, settings_file, encrypted_extension='enc', initial_extension='json'):
    encryption = Fernet(settings_key)

    encrypted_file_name = f'{settings_file}.{encrypted_extension}'
    encrypted_data = None
    if path.isfile(encrypted_file_name):
        with open(encrypted_file_name, 'rb') as f:
            encrypted_data = encryption.decrypt(f.read())

    raw_file_name = f'{settings_file}.{initial_extension}'
    initial_data = None
    if path.isfile(raw_file_name):
        with open(raw_file_name, 'rb') as f:
            initial_data = f.read()

    if not initial_data:
        return encrypted_data
    elif initial_data != encrypted_data:
        encrypted_data = encryption.encrypt(initial_data)
        with open(encrypted_file_name, 'wb') as f:
            f.write(encrypted_data)
    return initial_data


def random_key():
    return Fernet.generate_key().decode("utf-8")
