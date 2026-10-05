def function(n):
    if n <= 1:
        return 0
    counter = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            counter += 1
            break
    return counter

C = function(100000)
print(C)