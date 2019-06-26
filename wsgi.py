import os

import stanfordnlp

import config
from server import get_args

activate_this = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'venv', 'bin', 'activate_this.py')

application = config.connex_app

if __name__ == "__main__":
    args = get_args()

    try:
        config.nlp = stanfordnlp.Pipeline(lang=args.lang,
                                          models_dir=args.models_dir,
                                          processors='tokenize,mwt,pos,lemma')
    except KeyError:
        print('Invalid arguments.')
        exit(1)


    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

    application.run(debug=args.debug, port=args.port)

