import re
from rosalind.dna import gc_content

class Fasta:

  def __init__(self, fasta_string):
    self.fasta_string = fasta_string

  def all(self):
    label = None
    string = ''
    for line in self.fasta_string.split('\n'):
      if line.startswith('>'):
        if label != None:
          yield (label, string)
          string = ''
        label = line[1:]
      else:
        string += line.strip()
    yield (label, string)

  def highest_gc_content(self):
    max_so_far = None
    for segment in self.all():
      candidate = (segment[0], gc_content(segment[1]))
      if max_so_far is None:
        max_so_far = candidate
      elif candidate[1] > max_so_far[1]:
        max_so_far = candidate
    return max_so_far
