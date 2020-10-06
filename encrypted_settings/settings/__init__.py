import os
import json
from encrypted_settings.encrypted_file import get_decrypted_file, random_key


def load_settings(settings_key, settings_file):
    settings = json.loads(get_decrypted_file(settings_key, settings_file))
    for s in settings:
        globals()[s] = settings[s]


if not os.environ.get('SETTINGS_KEY'):
    print(f'No SETTINGS_KEY set in Environment for secure settings\n'
          f'A new project can use this random key: SETTINGS_KEY={random_key()}')
else:
    load_settings(os.environ['SETTINGS_KEY'], os.environ['DJANGO_SECURE_SETTINGS'])
