from specs import *
from rosalind.bioinformatics_stronghold.fasta import Fasta


with description('Fasta'):
  with description('#all'):
    with context('the class is initialised with a valid Fasta format'):

      with it('returns an iterable of tuples with the label and base pair string'):
        valid_fasta_contents = '''
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
        '''
        fasta_file = Fasta(valid_fasta_contents)
        list_of_tuples = map(lambda x: x, fasta_file.all())
        expect(list_of_tuples).to(equal([('Rosalind_6404','CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'),('Rosalind_5959','CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC'),('Rosalind_0808','CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT')]))


  with description('#highest_gc_content'):
    with context('the class is initialised with a valid Fasta format'):
      with it('returns a tuple of the label and the gc_content of the highest gc content string'):
        with patch('rosalind.bioinformatics_stronghold.fasta.gc_content', side_effect=[0,0,20]):
          valid_fasta_contents = '''
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
          '''
          fasta_file = Fasta(valid_fasta_contents)
          highest = fasta_file.highest_gc_content()
          expect(highest).to(equal(('Rosalind_0808',20)))
