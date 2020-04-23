a = 5
b = 2
try:
    f= open("C:/Users/Nikhesh/desktop/niks.txt",'r+')
    k = (input("Enter what ever u want "))
    f.write(k)
    print("Division is ",a/b)

except ValueError as n:
    print("Invalid input")

except ZeroDivisionError as e:
    print("Divide by zero is not poosibe")

except Exception as e:
    print("Something went wrong ")

finally:
    print("bye")
    f.close()