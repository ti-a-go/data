# Tasks


Save Token List
- after save the summary of a page, process it using Spacy model and save the tokens data on a csv file.
    - a python function that receive a list of Wikipedia pages, process each summary and save the list of tokens in a csv file with the same name of the text file plus the indication that it's a token list, something like ´{page.title}.txt´ generates ´{page.title}_tokens.csv´

Define which text file metadata will be generated.
- charactes count
- text data size (disk space used to store the data)

Define wich tokens metadata will be generated
- tokens count


# Requirements
- Save Token list
- Save more data from the page besides the summary
- Save metadata: characters stats, string stats, data storage stats.


# Input
- search = the search query used to get the Wikipedia Page.

# Script Flow
- donwload page summaries from Wikipedia search (DONE)
- treat disambiguation
- process the page summary using Spacy model
- save the data anotated by the model in csv format

# Interface
- python script

# Dependencies

- Wikipedia
- Spacy
- Pandas
