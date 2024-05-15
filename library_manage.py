class Library():
    def __init__(self):
        self.bookGiven = []
        self.bookTaken = []
    
    def giveBook(self, author, book):
        self.bookGiven.append({"Author" : author, "Book" : book})
    
    def printGivenBook(self):
        str = ""
        for book in self.bookGiven:
            str += f"""
    Author : {book['Author']} -> Book : {book['Book']}
    """
        return str
    
    def takeBook(self, author, book):
        self.bookTaken.append({"Author" : author, "Book" : book})
        self.bookGiven.pop(self.bookGiven.index({"Author" : author, "Book" : book}))
    
    def printTakenBook(self):
        str = ""
        for book in self.bookTaken:
            str += f"""
    Author : {book['Author']} -> Book : {book['Book']}
    """
        return str


class LibraryMember(Library):
    def __init__(self, name, surname, middleName="", id=0):
        self.name = name
        self.surname = surname
        self.middleName = middleName
        self.id = id
        super().__init__()
        
    def printMemberInfo(self):
        if not id:
            print("Please enter your designated ID.")
        else:
            if self.middleName:
                print(f"""
    Member's Full Name : {self.name} {self.middleName} {self.surname}
    Member's ID : {self.id}
                """)
            else:
                print(f"""
    Member's Full Name : {self.name} {self.surname}
    Member's ID : {self.id}
                """)
    
    def printGivenBook(self):
        print(f"""
    {self.name} {self.surname} gave these books :
    {super().printGivenBook()}
            """) 
    
    def printTakenBook(self):
        print(f"""
    {self.name} {self.surname} take these books :
    {super().printTakenBook()}
            """) 

member1 = LibraryMember("Nafi", "Girgin", id=1)
member1.printMemberInfo()
member1.giveBook(author="JRR Tolkien", book="Lord of The Rings")
member1.giveBook(author="Ray Bradbury", book="Fahrenheit 451")
member1.printGivenBook()
member1.takeBook(author="JRR Tolkien", book="Lord of The Rings")
member1.printTakenBook()
member1.printGivenBook()
