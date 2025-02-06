Is_True = False

while not Is_True:
    try:
        num = int(input("Enter A Number: "))
        while (num % 2) == 0:
            print ("Bye Bye Bye")
        Is_True = True
    except ValueError:
            print ("Invalid")