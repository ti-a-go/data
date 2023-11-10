# Processamento de Língua Natural

Esse projeto é utilizado para armazenar dados textuais (strings) de diversas fontes e que serão utilizados em outros projetos para testar hipoteses e fazer __provas de conceito__ relacionadas a Processamento de Língua Natural.


# Dados

A pasta dados está organizada da seguinta maneira:

## Wikipedia

A pasta `wikipedia` centraliza os dados extraídos da Wikipedia.

Para mais informações: [Extraindo dados da Wikipedia](./Extraindo%20dados%20da%20Wikipedia.md)


## Datasets (Conjuntos de dados)

Os datasets são a unidade básica de organização dos dados.

[Constituição Federal](./data/Constituição%20Federal/Constituição%20Federal.txt)
[Fonte: Site do Planalto Federal](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm)




# Organização de pastas

a pasta

# Fontes de dados

Wikipedia

# Projetos

[Extração de Informações de Textos Jurídicos](Textos%20Jurídicos.md)

Testa métodos de extração de informações de textos jurídicos, começando pela Constituição Federal.

[Afropedia](Afropedia.md)

Uma interface Web para páginas da Wikipedia relacionada à África e aos povos africanos e em diáspora.

[Linha do Tempo - História](LinhaDoTempo.md)

Uma interface que mostre uma linha do tempo de acontecimentos históricos importantes na história do Universo desde o a grande explosão até o presente momento.


# Open Information Extraction

Textos Acadêmicos:

[Snowball: Extracting Relations from Large Plain-Text Collections](https://www.cs.columbia.edu/~gravano/Papers/2000/dl00.pdf)

[A Survey on Open Information Extraction](https://arxiv.org/pdf/1806.05599.pdf)

[Desafios da tarefa de Extração de Informação Aberta: uma abordagem metodológica de um corpus automatizado até o corpus manual](https://sol.sbc.org.br/index.php/stil/article/view/25477/25298)

[Identifying Relations for Open Information Extraction](https://aclanthology.org/D11-1142.pdf)

# WordNet
    
[Site Oficial de Princeton](https://wordnet.princeton.edu/)

[WordNet Web Browser](http://wordnetweb.princeton.edu/perl/webwn)

[Download WordNet](https://wordnet.princeton.edu/download)

[WordNet PT Site Oficial](https://www.openwordnet-pt.org/)

[NLTK WordNet API](https://www.nltk.org/howto/wordnet.html)

[WordNet PT Github](https://github.com/own-pt/openWordnet-PT)

[WordNet Python Library](https://wn.readthedocs.io/en/latest/)


# Reconhecimento de Entidades Nomeadas

Textos Acadêmicos:

[Reconhecimento de Entidades Nomeadas para o Portugues Usando o OpenNLP](https://repositorio.pucrs.br/dspace/bitstream/10923/14040/2/Reconhecimento_de_Entidades_Nomeadas_para_o_Portugues_Usando_o_OpenNLP.pdf)


# [Universal POS Tag](https://universaldependencies.org/u/pos/)

ADJ: adjective
ADP: adposition
ADV: adverb
AUX: auxiliary
CCONJ: coordinating conjunction
DET: determiner
INTJ: interjection
NOUN: noun
NUM: numeral
PART: particle
PRON: pronoun
PROPN: proper noun
PUNCT: punctuation
SCONJ: subordinating conjunction
SYM: symbol
VERB: verb
X: other

# Canais no YouTube:

- Python Tutorials for Digital Humanities
    https://www.youtube.com/@python-programming
    

# Bibliotecas Python

- Spacy
- Gensim
- NLTK
- Stanza (CoreNLP)
- ScikitLearn
    https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
- [Wn](https://wn.readthedocs.io/en/latest/) WordNet python library

## Install and Run

Esse projeto utiliza modelos pré-treinados disponível na biblioteca Spacy.

Para baixar os modelos execute o script `spacy_download.sh`

Os modelos baixados:
- pt_core_news_lg
- es_dep_news_trf
- zh_core_web_sm