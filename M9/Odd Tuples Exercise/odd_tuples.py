'''Exercise : Odd Tuples'''
# Write a python function oddTuples
def oddtuples(atup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    # Your Code Here

    return atup[::2]

def main():
    '''Input'''
    data = input()
    data = data.split()
    atup = ()
    for j in range(len(data)):
        atup += ((data[j]),)
    print(oddtuples(atup))

if __name__ == "__main__":
    main()
