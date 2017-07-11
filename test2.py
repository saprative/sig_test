# Dynamic Programming Python implementation of Min Cost Path
# Array dimentions is 3
R = 3
C = 3
from pprint import pprint

# Sample array
p = [[50, 3, 20],
        [30, 200, 2],
        [1, 20, 90]]

def zeros(longint):
    manipulandum = str(longint)
    return len(manipulandum)-len(manipulandum.rstrip('0'))

def more_0_right(rightint,downint):
    if zeros(rightint) == zeros(downint):
        return True
    else:
        return False


def routeGrid(a, m, n):
 
    # Instead of following line, we can use int tc[m+1][n+1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(C)] for x in range(R)]
 
    tc[0][0] = a[0][0]
 
    # Initialize first column of total cost(tc) array
    for i in range(1, m):
        tc[i][0] = tc[i-1][0] * a[i][0]
 
    # Initialize first row of tc array
    for j in range(1, n):
        tc[0][j] = tc[0][j-1] * a[0][j]
 
    # Construct rest of the tc array
    for i in range(1, m):
        for j in range(1, n):
            tc[i][j] = more_0_right(tc[i-1][j], tc[i][j-1]) * a[i][j]
 
    return tc
 
pprint(routeGrid(p, R, C))
 
