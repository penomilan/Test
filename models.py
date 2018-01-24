"""Models."""


class Comment(object):
    """Comment model."""

    def __init__(self, text, date):
        """Constructor."""
        self.text = text
        self.date = date

if __name__ == '__main__':
    COMMENTS = [
        Comment("hello", "2018-01-01"),
        Comment("world", "2018-01-02"),
        Comment("test", "2018-01-03"),
    ]