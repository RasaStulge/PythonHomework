# Create a function that will calculate the number of upper and lower case letters in a string
# eg for: "The quick Brown Fox"
# Expected result:
# Number of uppercase letters: 3, number of lowercase letters: 13
# Hint: use a loop, conditional statement and appropriate methods for the string


s=input('Enter your text:')
u=0
l=0
for i in s:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
print('The number of upper case letters {} and the number of lower case letters {}'.format(u,l))