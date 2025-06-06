def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    n = int(input("Enter a number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    result = in_range(n, low, high)
    print("In range?" , result)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
