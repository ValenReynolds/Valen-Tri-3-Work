def swap(first, second):
    print ("swap ", first, second)
    temp = first
    first = second
    second = temp
    return first, second

def swap_items():
    # get user choice
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    first, second = swap(first, second)
    print ("Swap result: ", first, second)