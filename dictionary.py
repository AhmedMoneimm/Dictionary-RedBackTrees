import RBTree

def insert_new_word(arr,Tree):
    word=input("Insert word: \n")
    if Tree.search(word)==None:
        arr+=word
        Tree.insert(word)
        Tree.print_size()
        Tree.print_height()
    else:
        print("Error! Word already in dictionary.")

def lookup(Tree):
    word=input("Enter word: \n")
    if Tree.search(word) == None:
        print("NO")
    else:
        print("YES")



file1=open("EN-US-Dictionary.txt","r+")
arr=[]
arr=file1.readlines()
Tree=RBTree.RBTree()
for i in range(0,arr.__len__()):
    Tree.insert(arr[i])
order=input("Enter operation:")
while order!="4":
    if order=="1":
        insert_new_word(arr,Tree)
        order = input("Enter operation:")
    if order == "2":
        lookup(Tree)
        order = input("Enter operation:")
    if order=="3":
        Tree.print_size()
        order = input("Enter operation:")




