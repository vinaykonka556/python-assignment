#isalnum()

a = "python"
print(a.isalnum()) #True

a = " PYTHON "
print(a.isalnum()) #False

a  = "12345"
print(a.isalnum()) #True

a  = "raina 33"
print(a.isalnum()) #False

a  = "Raina"
print(a.isalnum())  # False

#isalpha()


a = "python"
print(a.isalnum()) #True

a = " PYTHON "
print(a.isalnum()) #False

a  = "12345"
print(a.isalnum()) #True

a  = "raina 33"
print(a.isalnum()) #False

a  = "Raina"
print(a.isalnum())  # False


#isdigit()

a = "12345"
print(a.isdigit()) #True

a = " 12345 "
print(a.isdigit()) # False

a = 12345adc"
print(a.isdigit()) # False


a = 1234 576"
print(a.isdigit()) # False


#islower()

a = "python is a easy to learn"
print(a.islower()) #True

a = "Python"
print(a.islower()) #False

a = "p y thon"
print(a.islower()) #True

a = "python1233"
print(a.islower()) #True


#isupper()

a = "PYTHON"
print(a.isupper())  #True

a = "pyTHON"
print(a.isupper())  #False

a = "PYTHON 123"
print(a.isupper()) #True


a = "python 123"
print(a.isupper())  # False


#istitle()

a = "PYTHON"
print(a.istitle()) # False

a = "Python"
print(a.istitle()) #True

a = "python"
print(a.istitle())  #False

a = "Python 1233"
print(a.istitle()) #Ture


#isspace()

a = "python"
print(a.isspace()) #False

a = "PYTHON"
print(a.isspace()) #False

a = "python  123"
print(a.isspace()) # False


a = "python123"
print(a.isspace())  #Fals