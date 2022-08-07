# This is my DCIT 104 assignment in python
# The aim of the code is to find the average of prime numbers from 1 to any given number


def isPrime(n):
    # since 0 and 1 is not prime return false.
    if n == 1 or n == 0:
        return False

    # Run a loop from 2 to n-1
    for i in range(2, n):
        # if the number is divisible by i, then n is not a prime number.
        if n % i == 0:
            return False

    # otherwise, n is prime number.
    return True


def main():
    # create an empty list/array and a sum variable that's initialised to 0
    lst = []
    sum = 0
    print(
        "This code will print out the average of prime numbers from 1 to any given number\n"
    )
    last_num = int(input("Please enter any positive integer apart from 1:"))
    # Use a for loop to go through the given range of numbers from 1 till the last_num variable which is entered by the user
    # check if the variable i is prime and print the values
    for i in range(1, last_num + 1):
        if isPrime(i):
            print(i, end="  ")
            # put the values of i into the new list
            lst += [i]
    print("")  # This print statement creates a new line space
    for j in lst:
        # add the values of i and assign it to the variable sum
        sum += j
        n = len(lst)
        Average = sum / n
    print("The average of prime numbers in the given range is:", round(Average, 2))


main()
