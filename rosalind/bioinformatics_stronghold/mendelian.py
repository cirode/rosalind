
def probability_dominent(homo_dom=0, hetero=0, homo_rec=0):
  '''returns the probability of random mating producing a dominent individual'''
  total_in_population = float(homo_dom + hetero + homo_rec)
  if total_in_population < 2:
    return 0

  prob_homo_dom_x_homo_dom = homo_dom * (max(0,homo_dom-1))
  prob_homo_dom_x_homo_rec = homo_dom * homo_rec * 2
  prob_homo_dom_x_hetero   = homo_dom * hetero * 2
  prob_homo_rec_x_hetero = homo_rec * hetero * 2
  prob_hetero_x_hetero = hetero * (max(0,hetero-1))

  return (prob_homo_dom_x_homo_dom + \
  prob_homo_dom_x_homo_rec +        \
  prob_homo_dom_x_hetero +          \
  prob_homo_rec_x_hetero*0.5 +      \
  prob_hetero_x_hetero*0.75  )\
  /(total_in_population*(total_in_population-1))

