def print_primes():

    i = 2
    j = 2
    isComposite = False
    result = ''

    while i <= 20:
        while j < i:
            if i % j == 0:
                isComposite = True
                break
            j = j + 1

        if not isComposite:
            result = result + str(i) + ' '

        isComposite = False
        j = 2
        i = i + 1

    print(result)
    
print_primes()