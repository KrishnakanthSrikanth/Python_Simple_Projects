##Pyramid Pattern

def pattern(n):
    k = 2*n-2
    for i in range(0,n+1):
        for j in range(0,k+1):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
pattern(5)
##--------------------------------------
##InversePyramid

def pattern(n):
    k=2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)
##-------------------------------------
##RightSidePyramid

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    for i in range(i,-1,-1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)
##--------------------------------------
##LeftPyramid

def pattern(n):
    k=2*n-2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    k=-1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)
##--------------------------------------
##HourGlassPyramid

def pattern(n):
    k=n -2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
    k = 2 * n - 2
    for i in range(0,n+1):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)
##---------------------------------------------
##LeftTriangle

def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
pattern(5)
##-------------------------------------------
##RightTriangle

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)
##------------------------------------------
##DownwardHalfPyramid

def pattern(n):
    print("#####")
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(5)
##-------------------------------------------