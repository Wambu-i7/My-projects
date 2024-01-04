#!/usr/bin/python3
class Books:
    def __init__(self, genre, writer):
        self.typeof = genre
        self.artist = writer
    def content(self):
        print(f"Hi, my name is {Book_2.artist}, I write {Book_1.typeof} books")
Book_1 = Books("motivation", "James")
Book_2 = Books("Romance","Jenny")
Book_1.content()
Book_2.content()
print(Book_1.typeof)
print(Book_2.artist)

