from src.Wiki import Wiki
from src.Spc import Spc
from src.Data import Data
from src.NLP import NLP

wiki = Wiki()
spc = Spc()
data = Data()
nlp = NLP(data, wiki)

if __name__ == "__main__":
    print(wiki.search("wikipédia"))