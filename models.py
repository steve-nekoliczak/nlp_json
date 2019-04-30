from marshmallow import fields, Schema


class Features:
    def __init__(self):
        # shared article/adjective/pronoun/verb feats
        self.number = ""
        # shared article/adjective/pronoun feats
        self.case = ""
        self.gender = ""
        # shared article/pronoun feats
        self.pron_type = ""
        # shared pronoun/verb feats
        self.person = ""
        # only article feats
        self.definite = ""
        # only verb feats
        self.mood = ""
        self.tense = ""
        self.verb_form = ""


class Word:
    def __init__(self):
        self.text = ""
        self.lemma = ""
        self.pos = ""
        self.feats = Features()


class FeaturesSchema(Schema):
    # shared article/adjective/pronoun/verb feats
    case = fields.Str()
    # shared article/adjective/pronoun feats
    number = fields.Str()
    gender = fields.Str()
    # shared article/pronoun feats
    pron_type = fields.Str()
    # shared pronoun/verb feats
    person = fields.Str()
    # only article feats
    definite = fields.Str()
    # only verb feats
    mood = fields.Str()
    tense = fields.Str()
    verb_form = fields.Str()


class WordSchema(Schema):
    text = fields.Str()
    lemma = fields.Str()
    pos = fields.Str()
    feats = fields.Nested(FeaturesSchema())


