import wikipedia
import os

SAVED_PAGES_FILE = os.path.join("wikipedia", "saved_pages.txt") 
SUMMARIES_FOLEDER = os.path.join("wikipedia", "summaries")

def save_summaries(pages):
    # Save the summary of a list of pages
    if not os.path.exists(SUMMARIES_FOLEDER):
        os.makedirs(SUMMARIES_FOLEDER)
    for page in pages:
        file_name = page.title.replace(" ", "_") + ".txt"
        print(f"Saving page - {page.title}")
        with open(os.path.join(SUMMARIES_FOLEDER, file_name), "w") as file:
            file.write(page.summary)
            file.close()

def search_and_save_summaries(query):
    wikipedia.set_lang("pt")
    results = wikipedia.search(query)
    pages = []
    for result in results:
        print(f"Downloading page - {result}")
        pages.append(wikipedia.page(result))
    # pages = [wikipedia.page(result) for result in results]
    save_summaries(pages)


if __name__ == "__main__":
    # This function search on Wikipedia an saves the summaries from all pages returned from the search.
    search_and_save_summaries("premissa")