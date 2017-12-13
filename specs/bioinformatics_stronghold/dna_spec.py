from specs import *
from rosalind.dna import *


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