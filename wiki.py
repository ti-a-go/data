import os
import wikipedia
from wikipedia.exceptions import DisambiguationError
import spacy
import pandas as pd

SAVED_PAGES_FILE = os.path.join("wikipedia", "saved_pages.txt") 
SUMMARIES_FOLEDER = os.path.join("wikipedia", "summaries")

def save_summaries(summaries):
    # Save the summary of a list of pages
    if not os.path.exists(SUMMARIES_FOLEDER):
        os.makedirs(SUMMARIES_FOLEDER)
    for page_title in summaries:
        file_name = page_title + "_summary.txt"
        print(f"Saving page summary - {page_title}")
        with open(os.path.join(SUMMARIES_FOLEDER, file_name), "w") as file:
            file.write(summaries[page_title])
            file.close()

def search_and_save_summaries(query):
    wikipedia.set_lang("pt")
    results = wikipedia.search(query)
    summaries = {}
    for result in results:
        print(f"Downloading page summary - {result}")
        try:
            summaries[result] = wikipedia.summary(result)
        except Exception as e:
            print(str(e))

    save_summaries(summaries)
    save_summaries_tokens_list(summaries)

def save_summaries_tokens_list(summaries):
    nlp = spacy.load("pt_core_news_lg")
    docs = {}
    for page_title in summaries:
        docs[page_title] = nlp(summaries[page_title])
    
    dfs = {}
    for page_title in docs:
      print(f"Creating DataFrame: {page_title}")
    
      doc = docs[page_title]
      print(f"Doc text: {doc[:10]}...\n")
    
      data = []
      for token in doc:
        data.append((token.text, token.dep_, token.lemma_, token.morph, token.pos_, token.tag_))
    
      dfs[page_title] = pd.DataFrame(data=data, columns=["text", "dep_", "lemma_", "morph", "pos_", "tag_"])

      for page_title in dfs:
        df = dfs[page_title]
        file_name = page_title + "_tokens.csv";
        file_path = os.path.join("wikipedia", "summaries", file_name)
        df.to_csv(file_path, encoding="utf-8")


if __name__ == "__main__":
    search_and_save_summaries("física quantica")
    # This function search on Wikipedia an saves the summaries from all pages returned from the search.