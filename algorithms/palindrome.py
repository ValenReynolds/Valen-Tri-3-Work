import re

def is_a_palindrome():
    # get user choice
    choice = input("Enter string to run through palindrome checker: ")
    if Palindrome(choice).isPalindrome == True:
        print ("Congratulations ", choice, " is a Palindrome")
    else:
        print ("Sorry", choice, " is not a Palindrome")

class Palindrome:
    # palindrome initializer method
    def __init__(self, candidate):
        # input values
        self._candidate = candidate  # input string
        self._length = len(candidate)  # input length
        # analysis values
        self._is_a_palindrome = False  # initialize status
        self._az09 = re.sub(r'[^a-zA-Z0-9]', '', self._candidate)  # alpha numeric characters
        self._analysis = []  # array of tests
        self._tests = 0  # counter of tests performed
        # evaluate for palindrome
        self.is_palindrome()

    # palindrome tester method
    def is_palindrome(self):
        c = self._az09
        # Run loop from 0 to len/2 of string (middle is exit point)
        tests = int(len(c) / 2)
        for i in range(0, tests):
            front = c[i];
            back = c[len(c) - i - 1]
            if front.lower() == back.lower():
                self.logger(front, back, True)
                self._tests += 1
            else:
                self.logger(front, back, False)
                self._is_a_palindrome = False  # should assign here
                return False
        self._is_a_palindrome = True
        return True

    # palindrome logging
    def logger(self, front, back, result):
        self._analysis.append({"test": self._tests, "front": front, "back": back, "result": result})

    # getters follow
    @property
    def candidate(self):
        return self._candidate

    @property
    def tests(self):
        return self._tests

    @property
    def isPalindrome(self):
        return self.is_palindrome()

    @property
    def analysis(self):
        return self._analysis

if __name__ == '__main__':
    if Palindrome("abba").isPalindrome == True:
        print ("abba is a Palindrome")
    if Palindrome("abxba").isPalindrome == True:
        print ("abxba is a Palindrome")
    # these pass, but if any one failed our main would stop running on a failed assertion
    assert(Palindrome("xyzzyx").isPalindrome == True) 
    assert(Palindrome("abcdeffedcba").isPalindrome == True)  
    # Sadness is a fail
    assert(Palindrome("Sadness").isPalindrome == False)
    # longest true Palindrome
    if (Palindrome("tattarrattat").isPalindrome):
        print ("tattarrattat is a Palindrome")