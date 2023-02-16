# Zakaria Kortam - COMSC 080
# 1. Have a reciprocal function that takes the reciprocal of a number
# 2. Create a mean function that takes 3 numbers and finds their means.
# 3. Create a Geometric mean function that takes 3 numbers and finds their geometric meanms.
# 4. Create a Hartmonic mean functions that finds the harmonic mean, while using the reciprocal function.
# 5. Test via main.

def reciprocal(number): 
    return round((1/number),2)

def mean(a,b,c):
    return round(((a+b+c)/3),2)


def geometric_mean(a,b,c):
    return round(((a+b+c) ** (1./3.)),2)

def harmonic_mean(a,b,c):
    return round((3/(reciprocal(a) + reciprocal(b) + reciprocal(c))),2)

def main():
    print("Reciprocal of 8 is", reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")
    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")
    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6), \
        "[should be 11.9999..]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 
16.8), \
        "[should be 8.3.999...]")
  
    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3), \
        "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1), \
        "[should be 2.0]")
main()