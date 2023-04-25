fp = {}
sol = {}

# finds all integer factor pairs 
def findfp(n):
    for i in range(1, n+1):
        if n%i == 0:
            fp[i] = n/i

# checks if the element is congruent to d when prime factotized, removed if not
def checkmodc(c, d):
    deldict = []
    mod = c - d%c
    for key in fp:
        if not key%c == mod or not fp[key]%c == mod:
            deldict.append(key)

    for key in deldict:
        del fp[key]

# solves for a and b by setting factor pair equal to modified LHS of equation
def solvefp(c, d):
    for key in fp:
        a = (key+d)/c
        b = (fp[key]+d)/c
        sol[a] = b
            


if __name__ == '__main__':
    print('Problem 2018 A1 Putnam: Find all integer factor pairs for which \n1/a + 1/b = c/d ')
    c = int(input('Please enter a value for c: '))
    d = int(input('Please enter a value for d: '))
    findfp(d**2)
    checkmodc(c, d)
    #print(fp)                                       # prints the possible factor pairs
    solvefp(c, d)
    for key in sol.keys():                            # prints the solution set
      print(str(key) + ", " + str(sol[key]))
    
    #print(sol)                                      # prints the solution set
    # for key in sol:                               # preliminary checker of solution set, will not always work due to rounding issues but serves as a general analysis
    #     print(1/key + 1/sol[key] == c/d)