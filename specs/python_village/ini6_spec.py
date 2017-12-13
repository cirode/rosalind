from specs import *
from rosalind.python_village.ini6 import *

with description('count_words'):
  with context('when given an string of words'):
    with it('returns a dict of words with counts'):
      string = '''We tried list and we tried dicts also we tried Zen'''
      expect(count_words(string)).to(equal({'and': 1,'We': 1, 'tried': 3, 'dicts': 1, 'list': 1,'we': 2,'also':1, 'Zen':1}))