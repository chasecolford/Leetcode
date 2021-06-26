def numberOfMathes(n):
    matches = 0
    if n == 1: return 0
    while n > 1:
        if n % 2 == 0:
            matches += n // 2
            n = n // 2
        else:
            matches += (n - 1) // 2
            n = (n - 1) // 2 + 1
    return matches


#expected 13
print(numberOfMathes(14))

#expected 6
print(numberOfMathes(7))