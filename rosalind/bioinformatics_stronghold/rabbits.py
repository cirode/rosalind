def breed(month, litter_size):
  return _simulate_breeding(1, litter_size, 0, 1, month)

def _simulate_breeding(current_month, litter_size, adult_rabbit_pairs, infant_rabbit_pairs, stop_at_month):
  total_rabbit_pairs = adult_rabbit_pairs+infant_rabbit_pairs
  if current_month == stop_at_month:
    return total_rabbit_pairs
  else:
    gestating_rabbit_pairs = adult_rabbit_pairs*litter_size
    return _simulate_breeding(current_month+1, litter_size, total_rabbit_pairs, gestating_rabbit_pairs, stop_at_month)
