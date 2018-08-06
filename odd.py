'''Exercise: odd'''
# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.
def odd(x_y):
    '''square function'''
    return x_y%2 != 0
def main():
    '''function'''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
