def squareroot(n):
    '''
    Find Squareroot via Binary Search
    '''

    search_size = 54 # for 15 decimal places of percision which is plenty

    min = 0
    max = n

    guess = 0
    for i in range(search_size):
        if max - min < 1e-16:
            break # Break if we've converged
        
        guess = (min + max) / 2

        if (guess * guess) > n:
            max = guess
        else:
            min = guess

    # Testing with values such as 10000000000, I found that there are some floating point errors, which we try to rectify here to present our value nicely 
    if abs(guess - int(guess)) < 1e-5:
        guess = int(guess)

    print(guess)

squareroot(10000000000) 
    

