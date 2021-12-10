# TASK 3
#Create a function that checks that the number given in the argument is prime.
#The function should take a numeric value and return a logical value of True/False.
#eg For 11 the function will return True, for 12 -> False
# Python program to display all the prime numbers within an interval

n1 = 12
n2 = 11

def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if (num1 % i) == 0:
            return False
    return True

if __name__ == '__main__'

    print(f"n1: {is_prime(n1)}")
    print(f"n2: {is_prime(n2)}")