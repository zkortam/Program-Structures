# Zakaria Kortam - COMSC 78 - Professor Estrada
# April 12, 2023
# 1 Create a GenericMatrix class with a constructor and necissary functions.
# 2. Create IntegerMatrix and RationalMatrix classes that extend the GenericMatrix.
# 3. Make custom functions that override the parent ones for each class, mainly, add,
# multiply, and the to string function.
# 4. Print and format in main.
# 5. For formatting reasons, I also made a fraction simplifier function that simplifies
# the fraction down into the best possible terms.


import math 

def simplify_fraction(fraction):
    num, den = fraction
    gcd = math.gcd(num, den)
    return num // gcd, den // gcd

class GenericMatrix:
    def __init__(self, a,b):
        self.__a = a;
        self.__b = b;

    def __add__(self,other):
        self + other;

    def __mul__(self,other):
        self * other;

    def __zero__(self):
        self;
    
    def __addMatrix__(self,other):
        self;
    
    def __multiplyMatrix__(self,other):
        self;

    def __str__(self):
        self;
    
class IntegerMatrix(GenericMatrix):
    def __init__(self, matrix):
        self.__matrix = matrix

    def __add__(self, other):
        result = [];
        for i in range(len(self.__matrix)):
            row = [];
            for j in range(len(self.__matrix[0])):
                row.append(self.__matrix[i][j] + other.__matrix[i][j])
            result.append(row);
        return IntegerMatrix(result);

    def __mul__(self, other):
        result = [];
        for i in range(len(self.__matrix)):
            row = [];
            for j in range(len(other.__matrix[0])):
                number = 0;
                for k in range(len(other.__matrix)):
                    number += self.__matrix[i][k] * other.__matrix[k][j];
                row.append(number);
            result.append(row);
        return IntegerMatrix(result);

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.__matrix]);

class RationalMatrix(GenericMatrix):
    def __init__(self, matrix):
        self.__matrix = matrix;

    def __add__(self, other):
        result = [];
        for i in range(len(self.__matrix)):
            row = [];
            for j in range(len(self.__matrix[0])):
                n1, d1 = self.__matrix[i][j];
                n2, d2 = other.__matrix[i][j];
                n = n1 * d2 + n2 * d1;
                d = d1 * d2;
                row.append((n, d));
            row = [simplify_fraction(f) for f in row];
            result.append(row);
        return RationalMatrix(result);

    def __mul__(self, other):
        result = [];
        for i in range(len(self.__matrix)):
            row = [];
            for j in range(len(other.__matrix[0])):
                num = 0;
                den = 1;
                for k in range(len(self.__matrix[0])):
                    n1, d1 = self.__matrix[i][k];
                    n2, d2 = other.__matrix[k][j];
                    num += n1 * n2 * den;
                    den *= d1 * d2;
                row.append((num, den));
            row = [simplify_fraction(f) for f in row];
            result.append(row);
        return RationalMatrix(result);

    def __str__(self):
        return '\n'.join(['\t'.join([str(j[0])+'/'+str(j[1]) for j in i]) for i in self.__matrix]);


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>> Zakaria Kortam - COMSC 78 >>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

def main():
    # IntegerMatrix example
    A = IntegerMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
    B = IntegerMatrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]]);
    print("===== Matrix A =====");                             
    print(A);
    print("===== Matrix B =====");
    print(B);
    print("\n\nA + B:");
    print(A + B);
    print("\nA * B:");
    print(A * B);
    print();

    # RationalMatrix example
    C = RationalMatrix([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]);
    D = RationalMatrix([[(8, 7), (6, 5)], [(4, 3), (2, 1)]]);
    print("===== Matrix C =====");
    print(C);
    print("===== Matrix D =====");
    print(D);
    print("\n\nC + D:");
    print(C + D);
    print("\nC * D:");
    print(C * D);                                                     

main()


