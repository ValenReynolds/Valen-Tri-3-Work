--- 
layout: default
permalink: /docs/
---


# Documentation 

## Tree Challenge
This is the code for the tree. 
<img src="https://github.com/ValenReynolds/Valen-Tri-3-Work/blob/main/menus/ship.py?raw=true">

## Algorithms
All the algorithm work is here
https://github.com/ValenReynolds/Valen-Tri-3-Work/tree/main/algorithms 

## Testing Algorithms
Here is an example of my unit tests for the Palindrome algorithm. It uses the built in Python unittest framework
https://github.com/ValenReynolds/Valen-Tri-3-Work/blob/main/algorithms/palindrome_test.py

<pre>
<code>
from unittest import TestCase
from palindrome import Palindrome

class TestPalindrome(TestCase):
    def test_palindromes(self):
        self.assertTrue(Palindrome("abba").isPalindrome)  # add assertion here
        self.assertTrue(Palindrome("abxba").isPalindrome)  # add assertion here
        self.assertTrue(Palindrome("xyzzyx").isPalindrome)  # add assertion here
        self.assertTrue(Palindrome("abcdeffedcba").isPalindrome)  # add assertion here

    def test_longest_palindrome(self):
        self.assertTrue(Palindrome("tattarrattat").isPalindrome)

    def test_not_palindromes(self):
        self.assertFalse(Palindrome("abc").isPalindrome)
        self.assertFalse(Palindrome("Happy").isPalindrome)

    def test_small_pallindrome(self):
        self.assertTrue(Palindrome("aa").isPalindrome)

    def test_onesyllable_palindrome(self):
        pal = Palindrome("a").isPalindrome
        self.assertTrue(pal)
        
    def test_invalid_palindrome(self):
        pal = Palindrome("()*&^").isPalindrome
        self.assertFalse(pal)
</code>
</pre>

## Alphanumeric
This is my utility for handling alphanumeric code that is re-used

<pre>
<code>
import re
import sys
from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

# a utility to prompt users for integer values within a min and max range
# Now we can clean up some of our code where we prompt for numbers 
def get_alphanumeric (message, min=0, max = sys.maxsize, tries=5):
    tries  = 0 
    while tries < 3:
        try:
            result = input(message) 
            pattern = re.compile("[a-zA-Z0-9]")           
            found = pattern.findall(result) 
            if len(found) < len(result):
                print ("Please enter an alphanumeric ")
                tries += 1
                continue
            return result
            # end prompts try
        except ValueError:
            # not a number error
            print("Not a number: ", result)
        except TypeError:
            # not a number error
            print("Type error: ", result)
        except UnboundLocalError:
            # traps all other errors
            print("Invalid input: ", result)
        # end validation try
        tries = tries + 1

    return None
</code>
</pre>
