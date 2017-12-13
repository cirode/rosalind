from expects import *
from mock import patch
import pdb

def be_within_error_of(expected, error=0.01):
  high_value = expected + error
  low_value = expected - error
  return be_within(low_value,high_value)