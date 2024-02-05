class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        self._articles = []
        Magazine._all_magazines.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    def contributors(self):
        return self._contributors

    def add_contributor(self, author):
        self._contributors.append(author)

    def add_article(self, author, title):
        new_article = author.add_article(self, title)
        self._articles.append(new_article)
        return new_article

    @classmethod
    def all(cls):
        return cls._all_magazines

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all_magazines:
            if magazine.name() == name:
                return magazine
        return None

    @classmethod
    def article_titles(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        if magazine:
            return [article.title() for article in magazine._articles]
        return []

    @classmethod
    def contributing_authors(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        if magazine:
            contributors = [author.name() for author in magazine._contributors if len(author.articles()) > 2]
            return contributors
        return []
