from RBTree import RBTree

def insert_new_word(Tree):
    word=input("Insert word: \n")

    if Tree.search(word):
        print("Error! Word already in dictionary.")
        return
    else:
        # words_list.append(word) ## not needed as we won't save words into the .txt file
        Tree.insert(word)
        Tree.print_size()
        Tree.print_height()

def lookup(Tree):
    word=input("Enter word: \n")

    if Tree.search(word) is not None:
        print("YES")
    else:
        print("NO")


file=open("EN-US-Dictionary.txt","r")

Tree = RBTree()

words_list=[]

for line in file:
    words_list.append(line.strip())

for word in words_list:
    Tree.insert(word)

order=input("Choose operation: \n 1. Insert new word \n 2. Lookup \n 3. Print size \n 4. Exit \n")

while order!="4":
    if order=="1":
        insert_new_word(Tree)
        order = input("Enter operation:")
    if order == "2":
        lookup(Tree)
        order = input("Enter operation:")
    if order=="3":
        Tree.print_size()
        order = input("Enter operation:")