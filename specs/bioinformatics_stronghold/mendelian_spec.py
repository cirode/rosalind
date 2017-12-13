from specs import *
from rosalind.bioinformatics_stronghold.mendelian import *


with description('probability_dominent'):
  with before.each:
    self.acceptable_error = 0.0001


  with context('if all three genotypes in the pop are zero'):
    with it('returns zero'):
      expect(probability_dominent(0,0,0)).to(equal(0))

  with context('if only 1 individual in the pop'):
    with context('that is homzygous_dom'):
      with it('returns zero'):
        expect(probability_dominent(1,0,0)).to(equal(0))

    with context('that is homzygous_rec'):
      with it('returns zero'):
        expect(probability_dominent(0,0,1)).to(equal(0))

    with context('that is hetero'):
      with it('returns zero'):
        expect(probability_dominent(0,0,0)).to(equal(0))    


  with context('two individuals from the same subpopulation in the population'):
    with context('that is homzygous_dom'):
      with it('returns 1'):
        expect(probability_dominent(2,0,0)).to(equal(1))

    with context('that is homzygous_rec'):
      with it('returns 0'):
        expect(probability_dominent(0,0,2)).to(equal(0))

    with context('that is hetero'):
      with it('returns 0.75'):
        expect(probability_dominent(0,2,0)).to(be_within_error_of(0.75, error=self.acceptable_error))

  with context('with mixed populations'):
    with context('1 homozygous_dom, 1 homogygous_rec'):
      with it('returns 1'):
        expect(probability_dominent(1,0,1)).to(equal(1))

    with context('1 hetero, 1 homogygous_rec'):
      with it('returns 0.5'):
        expect(probability_dominent(0,1,1)).to(equal(0.5))

    with context('that is two of each (rosalind example)'):
      with it('returns 0.78333'):
        expect(probability_dominent(2,2,2)).to(be_within_error_of(0.78333, error=self.acceptable_error))
