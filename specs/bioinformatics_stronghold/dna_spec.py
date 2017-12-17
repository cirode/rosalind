from specs import *
from rosalind.bioinformatics_stronghold.dna import *
import numpy

with description('count_bases'):
  with context('it is given a string of nucleotide bases'):
    with it('returns the count for those bases'):
      expect(count_bases('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')).to(equal('20 12 17 21'))


with description('transcribe'):
  with context('it is given a string of DNA nucleotide bases'):
    with it('returns the corresponding RNA nucleotide string'):
      expect(transcribe('GATGGAACTTGACTACGTAAATT')).to(equal('GAUGGAACUUGACUACGUAAAUU'))


with description('reverse_compliment'):
  with context('it is given a string of DNA nucleotide bases'):
    with it('returns the corresponding RNA nucleotide string (Example 1)'):
      expect(reverse_compliment('GTCA')).to(equal('TGAC'))

  with context('it is given a string of DNA nucleotide bases'):
    with it('returns the corresponding RNA nucleotide string (Example 2)'):
      expect(reverse_compliment('AAAACCCGGT')).to(equal('ACCGGGTTTT'))


with description('gc_content'):
  with context('it is given a string of DNA nucleotide bases'):
    with it('returns the fraction of the bases in the string that are a G or a C'):
      expect(gc_content('AGCTATAG')).to(equal(0.375))


with description('hamming_dist'):
  with context('it is given two strings of equal length'):
    with it('returns the number of positions in those strings that differ'):
      expect(hamming_dist('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT')).to(equal(7))


with description('locate_gene'):
  with context('it is given a DNA string and a GENE string of nucleotide bases'):
    with it('returns an array of locations the GENE exists in the DNA string (Example 1)'):
      expect(locate_gene('AUGCUUCAGAAAGGUCUUACG','U')).to(equal([ 2, 5, 6, 15, 17, 18]))

    with it('returns an array of locations the GENE exists in the DNA string (Example 2)'):
      expect(locate_gene('GATATATGCATATACTT','ATAT')).to(equal([ 2,4,10]))

with description('concensus_profile'):
  with context('it is given an mxn matrix of DNA strings'):
    with it('returns an 4xn profile matrix of base counts'):
      dna_strings_matrix = [\
        ['A','T','C','C','A','G','C','T'],\
        ['G','G','G','C','A','A','C','T'],\
        ['A','T','G','G','A','T','C','T'],\
        ['A','A','G','C','A','A','C','C'],\
        ['T','T','G','G','A','A','C','T'],\
        ['A','T','G','C','C','A','T','T'],\
        ['A','T','G','G','C','A','C','T'],\
      ]
      expected_profile_matrix = [\
        [5,1,0,0,5,5,0,0],#A \ 
        [0,0,1,4,2,0,6,1],#C \ 
        [1,1,6,3,0,1,0,0],#G \
        [1,5,0,0,0,1,1,6],#T \
      ]
      expect(concensus_profile(dna_strings_matrix)).to(equal_array(expected_profile_matrix))

with description('concensus_sequence'):
  with context('it is given profile matrix'):
    with it('returns the concensus_sequence'):
      profile_matrix = [\
        [5,1,0,0,5,5,0,0],#A \ 
        [0,0,1,4,2,0,6,1],#C \ 
        [1,1,6,3,0,1,0,0],#G \
        [1,5,0,0,0,1,1,6],#T \
      ]
      expected_consensus_sequence = ['A','T','G','C','A','A','C','T']
      expect(concensus_sequence(profile_matrix)).to(equal(expected_consensus_sequence))


