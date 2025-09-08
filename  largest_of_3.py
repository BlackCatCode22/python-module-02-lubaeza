number1 = float(input("Enter first number:" ))
number2 = float(input("Enter second number:" ))
number3 = float(input("Enter third number:" ))

if number1 >= number2:
  if number1 >= number3:
    biggestnumber = number1
  else:
    biggestnumber = number3
else:
  if number2 >= number3:
    biggestnumber = number2
  else:
    biggestnumber = number3
print("The largest of the three numbers is:", biggestnumber)