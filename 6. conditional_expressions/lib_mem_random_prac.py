
while True:

    name=input("Name: ")
    overdue_books=input("do you have overdue books? ")

    if overdue_books=="yes":
        print("Sorry you can not borrow any book.")
    
    elif not overdue_books=="yes":
        banned=input("are you banned? ")
        if banned=="yes":
            print("Sorry you can not borrow any book.")

        else:
            age=int(input("your age? "))
            if age>=16:
                student=input("are you a student: ")
                if  student=="yes":
                    days_needed=int(input("for how many days you need the book: "))
                    number_of_books=int(input("Number of books: "))
                    if number_of_books<=10 and days_needed>=1 and days_needed<=30 :
                        print("you can borrow books for maximum 5 days.")
                    else:
                        print("Sorry you can not borrow any book.")
                else:
                    membership=input("are you a member: ")
                    if membership=="yes":
                        number_of_books=int(input("Number of books: "))
                        days_needed=int(input("for how many days you need the book: "))
                        if days_needed<=7 and number_of_books<4:
                            print("you can borrow books for maximum 5 days. ")
                    
                    elif membership=="no":
                        number_of_books=int(input("Number of books: "))
                        days_needed=int(input("for how many days you need the book: "))
                        if days_needed>=1 and days_needed<=30 and number_of_books>=1 and number_of_books<=30:
                            print("you can borrow 2 books for maximum 3 days. ")
                    else:
                        print("sorry! you can not borrow any books. ")
            elif age<=15 and age>=1 and not banned=="yes" and not overdue_books=="yes":
                parents_permission=input("do you have parents permission? ")
                if parents_permission=="yes":
                    days_needed=int(input("for how many days you need the book: "))
                    number_of_books=int(input("Number of books: "))
                    if (days_needed>=1 or days_needed<=30) and (number_of_books>=3 or number_of_books<=7):
                        print("you can borrow maximum 2 books. ")
                    else:
                        if(number_of_books<=1 and days_needed<=2):
                            print("ok you can borrow")
                        else:
                            print("sorry! you can not borrow any books. ")
                else:
                    print("sorry! you can not borrow any books. ")
    else:
        print("sorry! you can not borrow any books. ")  