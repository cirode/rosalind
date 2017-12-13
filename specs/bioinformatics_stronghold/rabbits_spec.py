from specs import *
from rosalind.bioinformatics_stronghold.rabbits import *


with description('breed'):
  with context('it is given the number of offspring per generation and the number of months to simulate'):
    with it('returns the number of pairs that will be present in the nth month'):
      expect(breed(5,3)).to(equal(19))

