import math
import random

def random(num):
    print(random.random(), "is a random number")
    print(random.randint(),"is a random integer ")
    print(random.randrange(num),"is a random number within the range")


def math(num):
    print(math.ceil(num), "is the ceiling value of ", num)
    print(math.gcd(num,2),f"is the greatest common divisor between {num}, 2")
    print(math.sqrt(num), f"is the square root of {num}")