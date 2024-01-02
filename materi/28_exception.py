try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")
