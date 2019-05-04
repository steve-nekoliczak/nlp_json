from models import Word, WordSchema
import config


def process_sentences(sentences_str):
    sentences = config.nlp(sentences_str).sentences

    sentences_json = []
    dummy_schema = WordSchema()
    for i, sentence in enumerate(sentences):
        sentences_json.append([])
        for word in sentence.words:
            word_obj = Word()
            word_obj.text = word.text
            word_obj.lemma = word.lemma
            word_obj.pos = word.upos

            word_obj.feats = dict(x.split('=') for x in word.feats.split('|') if "=" in x)

            sentences_json[i].append(dummy_schema.dump(word_obj).data)

    return sentences_json
