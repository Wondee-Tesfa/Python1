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
        
#2 To calculate the area and curcumference of a CIRCLE by recieving the radius from the user ond using PYTHON Language.

pi = 3.14
rad = float(input("\nEnter the Radius : "))
if rad >= 0:
    area = pi*rad**2
    circm= pi*rad*2
    
    print(f"The Area of radius {rad} is {area}M square. \n")
    print(f"The Circumfference of radius {rad} is {circm}M.\n")
else:
    print("Your radius shoud be greater than 0.")    