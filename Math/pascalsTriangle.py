import math

def get_row(n):
    # Implementation of Pascal's rule: https://en.wikipedia.org/wiki/Pascal%27s_rule
    return [(math.factorial(n)/(math.factorial(k) * math.factorial(n - k))) for k in range(n + 1)]

print(get_row(7))