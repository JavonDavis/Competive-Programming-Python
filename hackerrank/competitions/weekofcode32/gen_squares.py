def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, min(int((5*pow(10, 5))**0.5), int(n**0.5)) + 1) if n % i == 0)))
d = {}
squares = [x**2 for x in range(1, 5*pow(10, 5) + 1)]

for square in squares:
    d[square] = factors(square)

print d

