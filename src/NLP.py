from wikipedia import WikipediaPage

class NLP:

    def __init__(self, data, wiki) -> None:
        self.data = data
        self.wiki = wiki

    def save_wiki_linked_pages(self, page: WikipediaPage, limit = None):
        if not limit:
            limit = len(page.links)
        for link in page.links[:limit]:
            try:
                if not self.data.is_page_saved(link):
                    self.data.save_wiki_page(self.wiki.page(link))
            except Exception as e:
                print(str(e))