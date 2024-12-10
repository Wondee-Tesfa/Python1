#1 To check from the given three number which one is greater by using Python Language.

number1 = float (input ("Enter the number : "))
number2 = float (input ("Enter the number : "))
number3 = float (input ("Enter the number : "))

if number1 > number2:
    if number1 > number3:
        print (f"{number1} is the largest number.")
    else:
        print (f"{number3} is the largest number.")
else:
    if number2 > number3:
        print(f"{number2} is the largest number.")
    else:
        print(f"{number3} is the largest number.")