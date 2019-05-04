from marshmallow import fields, Schema


class Word:
    def __init__(self):
        self.text = ""
        self.lemma = ""
        self.pos = ""
        self.feats = {}


class WordSchema(Schema):
    text = fields.Str()
    lemma = fields.Str()
    pos = fields.Str()
    feats = fields.Dict()
