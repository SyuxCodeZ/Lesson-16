try:
    num1, num2 = eval(input("Enter 2 numbers seperated by commas:"))
    result = num1 / num2
    print (result)

except ZeroDivisionError:
    print ("Division By Zero Is Not Allowed\n")
except SyntaxError:
    print ("Use A Comma Like This: 1, 2\n")
except:
    print ("Wrong Input\n")
else:
    print ("No Exceptions\n")
finally:
    print ("This Will Run No Matter What\n")