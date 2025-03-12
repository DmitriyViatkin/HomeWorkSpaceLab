import copy

Books=[0,2,32,[45,78]]
print("Books",Books)
NewBooks = Books.copy()
TwoBook=copy.deepcopy(Books)
print("NewBooks", NewBooks)
print("TwoBook",TwoBook)
Books[3].append("Two")
NewBooks[3].append("One")
print("*"*10)
print("Books",Books)
print("NewBooks", NewBooks)
print("TwoBook",TwoBook)
print("*"*10)
TwoBook[3].append('Three')
print("Books",Books)
print("NewBooks", NewBooks)
print("TwoBook",TwoBook)