import os
import sys

import connexion


# Placeholder for nlp var initialized in server module.
nlp = None

drive_letter = os.path.splitdrive(sys.executable)[0]
if drive_letter:
    drive_letter += '\\'
else:
    drive_letter = r'/'
models_dir = os.path.join(drive_letter, 'data', 'language_models')

basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app.add_api("rest_api.yml")

