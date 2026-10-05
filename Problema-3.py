import time
def function(n):
    counter = 0
    for i in range(1, n//3 + 1):
        for j in range(1, n+1, 4):
            counter += 1
    return counter

# {1, 10, 100, 1000, 10000, 100000, 1000000}

C = function(1)
print(C)