import wikipedia


class Wiki:
    wikipedia = wikipedia

    def search(self, query, results=10, lang="pt"):
        self.wikipedia.set_lang(lang)
        pages = self.wikipedia.search(query, results=results)
        return pages

    def page(self, title):
        return self.wikipedia.page(title)

    def pages(self, titles):
        pages = []
        for title in titles:
            pages.append(self.wikipedia.page(title))
        return pages
