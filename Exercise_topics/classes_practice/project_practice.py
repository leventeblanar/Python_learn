# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#             if self.age < 30:
#                 print(f"Hey, My name is {self.name} and I am {self.age} years old.")

#     def have_birthday(self):
#             self.age += 1
#             print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

# persons = []

# for person in range(3):
#     person_name = str(input("What's your name? "))
#     person_age = int(input("What's your age? "))
#     persons.append(Person(person_name, person_age))

# print(persons)

# for person in persons:
#     person.say_hello()
#     person.have_birthday()


# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages

#     def summary(self):
#         print(f"A könyv íme: {self.title}, oldalszáma: {self.pages}")

#     def is_short(self):
#         if self.pages < 150:
#             print(f"A {self.title} könyv egy rövid könyvnek számít.")

# book_collection = []

# for book in range(3):
#     book_title = str(input("Adj meg egy könyv címét: "))
#     book_pages = int(input("Add meg az oldalszámot: "))
    
#     book_collection.append(Book(book_title, book_pages))

# print(book_collection)

# for book in book_collection:
#     book.summary()
#     book.is_short()


