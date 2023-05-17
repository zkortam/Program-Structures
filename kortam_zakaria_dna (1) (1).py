# Zakaria Kortam - Professor Estrada - 3/22/2023
# DNA Assignment
# 1. Ask the user to enter their input sequence
# 2. Refine and clean it to make sure it has the proper characters. 
# 3. split them into 3 character groups.
# 4. Check to see if the length of the triplet string is less then 3,
# if so, then thee program will declare that it is insufficient and doesn't have 3 
# letters.
# 5. Then, the program checks to see if the characters in the triplet are present within the valid letters
# set. If not, it will declare an error.
# 6. Otherwise, the program will resume as normal.
# 7. The program repeats until the user presses enter, where it stops.
# 8. The collection of all of the Amino Acid and Nucleotides are present within the table. The 
# colon acts as a seperator that indicates the correspondance between the nucleotide and amino acid.


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>> Zakaria Kortam - COMSC 78 >>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

def clean_sequence(sequence):
    result = ''
    for char in sequence:
        if char.isalpha():
            result += char.upper()
    return result

def split(string):
    return [string[i:i+3] for i in range(0, len(string), 3)]

def main():
    inputStr = input("Enter a nucleotide sequence, or press ENTER to quit: ")
    while inputStr:
        # Refinement
        cleanedStr = clean_sequence(inputStr)
        triplets = split(cleanedStr)
        invalid_sequence = False
        for triplet in triplets:
            # Check Validity
            if len(triplet) < 3:
                print(f"Invalid sequence. The sequence {triplet} does not have 3 letters.")
                invalid_sequence = True
            elif not set(triplet).issubset(valid_letters):
                print(f"Invalid sequence. The sequence {triplet} contains non-standard nucleotides.")
                invalid_sequence = True
            else:
                # Correspondance Check
                if triplet in table:
                    amino_acid = table[triplet]
                    print(f'{triplet}:{amino_acid}')
                else:
                    print(f"Invalid sequence. The sequence {triplet} does not code for any amino acid.")
                    invalid_sequence = True
        if invalid_sequence:
            inputStr = input("Enter a valid nucleotide sequence, or press ENTER to quit: ")
        else:
            inputStr = input("Enter a nucleotide sequence, or press ENTER to quit: ")
    # End of Program
    print("\n\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>> Program has ended. >>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

 # Database of Information
valid_letters = {'U','A','C','G'}
table = {
    "UUU": "Phe", "UCU": "Ser", "UAU": "Tyr", "UGU": "Cys",
    "UUC": "Phe", "UCC": "Ser", "UAC": "Tyr", "UGC": "Cys",
    "UUA": "Leu", "UCA": "Ser", "UGA": "***", "UAA": "***",
    "UUG": "Leu", "UCG": "Ser", "UGG": "Trp", "UAG": "***",
    "CUU": "Leu", "CCU": "Pro", "CAU": "His", "CGU": "Arg",
    "CUC": "Leu", "CCC": "Pro", "CAC": "His", "CGC": "Arg",
    "CUA": "Leu", "CCA": "Pro", "CAA": "Gln", "CGA": "Arg",
    "CUG": "Leu", "CCG": "Pro", "CAG": "Gln", "CGG": "Arg",
    "GUU": "Val", "GCU": "Ala", "GAU": "Asp", "GGU": "Gly",
    "GUC": "Val", "GCC": "Ala", "GAC": "Asp", "GGC": "Gly",
    "GUA": "Val", "GCA": "Ala", "GAA": "Glu", "GGA": "Gly",
    "GUG": "Val", "GCG": "Ala", "GAG": "Glu", "GGG": "Gly"
}

main()
