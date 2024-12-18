age=int(input("Enter your age : "))
try :
    if age<18:
        raise IOError
except IOError:
    print("This is IOerror")
finally:
    print("Hi")