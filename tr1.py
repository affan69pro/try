num=1
try :
    print(num)
except NameError:
    print("This is a name error")
finally:
    print("hello")