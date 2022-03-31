# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import sys
from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
import ship
import swap
import tree
from algorithms import factorial
from algorithms import palindrome
from algorithms import primes

# Main list of [Prompts, Actions]
# One style is supported to execute abstracted logic (using exec is not secure)
# 1. External function references are executed directly file.function()
# 2. Internal function references are called directly "function()"
main_menu = [
    ["Swap", swap.swap_items],
    ["Tree", tree.tree],
]

animations_sub_menu = [
    ["Ship", ship.ship],
]

patterns_sub_menu = [
    ["Palindrome", palindrome.is_a_palindrome],
]
algorithms_sub_menu = [
    ["Factorial", factorial.get_factorial],
    ["Primes", primes.is_prime_number],
]


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control


def menu():
    title = "Main Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", animations_submenu])
    menu_list.append(["Patterns", patterns_submenu])
    menu_list.append(["Algorithms", algorithms_submenu])
    
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()


def animations_submenu():
    title = "Animations Submenu" + banner
    buildMenu(title, animations_sub_menu)


def patterns_submenu():
    title = "Patterns Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def algorithms_submenu():
    title = "Algorithms Submenu" + banner
    buildMenu(title, algorithms_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    if (banner[0:4] == "Main"):
        prompts = {0: ["Exit", None]}
    else:
        prompts = {0: ["Main Menu", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except TypeError:
        # not a number error
        print(f"Type Error - maybe menus are set up wrong: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
