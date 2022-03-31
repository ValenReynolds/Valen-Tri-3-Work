import sys
from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
from utilities import get_input 

def is_prime_number():
    choice = get_input.get_integer ("Enter number to see if it is prime: ")
    if Primes(int(choice)).is_prime_number(int(choice)) == True:
        print (choice, " is a prime number")
        return True
    else:
        print (choice, " is not a prime number")
        return False
    
class Primes:
# Use OO programming to display all the prime numbers within an interval
    prime_nums = []

    def is_prime_number(self, num):
        if num in self.prime_nums:
            return True
        else:
            return False

    def __init__(self, prime):
        self.primes_between (0, prime)

    def primes_between(self, lower, upper):
        for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    self.prime_nums.append(num)

    def print_prime_nums(self):
        print("Primes are", self.prime_nums)

if __name__ == "__main__":
    '''Value for testing'''
    p = Primes(100)
    p.print_prime_nums()
    is_prime_number()

