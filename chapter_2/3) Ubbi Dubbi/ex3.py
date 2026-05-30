def remove_author_names(article, authors):
    for name in authors:
        article = article.replace(name, '_____')
    return article

article = "This paper was written by Alice Smith and Bob Jones."
authors = ["Alice Smith", "Bob Jones"]

print(remove_author_names(article, authors))