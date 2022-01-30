#Write a program that prints the integers from 1 to 200. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"

for i in range(1,201):
    if i % 5==0 and i % 3==0:
        print("Fizzbuzz")

    elif i % 3==0:
        print("Fizz")

    elif i % 5 ==0:
        print("Buzz")

    else:
        print(int(i))
#
#
# Write a Python function to multiply all the numbers in a list.
#
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    total = 1

    for i in numbers:
        total *= i
    return total

list=[1,2,3,-4]
print(multiply(list))

