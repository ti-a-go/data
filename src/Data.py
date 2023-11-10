from os.path import join, exists
from os import makedirs
from wikipedia import WikipediaPage


class Data:
    ROOT_DIR = "data"
    WIKI_DIR = "wikipedia"

    def __int__(self):
        if not exists(self.ROOT_DIR):
            makedirs(self.ROOT_DIR)

        if not exists(self.WIKI_DIR):
            makedirs(join(self.ROOT_DIR, self.WIKI_DIR))

    def save_wiki_page(self, page: WikipediaPage):
        page_dir = join(self.ROOT_DIR, self.WIKI_DIR, page.title)
        if not exists(page_dir):
            makedirs(page_dir)
        file = join(page_dir, f"{page.title}.txt")
        with open(file, "w", encoding="UTF-8") as f:
            f.write(page.content)

    def save_wiki_pages(self, pages: list[WikipediaPage]):
        for page in pages:
            self.save_wiki_page(page)

    def is_page_saved(self, title):
        file = join(self.ROOT_DIR, self.WIKI_DIR, title, f"{title}.txt")
        if exists(file):
            return True
        else:
            return False

