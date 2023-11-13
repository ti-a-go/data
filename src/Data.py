from os.path import join, exists, getsize
from os import makedirs, listdir
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
        file_path = self.get_file_path(title)
        if exists(file_path):
            return True
        else:
            return False

    def generate_wiki_page_metadata(self):
        first_title = listdir(join(self.ROOT_DIR, self.WIKI_DIR))[0]
        return first_title

    def load_wiki_page_content(self, title):
        file_path = self.get_file_path(title)
        content = None
        if not exists(file_path):
            return content
        with open(file_path, "r", encoding="UTF-8") as f:
            content = f.read()
        return content

    def get_file_path(self, title: str):
        return join(self.ROOT_DIR, self.WIKI_DIR, title, f"{title}.txt")

    def list_saved_wiki_pages(self):
        return listdir(join(self.ROOT_DIR, self.WIKI_DIR))

    def page_content_size(self, title):
        file_path = self.get_file_path(title)
        return getsize(file_path)

    def wikipedia_data_size(self):
        return getsize(join(self.ROOT_DIR, self.WIKI_DIR))
