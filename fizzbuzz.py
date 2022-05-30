# Script to implement the classic
# FizzBuzz coding exercise.

def fizzbuzz(n):
    for i in range(1, n+1):
        msg = ""
        if i % 3 == 0:
            msg += "fizz"
        if i % 5 == 0:
            msg += "buzz"
        if i % 3 != 0 and i % 5 != 0:
            msg += str(i)
        print(msg)

# This was surprisingly hard for me to
# implement. I assumed I would complete
# the exercise in one or two tries. It was
# more like 5 attempts before I got it right.

fizzbuzz(30)
