# TASK 6
# Write a function that takes two strings and checks to see if they are
# anagrams of each other.
# For example:
# "Army" and "Mary",
# "Sharing" and "Sunday",
# "Quid est veritas?" and "Vir est qui adest",
# "Jim Morrison" and "Mr.Mojo Risin"
# "Tom Marvolo Riddle" and "I am Lord Voldemort"
str1 = input("string1:")
str2 = input("string2:")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)


if sorted_str1 == sorted_str2:
    print("given strings are anagrams")
else:
    print("given strings are not anagrams")
