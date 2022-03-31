import math
# Python code to demonstrate naive method
# to compute factorial
def get_factorial():
    # get user choice
    choice = input("Enter factor: ")
    Factor.myfactorial(int(choice)) 

class Factor:
    def myfactorial(n):
        if n < 0:
            return math.nan

        fact = 1
        for i in range(1,n+1):
            fact = fact * i
            
        print ("The factorial of " , n, " is ", fact)
        return fact

    # Test Code
if __name__ == "__main__":
    get_factorial()
    '''Value for testing
    n = 20
    for i in range(n):
        print("Factor (",i,") = ", Factor.myfactorial(i))
    '''