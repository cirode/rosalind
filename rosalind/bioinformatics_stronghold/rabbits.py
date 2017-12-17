def breed(months,*args,**kwargs):
  return _simulate_breeding(end_month=months,*args,**kwargs)

def _simulate_breeding(end_month, current_month=1, litter_size=1, rabbit_pairs=1, time_to_maturity=1,life_exp=float('inf'),_rabbits_born=None):
  all_arguments = locals()
  dying_rabbits = 0
  if life_exp != float('inf') and current_month >= life_exp:
    dying_rabbits= _rabbits_born[-life_exp]

  if current_month == end_month:
    return rabbit_pairs
  if _rabbits_born is None:
    _rabbits_born = [rabbit_pairs]

  infant_rabbits = sum(_rabbits_born[-(time_to_maturity):])
  adult_rabbits = rabbit_pairs - infant_rabbits
  
  new_rabbits = adult_rabbits*litter_size
  _rabbits_born.append(new_rabbits)
  rabbit_pairs += new_rabbits

  all_arguments.update({ \
    '_rabbits_born': _rabbits_born, \
    'current_month': current_month+1, \
    'rabbit_pairs':rabbit_pairs - dying_rabbits
  })
  return _simulate_breeding(**all_arguments)


# class Population():

#   def __init__(self, litter_size=1,rabbit_pairs=1):
#     self.rabbit_pairs=rabbit_pairs
#     self.life_exp = 1
#     self._litter_size = litter_size
#     self.month = 1
#     self._time_to_maturity = 1
#     self._rabbits_born = [rabbit_pairs]
    

#   def simulate_months(self,months):
#     for _ in xrange(months):
#       # self.dying
#       self.month += 1
#       self.birthing()
#       print(self.month)
#       print(self.rabbit_pairs)
#       print(self._rabbits_born)

#   def birthing(self):
#     new_rabbits = self._adult_rabbits() * self._litter_size
#     self._rabbits_born.append(new_rabbits)
#     self.rabbit_pairs += new_rabbits

#   def _adult_rabbits(self):
#     print("INFants:{}".format(self._infant_rabbits()))
#     return self.rabbit_pairs - self._infant_rabbits()

#   def _infant_rabbits(self):
#     if self.month <= (self._time_to_maturity+1):
#       return self.rabbit_pairs
#     return self.rabbit_pairs - sum(self._rabbits_born[:-(self._time_to_maturity+1)])