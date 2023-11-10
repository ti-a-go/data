from Wiki import Wiki


def test_search():
    wiki = Wiki()
    result = wiki.search("Wikipedia")
    assert len(result) > 0
