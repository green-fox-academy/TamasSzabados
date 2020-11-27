class Blog_post:
    def __init__(self, authorName, title, text, publicationDate):
        self.authorName = authorName
        self.title = title
        self.text = text
        self.publicationDate = publicationDate

    def __repr__(self):
        return repr(self.authorName)