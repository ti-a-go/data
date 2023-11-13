from src.Wiki import Wiki
from src.Spc import Spc
from src.Data import Data
from src.NLP import NLP

wiki = Wiki()
spc = Spc()
data = Data()
nlp = NLP(data, wiki)

if __name__ == "__main__":
    # title = data.generate_wiki_page_metadata()
    saved_wiki_pages = data.list_saved_wiki_pages()
    print(f"saved wiki pages count: {len(saved_wiki_pages)}")
    print(f"saved wiki pages: {saved_wiki_pages}")
    page_content_size = data.page_content_size(saved_wiki_pages[0])
    print(f"page content size: {page_content_size} bytes")
    print(f"page content size: {page_content_size / 1000} kB")
    content = data.load_wiki_page_content(saved_wiki_pages[0])
    print(f"page content head: {content[:100]}")
    print(f"page content character count: {len(content)}")
    print(f"Wikipedia data size: {data.wikipedia_data_size()} bytes")


