class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Returns a list of all contracts related to this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Returns a list of all books written by this author."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Creates and returns a new Contract between the author and the specified book."""
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer.")
        return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self):
        """Returns the total royalties earned by the author across all their contracts."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Returns a list of all contracts related to this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Returns a list of all authors who have contracts for this book."""
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts that have the specified date."""
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        return [contract for contract in cls.all if contract.date == date]
