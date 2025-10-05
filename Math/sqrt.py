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
    if abs(guess - round(guess, 1)) < 1e-5:
        guess = round(guess, 1)
    
    print("sqrt(", n, ") ~", guess)

squareroot(1) 
squareroot(2)
squareroot(4)
squareroot(15)
squareroot(16)
squareroot(100)
squareroot(1000)
squareroot(10000)
squareroot(100000)


