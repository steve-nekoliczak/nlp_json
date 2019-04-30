import os

import connexion

# Placeholder for nlp var initialized in server module.
nlp = None

basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app.add_api("rest_api.yml")
