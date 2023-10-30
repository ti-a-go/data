
import os
import pandas as pd
import wikipedia
import spacy



SUMMARY_FOLDER = os.path.join("summary")
SUMMARY_RAW_FOLDER = os.path.join(SUMMARY_FOLDER, "raw")
SUMMARY_DOC_FOLDER = os.path.join(SUMMARY_FOLDER, "doc")
DATA_FOLDER = "data"
FEDERAL_CONSTITUTION_FILE = os.path.join(DATA_FOLDER, "Constituição Federal.txt")





def load_federal_constitution_text():
    text = ""
    with open(FEDERAL_CONSTITUTION_FILE, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def search(query, results=10, lang="pt"):
    wikipedia.set_lang(lang)
    pages = wikipedia.search(query, results=results)
    return pages


def download_summary(page_title: str, lang="pt"):
    wikipedia.set_lang(lang)
    summary = ""
    try:
        summary = wikipedia.summary(page_title)
    except Exception as e:
        print(str(e))
    if not os.path.exists(SUMMARY_RAW_FOLDER):
        os.makedirs(SUMMARY_RAW_FOLDER)
    file_name = f"{page_title}.txt"
    with open(os.path.join(SUMMARY_RAW_FOLDER, file_name), "w") as file:
            file.write(summary)
            file.close()


def summaries():
    files = os.listdir(SUMMARY_RAW_FOLDER)
    summaries = [file.replace(".txt", "") for file in files]
    return pd.DataFrame(summaries, columns=["Summaries Files"])


def load_summary(summary):
    file_name = f"{summary}.txt"
    file_path = os.path.join(SUMMARY_RAW_FOLDER, file_name)
    text = ""
    with open(file_path, "r") as file:
        text = file.read()
    return text


def create_doc(text, model="pt_core_news_lg"):
    nlp = spacy.load(model)
    return nlp(text)


def create_tokens_df(doc):
    data = []
    for token in doc:
        data.append((token.text, token.dep_, token.lemma_, token.morph, token.pos_, token.tag_))
    return pd.DataFrame(data=data, columns=["text", "dep_", "lemma_", "morph", "pos_", "tag_"])


def save_csv(df, page_title):
    file_name = f"{page_title}.csv"
    file_path = os.path.join(SUMMARY_DOC_FOLDER, file_name)
    if not os.path.exists(SUMMARY_DOC_FOLDER):
        os.makedirs(SUMMARY_DOC_FOLDER)
    df.to_csv(file_path, encoding="utf-8")


