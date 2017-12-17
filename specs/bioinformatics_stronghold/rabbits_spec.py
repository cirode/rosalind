from specs import *
from rosalind.bioinformatics_stronghold.rabbits import *


with description('breed'):
  with context('it is given the number of offspring per generation and the number of months to simulate (fib)'):
    with it('returns the number of pairs that will be present in the nth month (assuming a life_exp of INF)'):
      expect(breed(litter_size=3,months=5)).to(equal(19))

  with context('it is given the number of months each generation lives and the number of months to simulate (fibd)'):
    with it('returns the number of pairs that will be present in the nth month (assuming a litter_size of 1)'):
      expect(breed(life_exp=3,months=6)).to(equal(4))

