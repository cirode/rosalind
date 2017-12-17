from specs import *
from rosalind.bioinformatics_stronghold.problems import *

with description('cons'):
  with context('it is given a fasta file contents as a string'):
    with it('prints the consensus string and consensus profile'):
      with patch('rosalind.bioinformatics_stronghold.problems.print') as mock_print:
        input_string = '''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT'''
        expected_output = '''ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6'''
        cons(input_string)
        mock_print.assert_called_with(expected_output)
