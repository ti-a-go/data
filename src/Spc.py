import spacy

class Spc:
    spc = spacy

    def __init__(self) -> None:
        self.pt = spacy.load("pt_core_news_lg")