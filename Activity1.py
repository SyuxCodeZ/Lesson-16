# the variables
try:
    num = int(input("Enter A Number: "))
    print (f"The Number You Entered Is {num}")

except ValueError as ex:
    print (f"Error: {ex}")