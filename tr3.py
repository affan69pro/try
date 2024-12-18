try:
    num1=int(input("Enter your number : "))
    num2=int(input("Enter your number : "))
    result=num1/num2
    print("Result is : ",result)
    print("Result is : ",result1)
except ZeroDivisionError:
    print("This is ZeroDivisionError")
except ValueError:
    print("This is ValueError")
except NameError as ex:
    print("this is NameError")
except:
    print("some error occured")
finally:
    print("I will execute no matter what")