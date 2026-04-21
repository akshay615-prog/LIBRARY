
# NEW LIBRARY

books=[]
issued_books=[]

def add_books():
    name=input("Enter The Book Name: ")
    books.append(name)
    print("✅",name,"is added")

def show_books():
    if len(books)==0:
        print("⚠️ No books available")
        return
    else:
        print("\n📖 Available Books")
        print("---------------------")
        i=1
        for b in books:
            print(i,".",b)
            i+=1

def issue_books():
    if len(books)==0:
        print("⚠️ No Books available")
    else:
        show_books()
        name=input("Enter the book name: ")
        if name in books:
            books.remove(name)
            issued_books.append(name)
            print("📕",name,"book issued")
        else:
            print("❌",name,"is not available")

def return_books():
    name=input("Enter the issued book you want to return: ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("📗",name,"book is returned")
    else:
        print("❌",name,"was not issued")

def library():
    while True:
        print("\n==============================")
        print("📚 LIBRARY MENU")
        print("==============================")
        print("1.Add Books")
        print("2.Show Books")
        print("3.Issue Books")
        print("4.Return Books")
        print("5.Exit")
        print("==============================")

        choice=int(input("Enter your choice: "))

        if choice==1:
            add_books()
        elif choice==2:
            show_books()
        elif choice==3:
            issue_books()
        elif choice==4:
            return_books()
        elif choice==5:
            print("👋 Thank you!")
            break
        else:
            print("❌ Invalid choice")

library()
