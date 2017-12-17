from __future__ import print_function
from fasta import Fasta
from dna import consensus_sequence, consensus_profile,PROFILE_MATRIX_KEY_INDEXES


def cons(input_string):
  '''http://rosalind.info/problems/cons/'''
  fasta = Fasta(input_string)
  matrix = []
  read_matrix = [read_string for label, read_string in fasta.all()]
  profile = consensus_profile(read_matrix)
  sequence = consensus_sequence(profile)
  print_lines = [''.join(sequence)]
  print_lines += ['{}: {}'.format(PROFILE_MATRIX_KEY_INDEXES[i], ' '.join(map(str,read))) \
    for i, read in enumerate(profile)]
  print('\n'.join(print_lines))

