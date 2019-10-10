import os

import stanfordnlp

import config
from args import get_args


if __name__ == "__main__":
    args = get_args()

    try:
        config.nlp = stanfordnlp.Pipeline(lang=args.lang,
                                          models_dir=args.models_dir,
                                          processors='tokenize,mwt,pos,lemma')
    except KeyError:
        print('Invalid arguments.')
        exit(1)

    config.connex_app.run(debug=args.debug, port=args.port)

