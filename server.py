import argparse
import re

import stanfordnlp

import config


def get_args():
    ap = argparse.ArgumentParser('Process human language sentences into JSON.')

    # Add args
    lang_code_link = \
        "https://stanfordnlp.github.io/stanfordnlp/installation_download.html"
    ap.add_argument('-l', '--lang', type=str,
                    help="StanfordNLP language code. Check\n" + lang_code_link,
                    default='en')
    ap.add_argument('-p', '--port', type=int,
                    help="Port number to run this service on.",
                    default=5010)

    a = ap.parse_args()

    # Sanitize arg inputs
    a.lang = re.sub('[^a-zA-Z]', '', a.lang).lower()

    return a


if __name__ == "__main__":
    args = get_args()

    try:
        config.nlp = stanfordnlp.Pipeline(lang=args.lang,
                                          processors='tokenize,mwt,pos,lemma')
    except KeyError:
        print('Invalid language selected.')
        exit(1)

    config.connex_app.run(debug=True, port=args.port)
