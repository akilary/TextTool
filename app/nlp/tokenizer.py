import json

from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters


def get_custom_tokenizer() -> PunktSentenceTokenizer:
    """Создаёт токенайзер с кастомными аббревиатурами"""
    with open("data/abbreviations.json") as f:
        data = json.load(f)
        abbr = data["russian"] + data["english"]
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = set(abbr)
    return PunktSentenceTokenizer(punkt_param)
