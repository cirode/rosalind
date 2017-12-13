import re
from sets import Set

def count_bases(dna_string):
  base_counts = {'A': 0, 'C': 0, 'G': 0, 'T':0}
  for base in dna_string:
    if base in base_counts:
      base_counts[base] += 1
  return '{} {} {} {}'.format(base_counts['A'],base_counts['C'],base_counts['G'],base_counts['T'])


def transcribe(dna_string):
  return re.sub("T","U",dna_string)


def reverse_compliment(dna_string):
  compliment_map = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
  reversed_dna_string =  dna_string[::-1]
  return ''.join(map(lambda x: compliment_map[x],reversed_dna_string))


def gc_content(dna_string):
  return (dna_string.count('G') + dna_string.count('C')) / float(len(dna_string))


def hamming_dist(a, b):
  count = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      count += 1
  return count

def locate_gene(dna_string, gene_string):
  potential_starting_locations = []
  gene_string_length_minus_one = len(gene_string) -1
  matching_positions = []

  for i,nucleotide in enumerate(dna_string):
    if nucleotide == gene_string[0]:
      potential_starting_locations.append(i)

    kept_starting_locations=[]

    for location in potential_starting_locations:
      position = i-location
      if nucleotide == gene_string[position]:
        if position == gene_string_length_minus_one:
          matching_positions.append(location)
        else: 
          kept_starting_locations.append(location)

    potential_starting_locations = kept_starting_locations
  return map(lambda x: x+1,matching_positions) #return in 1 base