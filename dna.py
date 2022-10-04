#Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

#Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

#Create a function which translates a given DNA string into RNA.

#For example:

#"GCAT"  =>  "GCAU"

#Adenine pairs with Uracil
#Cytosine pairs with Guanine


def dna_to_rna(dna):
    rna = ""

    for letter in dna:
        if letter == 'A':
            rna += 'U'
        elif letter == 'C':
            rna += 'G'
        elif letter == 'T':
            rna += 'A'
        else:
            rna += 'C'
        
    return rna 



print(dna_to_rna('GATAC'))