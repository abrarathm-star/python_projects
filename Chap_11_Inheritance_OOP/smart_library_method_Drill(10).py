class Library():
    library="Bibliothek"
    def __init__(self,title,author,available_copies):
        self.title=title
        self.author=author
        self.available_copies=available_copies

    def show(self):
        print(self.title)
        print(self.author)
        print(self.available_copies)
    def Borrow_books(self,books):
        if self.available_copies>3:
            self.available_copies-=books
        else:
            print("not enough copies are available")
    def return_books(self,books):
        self.available_copies+=books
    @classmethod
    def change_name(cls):
        cls.library="HM Bibliothek"
    @staticmethod
    def rules():
        print("Rules\n"
        "1. keep silence please!\n2. no open drinks and food are allowed.\n"
        "3. During a break a break card must be used and should be placed on the table\n" \
        "4. Books can be borrowed for not more than 7 days.\n" \
        "5. only university students and members can borrow books.\n" \
        "6.books must be return in the same condition as before.")
b1=Library("way of life","abc",3)
Library.change_name()
b1.show()
print()
print(b1.library)
b1.Borrow_books(1)
b1.return_books(0)
print()
print(b1.available_copies)
print()
Library.rules()
print()