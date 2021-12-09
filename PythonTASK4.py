# TASK 4
# Create a function that checks that the string given as an argument is a palindrome
# ie read backwards and fowards is exactly the same, eg "kayak", "madam").


s = input("Enter the value : ")

reverse = s[::-1]

if( s == reverse ):
    print("yes it is palindrome")
else:
    print("no")
