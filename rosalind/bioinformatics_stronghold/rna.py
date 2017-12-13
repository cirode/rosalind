from sets import Set

STOP_AMINO_ACID='Stop'
RNA_CODON_TABLE={'UUU':'F','CUU': 'L','AUU':'I','GUU':'V',\
'UUC':'F','CUC':'L','AUC':'I','GUC':'V','UUA':'L','CUA':'L',\
'AUA':'I','GUA':'V','UUG':'L','CUG':'L','AUG':'M','GUG':'V',\
'UCU':'S','CCU':'P','ACU':'T','GCU':'A','UCC':'S','CCC':'P',\
'ACC':'T','GCC':'A','UCA':'S','CCA':'P','ACA':'T','GCA':'A',\
'UCG':'S','CCG':'P','ACG':'T','GCG':'A','UAU':'Y','CAU':'H',\
'AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D',\
'UAA':STOP_AMINO_ACID,'CAA':'Q','AAA':'K','GAA':'E',\
'UAG':STOP_AMINO_ACID,'CAG':'Q','AAG':'K','GAG':'E','UGU':'C',\
'CGU':'R','AGU':'S','GGU':'G','UGC':'C','CGC':'R','AGC':'S',\
'GGC':'G','UGA':STOP_AMINO_ACID,'CGA':'R','AGA':'R','GGA':'G',\
'UGG':'W','CGG':'R','AGG':'R','GGG':'G'}

def translate(rna_string):
  protein_string = ''
  for i in xrange(3,len(rna_string),3):
    amino_acid = RNA_CODON_TABLE[rna_string[i-3:i]]
    if amino_acid == STOP_AMINO_ACID:
      return protein_string
    protein_string += amino_acid
  return protein_string
  
