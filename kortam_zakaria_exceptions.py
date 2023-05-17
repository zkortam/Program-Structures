

from fractions import Fraction;

#Zakaria Kortam - COMSC 78 - Exceptions
#Professor Estrada - 4/26 

#1. The read int function has a while loop, where it runs until a proper
#integer is inputted by the user. If the integer is valid, it returns the value
#, otherwise, it keeps asking and launches an exception. It has been commented out as it
# is not being used.
#2. The readVal function takes in the data type, promp and error messages. It does everything
# that the readInt function did, but general and across different numerical datatypes.
#3. Within the main function, for each value type, I had them all call the readVal function with the
#parameters filled according to the data type. 
#4. The value returned from the readVal function is printed. 
#5. For complex numbers, I added an additional filter that checks if the complex value has been set. If
# it hasn't, then it'll simply print out the number without the complex section. If it has, it'll print as normal.
# This is to avoid instances like (1 + 0j) or (5 + 0j)

#def readInt():
#    while True:
#        try:
#            intVal = int(input("Enter an integer value: "));
#            return intVal;
#        except ValueError:
#            print("Input is not an integer. Please try again.");


def readVal(valType, promptMsg, errorMsg):
    while True:
        try:
            val = valType(input(promptMsg));
            return val;
        except ValueError:
            print(errorMsg);


def isComplexSet(complex_val):
    try:
        complex_num = complex(complex_val)
        if complex_num.imag == 0:
            return False
        return True
    except ValueError:
        return False


def main():
    
    intVal = readVal(int, "Enter an integer: ", "Invalid. Please enter an integer.");
    print("The square of the integer you entered is:", intVal**2);

    fracVal = readVal(Fraction, "Enter a fraction (e.g. 1/3): ", "Invalid. Please enter a fraction.");
    print("The numerator of the fraction you entered is:", fracVal.numerator);

    floatVal = readVal(float, "Enter a floating point number: ", "Invalid. Please enter a floating point number.");
    print("The square root of the floating point number you entered is:", floatVal**0.5);

    complexVal = readVal(complex, "Enter a complex number (e.g. 1+2j): ", "Invalid. Please enter a properly formatted complex number.");

    if isComplexSet(complexVal):
        print("The complex number you entered is:", complexVal);
    else:
        print("The complex number you entered is:", complexVal.real);

main()