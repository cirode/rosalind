from specs import *
from rosalind.bioinformatics_stronghold.rna import *


with description('translate'):
  with context('it is given an RNA string of nucleotide bases of a multiple of 3'):
    with it('returns the protein sequence that results'):
      expect(translate('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')).to(equal('MAMAPRTEINSTRING'))

  with context('it is given an RNA string of nucleotide bases not a multiple of 3'):
    with context('with length less than 3'):
      with it('returns an empty string'):
        expect(translate('AU')).to(equal(''))

    with context('with length greater than 3'):
      with it('returns as much of a protein sequence as it can'):
        expect(translate('GUCUAUUA')).to(equal('VY'))


  with context('it is given an RNA string of nucleotide bases with a stop codon in the reading frame midway'):
    with it('returns as much of a protein sequence up to that stop codon'):
        expect(translate('CGGAGGCAAUGACAG')).to(equal('RRQ'))