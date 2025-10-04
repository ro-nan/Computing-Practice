def linear_least_square(data):
    '''
    Data should look like [[x,y],[x,y],[x,y]]
    Taken from https://www.geeksforgeeks.org/maths/least-square-method/

    n is the number of data points,
    Sumxy is the sum of the product of each pair of x and y values,
    Sumx is the sum of all x values,
    Sumy is the sum of all y values,
    Sumx2 is the sum of the squares of the x values.

    > Slope (m) Formula: m = n(Sumxy)−(Sumx)(Sumy) / n(Sumx2)−(Sumx)2​
    > Intercept (c) Formula: c = (Sumy)−a(Sumx) / n​
    '''
    n = len(data)
    Sumxy = sum(map(lambda xy: xy[0] * xy[1], data))
    Sumx = sum(map(lambda xy: xy[0], data))
    Sumy = sum(map(lambda xy: xy[1], data))
    Sumx2 = sum(map(lambda xy: float(xy[0]) ** 2.0, data))
    
    slope_m = ((n * Sumxy)-(Sumx*Sumy)) / ((Sumx2 * n)-(Sumx ** 2))
    intercept_c = c = ((Sumy)-(slope_m * Sumx)) / n

    return f"y = {slope_m}x + {intercept_c}"

print(linear_least_square([[1,3],[2,4],[3,5],[4,6]]))