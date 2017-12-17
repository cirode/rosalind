import re
import numpy
from sets import Set

PROFILE_MATRIX_KEY_INDEXES=['A','C','G','T']

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
  matching_positions = []
  position = 0
  try:
    while True:
      found_position = dna_string[position:].index(gene_string)
      position = found_position+position+1
      matching_positions.append(position)
  except ValueError:
    return matching_positions

def consensus_profile(dna_string_matrix):
  profile_matrix = [[],[],[],[]]
  depth = len(dna_string_matrix)
  bases = len(dna_string_matrix[0])
  for j in xrange(bases):
    position_counts = dict([key,0] for key in PROFILE_MATRIX_KEY_INDEXES)
    for i in xrange(depth):
      nucleotide = dna_string_matrix[i][j]
      position_counts[nucleotide] += 1
    for position, nucleotide in enumerate(PROFILE_MATRIX_KEY_INDEXES):
      profile_matrix[position].append(position_counts[nucleotide])
  return profile_matrix

def consensus_sequence(profile_matrix):
  depth = len(profile_matrix)
  bases = len(profile_matrix[0])
  sequence = []
  for j in xrange(bases):
    max_position = (profile_matrix[0][j],0)
    for i in xrange(1,depth):
      candidate_position = (profile_matrix[i][j],i)
      if candidate_position[0] > max_position[0]:
        max_position = candidate_position
    sequence.append(PROFILE_MATRIX_KEY_INDEXES[max_position[1]])
  return sequence
