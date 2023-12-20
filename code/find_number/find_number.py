"""
Created on Wed Dec 20 16:27:36 2023

@author: Snehal
"""
text = input("Input a word or numbers: ")

# Check if the input consists of digits only using the 'isdigit' method.
if text.isdigit():
    # If the input contains only digits, print "The input value is numbers."
    print("The input value is integer")
    
else:
    try:
        i = float(text)
        print("The input value is float.")
    except (ValueError, TypeError):
        print("The input value is string.")

