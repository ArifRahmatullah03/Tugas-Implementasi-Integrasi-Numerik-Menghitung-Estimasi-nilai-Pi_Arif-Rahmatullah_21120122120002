def f(x):
    return 4 / (1 + x**2)

def simpson_one_third(a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)  # initial value
    
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f(a + i * h)  # for even indexes
        else:
            integral += 4 * f(a + i * h)  # for odd indexes
    
    integral *= h / 3
    return integral

a = 0  # lower limit
b = 1  # upper limit
n = 1000  # number of subintervals, can be adjusted for desired accuracy

integral = simpson_one_third(a, b, n)
print("Nilai integral menggunakan Metode Simpson 1/3:", integral)
