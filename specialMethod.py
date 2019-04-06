
class Sample():
    pass

class Book():

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self): #we use __str__ if we want to print something from class it's like in c# 'ToString' Function
        return f"{self.title} by {self.author} "
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print("A Book Object has been deleted")

B = Book('Python rocks','Jose',200)
print(len(B))   # --> 200
print(B)        # --> Python rocks by Jose
print(B)        # --> A Book Object has been deleted
#del B           # Delete Variables from memory

