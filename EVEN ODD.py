'''
1. Conditional Statement
Write a Python program that checks if a number entered by the user is even or odd.

'''

def oddOrEven(number):
    
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


number = int(input("Enter a number: "))
oddOrEven(number)
