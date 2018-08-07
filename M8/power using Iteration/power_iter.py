'''Exercise: PowerIter'''
# Write a Python function, iterPower(base, exp),
#that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.


def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

    power_val = 1
    while exp != 0:
        power_val *= base
        exp -= 1
    return power_val

def main():
    '''function'''
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
