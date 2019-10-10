import argparse
import re

from config import models_dir, port

def get_args():
    ap = argparse.ArgumentParser('Process human language sentences into JSON.')

    # Add args
    ap.add_argument('-d', '--debug',
                    action='store_true',
                    help="Enable debugging mode.")
    lang_code_link = \
        "https://stanfordnlp.github.io/stanfordnlp/installation_download.html"
    ap.add_argument('-l', '--lang', type=str,
                    help="StanfordNLP language code. Check\n" + lang_code_link,
                    default='de')
    ap.add_argument('-m', '--models_dir', type=str,
                    help="Directory for language modules.`",
                    default=models_dir)
    ap.add_argument('-p', '--port', type=int,
                    help="Port number to run this service on.",
                    default=port)

    a = ap.parse_args()

    # Sanitize arg inputs
    a.lang = re.sub('[^a-zA-Z]', '', a.lang).lower()

    return a

