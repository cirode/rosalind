from expects import *
from mock import patch
import pdb
from expects.matchers import Matcher
import numpy


def be_within_error_of(expected, error=0.01):
  high_value = expected + error
  low_value = expected - error
  return be_within(low_value,high_value)

class equal_array(Matcher):

  def __init__(self, expected):
      self._expected = expected

  def _match(self, array):
    if numpy.array_equal(array, self._expected):
      return True, ['arrays match']
    return False, ['arrays do not match']