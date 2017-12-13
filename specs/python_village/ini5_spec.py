from specs import *
from rosalind.python_village.ini5 import *
from cStringIO import StringIO

with description('even_lines'):
  with context('when given an io object'):
    with it('returns an array with the even lines (1s based)'):
      string = '''Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat'''
      io = StringIO(string)
      expect(even_lines(io)).to(equal(\
        ['Yes, brave Sir Robin turned about',\
        'And gallantly he chickened out',\
        'Bravely talking to his feet',\
        'He beat a very brave retreat']))