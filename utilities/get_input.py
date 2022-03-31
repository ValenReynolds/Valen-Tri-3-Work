import sys
from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

# a utility to prompt users for integer values within a min and max range
# Now we can clean up some of our code where we prompt for numbers 
def get_integer (message, min=0, max = sys.maxsize, tries=5):
    tries  = 0 
    while tries < 3:
        try:
            result = input(message)
            choice = int(result)
            if (choice >= min and choice <= max):
                return choice
            else:
                print ("Please enter a value between ", min, " and ", max)
                tries += 1
                continue
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