import os
import sys
import yaml

import connexion


# Placeholder for nlp var initialized in server module.
nlp = None

basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=basedir)

# TODO leave this hardcoded for now
env = 'dev'

settings_file = os.path.join(basedir, 'settings.yml')

yml = {}
with open(settings_file) as f:
    yml = yaml.safe_load(f)[env]

port = yml['port']

drive_letter = os.path.splitdrive(sys.executable)[0]
if drive_letter:
    drive_letter += '\\'
else:
    drive_letter = r'/'
models_dir = os.path.join(drive_letter, 'data', 'language_models')

connex_app.add_api("rest_api.yml")

