number1 = int(input("Enter first number:" ))
number2 = int(input("Enter second number:" ))
number3 = int(input("Enter third number:" ))

def computebiggest(number1, number2, number3):
  if number1 >= number2:
    if number1 >= number3:
      return number1
    else:
      return number3
  else:
    if number2 >= number3:
      return number2
    else:
      return number3

biggestnumber = computebiggest(number1, number2, number3)
if biggestnumber == number1:
  variable_name = "number1"
elif biggestnumber == number2:
  variable_name = "number2"
else:
  variable_name = "number3"


print(f"You entered three numbers: {number1}, {number2}, and {number3}. The first whole number you " \
f"entered ({number1}) was assigned to a variable named number1, the second to ({number2}) to number2, and " \
f"finally the third ({number3}) was assigned to number3. Your input was processed and the " \
f"largest number you entered was {biggestnumber}, which belonged to an integer variable named {variable_name}.")
