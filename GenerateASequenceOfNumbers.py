def generateASequenceOfNumbers(i, j):
    maximum_cycle = 0
    for n in range(i, j+ 1):
        count = 0
        while n != 1:
            count += 1
            if (n % 2) == 0:
                n = n/2
            else:
                n = (n*3) + 1
        if count > maximum_cycle:
            maximum_cycle = count + 1
    return maximum_cycle
if __name__ == "__main__":
    print(generateASequenceOfNumbers(900, 1000))