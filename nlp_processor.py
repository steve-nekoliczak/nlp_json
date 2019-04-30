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

            feats = dict(x.split('=') for x in word.feats.split('|') if "=" in x)
            if 'Case' in feats:
                word_obj.feats.case = feats['Case']
            if 'Gender' in feats:
                word_obj.feats.gender = feats['Gender']
            if 'Number' in feats:
                word_obj.feats.number = feats['Number']
            if 'PronType' in feats:
                word_obj.feats.pron_type = feats['PronType']
            if 'Person' in feats:
                word_obj.feats.person = feats['Person']
            if 'Definite' in feats:
                word_obj.feats.definite = feats['Definite']
            if 'Mood' in feats:
                word_obj.feats.mood = feats['Mood']
            if 'Tense' in feats:
                word_obj.feats.tense = feats['Tense']
            if 'VerbForm' in feats:
                word_obj.feats.verb_form = feats['VerbForm']

            sentences_json[i].append(dummy_schema.dump(word_obj).data)

    return sentences_json
